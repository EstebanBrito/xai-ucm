# INTERPRETATION IMAGES GENERATOR "XAI"

This tool is used to generate interpretation images for any arbitrary dataset of images. The techniques used for interpretations are Integrated Gradients (IG), LIME, XRAI and ANCHOR. The first three used Inception V1 as their CNN arquitechture, while the last one uses Inception V3.

## REQUIREMENTS
This project used Python 3.9+ but should work with any Python 3.6+ installation.

Also, the project uses several scientific Python libraries, like Tensorflow or Numpy, to name a few.

### Virtual environment
Althoug the libraries needed for the project can be installed globally, is it highly recommended that virtual environments are used. We used virtualenv module to generate these environments, but other tools (like conda), can be used too.

#### Virtualenv installation and setup
If you don't have virtualenv, install it

```bash
$ pip install virtualenv
```

Once installed, position your terminal prompt inside the project root directory, and create the virtual environment using

```bash
$ python -m virtualenv env
```

Activate the environment in Power Shell with:

```bash
$ env\Scripts\activate.bat
```

or, the system is Linux based, use:

```bash
$ sh env\bin\activate
```

Once activated (you shoudl see a "(env)" at the beggining of the console prompt), install libraries in the next section.

### Install dependencies

The project uses many libraries, with specific versions so they do not cause errors.

Install them with:

```bash
$ pip install -r requirements.txt
```

If, by any reason, an error happens, installation can be manual:

```bash
$ pip install tensorflow scikit-image numpy matplotlib pillow 
```




## PROJECT STRUCTURE

## EXECUTION

The project uses 4 scripts to generate interpretation images, one script for each interpretion technique. The files used to generate images are:
- generate_ig.py (IG)
- generate_lime.py (LIME)
- generate_xrai.py (XRAI)
- generate_anchor.py (ANCHOR)

To generate images, simply type the folowing in a terminal

```bash
$ python [script_name]
```

For example, to generate LIME images, type

```bash
$ python generate_lime.py
```

As explained in the "Project Structure" section, images will be saved in the imgs/lime folder.

Take note that the execution time for each one of those depends on the technique that was used. We provide a rouch estimate for the interpretation time for a single image depending on the technique:

- IG : 25 sec
- LIME: 2 min 30 sec

These times can vary, because they were tested on an AMD A8 2.9Ghz CPU, using no GPU or any other parallel computing tool.