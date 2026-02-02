import tkinter as tk
from model import ImageModel
from view import ImageView
from controller import ImageController

root = tk.Tk()

model = ImageModel()
view = ImageView(root)
controller = ImageController(model, view)

root.mainloop()
