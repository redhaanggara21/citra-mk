import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class ImageView:

    def __init__(self, root):
        self.root = root
        self.root.title("MVC Image Processing")

        self.btn_load = tk.Button(root, text="Input Image")
        self.btn_process = tk.Button(root, text="Process Sobel")

        self.btn_load.pack()
        self.btn_process.pack()

        self.panel = tk.Label(root)
        self.panel.pack()

    def show_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if len(img.shape)==3 else img
        im = Image.fromarray(img_rgb)
        imgtk = ImageTk.PhotoImage(im)
        self.panel.imgtk = imgtk
        self.panel.config(image=imgtk)

    def open_dialog(self):
        return filedialog.askopenfilename()
