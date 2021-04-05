import os
import tensorflow as tf

baseline = tf.zeros(shape=(224,224,3))
interp_steps = 10
alpha_ratio = (0.5, 0.5)
cmap = 'hot'

# Constants
IMG_FOLDER = os.path.join('.', 'imgs')
IG_FOLDER = os.path.join(IMG_FOLDER, 'ig')