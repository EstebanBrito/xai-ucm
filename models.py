import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def load_inception_v1():
    model = tf.keras.Sequential([
        hub.KerasLayer(
            name='inception_v1',
            handle='https://tfhub.dev/google/imagenet/inception_v1/classification/4',
            trainable=False
        )
    ])
    model.build([None, 224, 224, 3])
    return model

def load_imagenet_labels(url='https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'):
    labels_file = tf.keras.utils.get_file('ImageNetLabels.txt', url)
    with open(labels_file) as reader:
        f = reader.read()
        labels = f.splitlines()
    return np.array(labels)

def get_pred_class_idx(model, labels, image):
    image_batch = tf.expand_dims(image, 0)
    predictions = model(image_batch)
    probs = tf.nn.softmax(predictions, axis=-1)
    top_probs, top_idxs = tf.math.top_k(input=probs, k=1)
    top_label = labels[tuple(top_idxs[0])]
    return top_idxs[0].numpy()[0]