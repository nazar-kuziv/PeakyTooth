import numpy as np
from PIL import Image
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

from utils.environment import Environment


class LayoutMouseVisualisation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = ControllerMouseVisualisation(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.image_label = QLabel()
        # noinspection PyUnresolvedReferences
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.update_img(self.controller.get_teeth_image())
        self.image_label.mousePressEvent = self.get_mouse_position
        self.layout.addWidget(self.image_label)

    def update_img(self, img):
        test = self.PIL_to_qimage(img)
        pixmap = QPixmap.fromImage(test)
        self.image_label.setPixmap(pixmap)

    def get_mouse_position(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        print(f"x: {x}, y: {y}")
        self.update_img(self.controller.color_teeth(x, y, [255, 0, 0]))

    @staticmethod
    def PIL_to_qimage(pil_img):
        temp = pil_img.convert('RGBA')
        return QImage(
            temp.tobytes('raw', "RGBA"),
            temp.size[0],
            temp.size[1],
            QImage.Format.Format_RGBA8888
        )


class ControllerMouseVisualisation:
    def __init__(self, view):
        self.view = view
        self.teeth_image = Image.open(Environment.resource_path("static/images/teeth.png")).convert("RGBA")
        self.teeth_mask = Image.open(Environment.resource_path("static/images/teeth_mask.png")).convert("RGBA")
        self.colored_image = self.teeth_image.copy()

    def color_teeth(self, x, y, color):
        teeth_mask_data = np.array(self.teeth_mask)
        colored_image_data = np.array(self.colored_image)
        target_color = teeth_mask_data[y, x]
        print(target_color)
        if np.array_equal(target_color, np.array([0, 0, 0, 0])):
            return self.colored_image
        if (target_color[0] == 20 and target_color[2] == 10) or (target_color[2] == 20):
            target_color[2] = target_color[0]
        # noinspection PyUnresolvedReferences
        mask = (teeth_mask_data == target_color).all(axis=-1)
        colored_image_data[mask] = color + [255]
        self.colored_image = Image.fromarray(colored_image_data, "RGBA")
        return self.colored_image

    def get_teeth_image(self):
        return self.colored_image
