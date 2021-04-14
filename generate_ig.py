import os
from tensorflow import zeros

import models
import utils
from settings import IG_FOLDER, cmap
from ig import integrated_gradients

baseline = zeros(shape=(224,224,3))
print('-----SETUP-----')
# Setup
utils.setup_folder_structure()

print('-----LOAD MODELS-----')
# Load models
model = models.load_inception_v1()
labels = models.load_imagenet_labels()

print('-----LOAD IMAGES-----')
# Load images info
img_paths = utils.load_img_paths()
img_tensors = utils.load_img_tensors(img_paths)
img_preds = utils.get_imgs_classes(model, labels, img_tensors)

print('-----INTERPRETATIONS-----')
# For each image
for name, tensor in img_tensors.items():
    # Generate IG's
    mask = integrated_gradients(model=model,
                                baseline=baseline,
                                image=tensor,
                                target_class_idx=img_preds[name],
                                m_steps=10)
    # Merge images
    mask_img = utils.convertMatrixToRGBA(mask.numpy(), cmap)
    orig_img = utils.convertMatrixToRGBA(tensor.numpy())
    merged_img = utils.merge_images(orig_img, mask_img)
    # Save images
    new_name = name.split('.')[0]
    new_ig_img_url = os.path.join(IG_FOLDER, f'{new_name}.png')
    utils.saveImageFile(merged_img, new_ig_img_url)