from model import ImageModel

class ImageController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.image = None

        self.view.btn_load.config(command=self.load_image)
        self.view.btn_process.config(command=self.process_image)

    def load_image(self):
        path = self.view.open_dialog()
        if path:
            self.image = self.model.load_image(path)
            self.view.show_image(self.image)

    def process_image(self):
        if self.image is None:
            return

        gray = self.model.to_grayscale(self.image)
        sobel = self.model.sobel_filter(gray)
        th = self.model.threshold(sobel, 100)

        self.view.show_image(th)
