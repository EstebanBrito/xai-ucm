import os
from tensorflow import zeros

baseline = zeros(shape=(224,224,3))
interp_steps = 10
alpha_ratio = (0.5, 0.5)
cmap = 'hot'

# Constants
IMG_FOLDER = os.path.join('.', 'imgs')
IG_FOLDER = os.path.join(IMG_FOLDER, 'ig')
LIME_FOLDER = os.path.join(IMG_FOLDER, 'lime')
ANCHOR_FOLDER = os.path.join(IMG_FOLDER, 'anchor')