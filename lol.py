import tkinter as tk
from PIL import ImageTk, Image
import os

from settings import IMG_FOLDER, IG_FOLDER, LIME_FOLDER, XRAI_FOLDER, ANCHOR_FOLDER

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
                if self.count <= len(self.img_names):
                    kwargs = {
                        'image_name': self.img_names[self.count],
                        'image_number': self.count + 1,
                        'no_of_images': len(self.img_names)
                    }
                    self.count += 1
                else:
                    # self.saveImages()
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


class WelcomeWindow(tk.Tk):
    w, h = 600, 400

    def __init__(self, app):
        # Prev. configurations
        super().__init__()
        # Window options
        self.title('Proyecto XAI-UCM: Votación de Imágenes')
        self.geometry(f'{self.w}x{self.h}')
        # Windows text
        title = tk.Label(self, text='VOTACIÓN DE IMÁGENES. PROYECTO XAI-UCM')
        title.place(x=0, y=30, width=self.w)
        title.config(font=('Helvetica', 18, 'bold'), justify=tk.CENTER)
        inst = tk.Label(self, text='Presione "Iniciar" o "Leer Instrucciones"')
        inst.place(x=0, y=70, width=self.w)
        inst.config(font=('Helvetica', 14), justify=tk.CENTER)
        # Buttons
        btn1 = tk.Button(self, text='Iniciar', bd=5, command=app.switch_window(ImageViewerWindow))
        btn1.place(x=270, y=150)
        btn1.config(font=('Helvetica', 12))
        btn2 = tk.Button(self, text=f'Leer instrucciones', bd=5, command=app.switch_window(InstructionsWindow))
        btn2.place(x=230, y=200)
        btn2.config(font=('Helvetica', 12))


class ImageViewerWindow(tk.Tk):
    w, h = 600, 400

    def __init__(self, app, image_name, image_number, no_of_images):
        # Prev. configurations
        super().__init__()
        self.geometry(f'{self.w}x{self.h}')
        self.title(f'Imagen {image_number}/{no_of_images}')
        # Main img and instructions
        main_img, img1, img2, img3, img4 = self.load_images_widgets('Giant_Panda_2.jpeg')
        main_lbl = tk.Label(self, imag=main_img)
        main_lbl.place(x=350, y=10, width=300, height=300)
        text = tk.Label(self, text='¿Cuál de las imágenes de abajo explica de mejor manera la imagen de arriba? Presiona el botón debajo de la imagen de tu elección')
        text.place(x=0, y=320, width=self.w)
        text.config(font=('Helvetica', 12, 'bold'), justify=tk.CENTER)
        # Images
        lbl1 = tk.Label(self, image=img1)
        lbl1.place(x=50, y=400, width=200, height=200)
        lbl2 = tk.Label(self, image=img2)
        lbl2.place(x=300, y=400, width=200, height=200)
        lbl3 = tk.Label(self, image=img3)
        lbl3.place(x=550, y=400, width=200, height=200)
        lbl3 = tk.Label(self, image=img3)
        lbl3.place(x=800, y=400, width=200, height=200)
        # Buttons
        btn1 = tk.Button(self, text='IG', bd=5)
        btn1.place(x=50, y=620)
        btn1.config(font=('Helvetica', 10))
        btn2 = tk.Button(self, text='LIME', bd=5)
        btn2.place(x=150, y=620)
        btn2.config(font=('Helvetica', 10))
        btn3 = tk.Button(self, text='XRAI', bd=5)
        btn3.place(x=300, y=620)
        btn3.config(font=('Helvetica', 10))
        btn4 = tk.Button(self, text='ANCHOR', bd=5)
        btn4.place(x=450, y=620)
        btn4.config(font=('Helvetica', 10))

    def load_images_widgets(self, img_name):
        img_name_png = f'{get_name_without_ext(img_name)}.png'
        main_img = ImageTk.PhotoImage(Image.open(os.path.join(IMG_FOLDER, img_name)).resize((300, 300)))
        img1 = ImageTk.PhotoImage(Image.open(os.path.join(IG_FOLDER, img_name_png)).resize((200, 200)))
        img2 = ImageTk.PhotoImage(Image.open(os.path.join(LIME_FOLDER, img_name_png)).resize((200, 200)))
        img3 = ImageTk.PhotoImage(Image.open(os.path.join(ANCHOR_FOLDER, img_name_png)).resize((200, 200)))
        img4 = ImageTk.PhotoImage(Image.open(os.path.join(ANCHOR_FOLDER, img_name_png)).resize((200, 200)))
        return main_img, img1, img2, img3, img4


class InstructionsWindow(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.geometry('200x200')


class ThankYouWindow(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.geometry('100x100')


if __name__ == "__main__":
    app = LabelerApp()
