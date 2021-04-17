import tkinter as tk
from PIL import ImageTk, Image
import os
import sys

from settings import IMG_FOLDER, IG_FOLDER, LIME_FOLDER, XRAI_FOLDER, ANCHOR_FOLDER

LABELS_FILE = os.path.join('.', 'labels.txt')

def get_class_from_filename(filename):
    rough_name = filename.split('__')[1]
    clean_name = rough_name.replace('_', ' ').upper()
    return clean_name

def get_name_without_ext(filename):
    return '.'.join(filename.split('.')[:-1])

def load_img_names():
    return [img_name for img_name in os.listdir(IMG_FOLDER) if file_is_image(img_name)]

def file_is_image(img_name):
    return img_name.split('.')[-1]=='jpeg' or img_name.split('.')[-1]=='jpg'


class LabelerApp():
    count = 0
    img_names = load_img_names()
    labeled_images = {}

    def __init__(self):
        self._window = None
        self.switch_window(WelcomeWindow)

    def switch_window(self, window):
        kwargs = {}
        if window is ImageViewerWindow:
            if len(self.img_names)!=0:
                if self.count < len(self.img_names):
                    kwargs = {
                        'image_name': self.img_names[self.count],
                        'image_number': self.count + 1,
                        'no_of_images': len(self.img_names),
                        'labels': self.labeled_images
                    }
                    self.count += 1
                else:
                    # Save images and thank the user
                    self.saveLabelsToFile()
                    window = ThankYouWindow
            else:
                print('No images detected')
                exit(0)
        new_window = window(self, **kwargs)
        # Create and show window
        if self._window is not None:
            self._window.destroy()
        self._window = new_window
        self._window.mainloop()
    
    def saveLabelsToFile(self):
        if os.path.exists(LABELS_FILE): os.remove(LABELS_FILE)
        f = open(LABELS_FILE, 'wt')
        for img, label in self.labeled_images.items():
            f.write(f'{img},{label}\n')
        f.close()


class WelcomeWindow(tk.Tk):
    w, h = 600, 400

    def __init__(self, app):
        # Prev. configurations
        super().__init__()
        # Window options
        self.title('Proyecto XAI-UCM: Votación de Imágenes')
        self.geometry(f'{self.w}x{self.h}')
        self.resizable(False, False)
        # Windows text
        title = tk.Label(self, text='VOTACIÓN DE IMÁGENES. PROYECTO XAI-UCM')
        title.place(x=0, y=30, width=self.w)
        title.config(font=('Arial', 18, 'bold'), justify=tk.CENTER)
        inst = tk.Label(self, text='Presione "Iniciar" o "Leer Instrucciones"')
        inst.place(x=0, y=70, width=self.w)
        inst.config(font=('Arial', 14), justify=tk.CENTER)
        # Buttons
        btn1 = tk.Button(self, text='Iniciar', bd=5, command=lambda: app.switch_window(ImageViewerWindow))
        btn1.place(x=270, y=150)
        btn1.config(font=('Arial', 12))
        btn2 = tk.Button(self, text=f'Leer instrucciones', bd=5)
        btn2.place(x=230, y=200)
        btn2.config(font=('Arial', 12))


class ImageViewerWindow(tk.Tk):
    app = None
    # Window measurements
    main_img_size, normal_img_size = 200, 150
    space_between = 50
    w = 850 # 4*normal_img_size + 5*space_between
    h = 600
    # Image info
    labels = None
    image_name = None
    # References to imgs are needed, for tkinter does not hold references
    main_img = None
    img1 = None
    img2 = None
    img3 = None
    img4 = None

    def __init__(self, app, image_name, image_number, no_of_images, labels):
        # Prev. configurations
        super().__init__()
        self.app = app
        self.labels = labels
        self.image_name = image_name
        # Window configurations
        self.geometry(f'{self.w}x{self.h}')
        self.title(f'Imagen {image_number}/{no_of_images}')
        self.resizable(False, False)
        # Main img and instructions
        self.load_images_widgets(image_name)
        class_name = get_class_from_filename(image_name)
        main_lbl = tk.Label(self, image=self.main_img)
        main_lbl.place(x=325, y=10, width=self.main_img_size, height=self.main_img_size)
        text = tk.Label(self, text=f'¿Cuál de las imágenes de abajo explica de mejor manera la imagen de arriba? (Se trata de un {class_name})\nPresiona el botón debajo de la imagen de tu elección')
        text.place(x=0, y=210, width=self.w, height=60)
        text.config(font=('Arial', 12, 'bold'), justify=tk.CENTER)
        # Images
        lbl1 = tk.Label(self, image=self.img1)
        lbl1.place(x=50, y=280, width=self.normal_img_size, height=self.normal_img_size)
        lbl2 = tk.Label(self, image=self.img2)
        lbl2.place(x=250, y=280, width=self.normal_img_size, height=self.normal_img_size)
        lbl3 = tk.Label(self, image=self.img3)
        lbl3.place(x=450, y=280, width=self.normal_img_size, height=self.normal_img_size)
        lbl3 = tk.Label(self, image=self.img4)
        lbl3.place(x=650, y=280, width=self.normal_img_size, height=self.normal_img_size)
        # Buttons
        btn1 = tk.Button(self, text='OPCION 1', bd=5, command=lambda: self.load_next_image_viewer('IG'))
        btn1.place(x=50, y=460, width=self.normal_img_size)
        btn1.config(font=('Arial', 10), justify=tk.CENTER)
        btn2 = tk.Button(self, text='OPCION 2', bd=5, command=lambda: self.load_next_image_viewer('LIME'))
        btn2.place(x=250, y=460, width=self.normal_img_size)
        btn2.config(font=('Arial', 10), justify=tk.CENTER)
        btn3 = tk.Button(self, text='OPCION 3', bd=5, command=lambda: self.load_next_image_viewer('XRAI'))
        btn3.place(x=450, y=460, width=self.normal_img_size)
        btn3.config(font=('Arial', 10), justify=tk.CENTER)
        btn4 = tk.Button(self, text='OPCION 4', bd=5, command=lambda: self.load_next_image_viewer('ANCHOR'))
        btn4.place(x=650, y=460, width=self.normal_img_size)
        btn4.config(font=('Arial', 10), justify=tk.CENTER)

    def load_images_widgets(self, img_name):
        size_main = (self.main_img_size, self.main_img_size)
        size_normal = (self.normal_img_size, self.normal_img_size)
        img_name_png = f'{get_name_without_ext(img_name)}.png'
        self.main_img = ImageTk.PhotoImage(master=self, image=Image.open(os.path.join(IMG_FOLDER, img_name)).resize(size_main))
        self.img1 = ImageTk.PhotoImage(master=self, image=Image.open(os.path.join(IG_FOLDER, img_name_png)).resize(size_normal))
        self.img2 = ImageTk.PhotoImage(master=self, image=Image.open(os.path.join(LIME_FOLDER, img_name_png)).resize(size_normal))
        self.img3 = ImageTk.PhotoImage(master=self, image=Image.open(os.path.join(XRAI_FOLDER, img_name_png)).resize(size_normal))
        self.img4 = ImageTk.PhotoImage(master=self, image=Image.open(os.path.join(ANCHOR_FOLDER, img_name_png)).resize(size_normal))
    
    def calc_img_x(self, img_no):
        return self.space_between + (img_no-1)*(self.normal_img_size + self.space_between)
    
    def register_label(self, label):
        self.labels[self.image_name] = label

    def load_next_image_viewer(self, label):
        self.register_label(label)
        self.app.switch_window(ImageViewerWindow)


class InstructionsWindow(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.geometry('200x200')
        self.resizable(False, False)


class ThankYouWindow(tk.Tk):
    w, h = 400, 400

    def __init__(self, app):
        super().__init__()
        self.geometry(f'{self.w}x{self.h}')
        self.resizable(False, False)
        self.title('Votación Terminada')
        # Widgets
        texto = '''
        Muchas gracias por cooperar en la votación.\n
        En la carpeta "xai-ucm" se ha generado un archivo\n
        de nombre "labels.txt". Entrégaselo a la persona\n
        que te pidió colaborar en la votación, o envíalo\n
        al correo jareciog@ucm.edu.es
        '''
        lbl = tk.Label(self, text=texto)
        lbl.place(x=0, y=10, width=self.w, height=200)
        lbl.config(font=('Arial', 10), justify=tk.LEFT)

        btn = tk.Button(self, text='SALIR', bd=5, command=lambda: exit(0))
        btn.place(x=100, y=300, width=150)
        btn.config(font=('Arial', 12), justify=tk.CENTER)


if __name__ == "__main__":
    sys.setrecursionlimit(2000) # Quick fix for recursion errors
    app = LabelerApp()
