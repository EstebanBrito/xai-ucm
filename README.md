# INTERPRETATION IMAGES GENERATOR "XAI"

This tool is used to generate interpretation images for any arbitrary dataset of images. The techniques used for interpretations are Integrated Gradients (IG), LIME, XRAI and ANCHOR. The first three used Inception V1 as their CNN arquitechture, while the last one uses Inception V3.

# REQUIREMENTS
This project used Python 3.8.5 but should work with any Python 3.6+ installation.

Also, the project uses several scientific Python libraries, like Tensorflow and Numpy, to name a few.

## Virtual environment
Although the libraries needed for the project can be installed globally, is it highly recommended that virtual environments are used. We used virtualenv module to generate these environments, but other tools (like conda), can be used too.

### Virtualenv installation and setup
If you don't have virtualenv, install it

```bash
$ pip install virtualenv
```

Once installed, position your terminal prompt inside the project root directory (if the project is inside your desktop, then navigate to "/desktop/xai-ucm" using the "cd" command), and create the virtual environment using

```bash
$ python -m virtualenv env
```

For Windows, activate the environment in Power Shell (not cmd) with:

```bash
$ env\Scripts\activate.bat
```

or, if the system is Linux based, use:

```bash
$ source env\bin\activate
```

Once activated (you should see an "(env)" at the beggining of the console prompt), install libraries in the next section.

## Install dependencies

The project uses many libraries, with specific versions so they do not cause errors.

### Image generation dependencies

If you want to use the generation functionalities of the project, use the following command

```bash
$ pip install -r requirements-gen.txt
```

If, by any reason, an error happens, installation can be manual:

```bash
$ pip install tensorflow==2.4 tensorflow_hub==0.11.0 alibi==0.5.5 lime==0.2.0.1 pillow==8.2.0 scikit-image==0.18.1 matplotlib==3.4.1 numpy==1.19.5
```

### Image labeling dependencies

If you also want to use the labeling functionalities of the project, use the following command

```bash
$ pip install -r requirements-gui.txt
```

If, by any reason, an error happens, installation can be manual:

```bash
$ pip install pillow==8.2.0
```


# PROJECT STRUCTURE

The repository comes with a folder called "imgs". Put any image that you want to interpret inside and run the script mentioned in the section "Execution".   

Also note that images should fullfill certain requirements:   
- Images must be in JPEG format (extensions '.jpg' or '.jpeg)
- Images' name must have the following name structure (additional doble underscores are not permitted, only single underscores)
    - [something]\__[string]__[something].[extension]
    - Example: 2377698__zebra__0.9999999.jpg
    - Example: 4339__manhole_cover__0.99999416

When you use any of the generation scripts of the project, 4 new folders can be found inside the imgs folder. These folders contain interpretation images made with the 4 interpretation techniques mentioned before. The name for the images inside any of these folders will be the same as the name of the original images (where the interpretation was produced from), which are present int the "imgs" folder, but with the '.png' extension instead of the '.jpg'/'.jpeg' extension.   

When you run the GUI script and finished voting, a file "labels.txt" will be generated at the root of the project folder. It will be composed of X rows (where X is the number of images present at the root of the "imgs" folder), each of the rows following this structure:
- NAME_OF_THE_IMAGE,MODEL_VOTED
- Example: 2377698__zebra__0.9999999.jpg,LIME
- Example: 4339__manhole_cover__0.99999416,IG

MODEL VOTED can be one of the following: IG, LIME, XRAI, ANCHOR

# EXECUTION AND USAGE

## Image Generation

The project uses 3 scripts to generate interpretation images, one script for each interpretion technique (XRAI generation script has not been finished yet). The files used to generate images are:
- generate_ig.py (for Integrated Gradients technique)
- generate_lime.py (for LIME technique)
- generate_xrai.py (for XRAI technique)
- generate_anchor.py (for ANCHOR technique)

To generate images, simply type the folowing in a terminal

```bash
$ python [script_name]
```

For example, to generate LIME images, type

```bash
$ python generate_lime.py
```

As explained in the "Project Structure" section, images for the exmaple script will be saved in the imgs/lime folder.

Take note that the execution time for each one of those depends on the technique that was used. We provide a rouch estimate for the interpretation time for a single image depending on the technique:

- IG : 25 sec
- LIME: 2 min 30 sec
- ANCHOR: 5 min (Beware of this technique. During testing, some images took up to 20 minutes)

These times can vary, because they were tested on an AMD A8 2.9Ghz CPU, using no GPU or any other parallel computing tool. However, they can be used in any machine with a GPU installed, given that tensorflow 2.4 is compatible with the graphics card drivers.

Also, the memory used by these scripts can reach up to 2 GB, so that should be kept in mind.

## Image voting/labeling

To start labeling images, simple type:

```bash
$ python gui.py
```

A home window will appear. Click on "Iniciar" and a series of windows with images will appear. Follow the instrucions given in those image windows. The number of image windows will be the same as the number of images at the root of the folder "imgs". You can see the images voted so far and the total of images at the upperf left side of the image windows.   

Once you have voted for the last image, a "Thank You" window will appear, with instruction of what to do next. Also, a "labels.txt" file will appear inside the project folder. The instruction of the "Thank you" windows will ask you to send that file to someone.