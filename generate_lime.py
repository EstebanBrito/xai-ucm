import os
from skimage.io import imread

from tensorflow.keras.applications import inception_v3 as inc_net
from tensorflow.keras.preprocessing import image

from lime import lime_image

from skimage.segmentation import mark_boundaries

from settings import IMG_FOLDER, LIME_FOLDER
from utils import convertMatrixToRGBA, saveImageFile, file_is_image, load_img_paths, setup_folder_structure
from models import load_inception_v1

def transform_img_fn(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = inc_net.preprocess_input(x)
    return x


if __name__ == '__main__':
    count = 1
    
    setup_folder_structure()
    print('LOADING MODELS')
    explainer = lime_image.LimeImageExplainer()
    model = load_inception_v1()
    print('GENERATING LIME IMAGES')
    img_paths = load_img_paths()
    for img_name, img_path in img_paths.items():
        img = transform_img_fn(img_path)
        explanation = explainer.explain_instance(img.astype('double'),
                                                model.predict,
                                                top_labels=5,
                                                hide_color=0,
                                                num_samples=1000)
        exp_img, mask = explanation.get_image_and_mask(explanation.top_labels[0],
                                                    positive_only=True, 
                                                    num_features=10, 
                                                    hide_rest=True)
        interp_img = mark_boundaries(exp_img/2 + 0.5, mask)
        new_img = convertMatrixToRGBA(interp_img)
        new_img_name = img_name.split('.')[0]
        new_img_path = os.path.join(LIME_FOLDER, f'{new_img_name}.png')
        saveImageFile(new_img, new_img_path)
        print(f'Generated Images: {count}/{img_paths.__len__()}')
        count += 1
