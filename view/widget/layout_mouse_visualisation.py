from queue import LifoQueue

import numpy as np
from PIL import Image
from PySide6.QtCore import QSize
from PySide6.QtGui import QImage, QPixmap, QShortcut, QKeySequence, Qt, QIcon
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QHBoxLayout, QPushButton

from utils.environment import Environment


class LayoutMouseVisualisation(QWidget):
    def __init__(self, save_img_foo, parent=None):
        super().__init__(parent)
        self.controller = ControllerMouseVisualisation(self)
        self.main_layout = QHBoxLayout()
        self.setFixedSize(1041, 650)
        self.setStyleSheet("""
            QWidget {
                background-color: #A9B4BE;
            }
        """)
        self.setLayout(self.main_layout)
        self.image_label = QLabel()
        # noinspection PyUnresolvedReferences
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.update_img(self.controller.get_teeth_image())
        self.image_label.mousePressEvent = self.get_mouse_position
        self.main_layout.addWidget(self.image_label)

        self.btn_layout_widget = QWidget()
        self.btn_layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn_layout_widget.setMaximumWidth(80)
        self.btn_layout_widget.setMaximumHeight(629)
        self.btn_layout = QVBoxLayout()
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_layout.setSpacing(0)
        # noinspection PyUnresolvedReferences
        self.btn_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.btn_layout_widget.setLayout(self.btn_layout)
        self.btn_layout_widget.setObjectName("btn_layout_widget")
        self.btn_layout_widget.setStyleSheet("""
            #btn_layout_widget{
                background-color: #A9B4BE;
            }
        """)
        self.main_layout.addWidget(self.btn_layout_widget)

        self.save_btn = ButtonSave(save_img_foo)
        self.btn_layout.addWidget(self.save_btn)

        self.red_btn = ButtonColor([210, 4, 45], self.controller.set_color, self.btn_layout)
        self.btn_layout.addWidget(self.red_btn)

        self.black_btn = ButtonColor([27, 18, 18], self.controller.set_color, self.btn_layout)
        self.btn_layout.addWidget(self.black_btn)

        self.blue_btn = ButtonColor([137, 207, 240], self.controller.set_color, self.btn_layout)
        self.btn_layout.addWidget(self.blue_btn)

        self.purple_btn = ButtonColor([207, 159, 255], self.controller.set_color, self.btn_layout)
        self.btn_layout.addWidget(self.purple_btn)

        self.eraser_btn = ButtonColor([255, 255, 255], self.controller.set_color, self.btn_layout)
        self.eraser_btn.setIcon(QIcon('static/images/eraser.png'))
        self.eraser_btn.setIconSize(QSize(30, 30))
        self.btn_layout.addWidget(self.eraser_btn)

        self.undo_btn = ButtonUndo(self.set_previous_image)
        self.btn_layout.addWidget(self.undo_btn)

        self.red_btn.set_selected(True)

        self.undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.undo_shortcut.activated.connect(self.set_previous_image)

    def get_mouse_position(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        print(f"x: {x}, y: {y}")
        self.update_img(self.controller.color_teeth(x, y, self.controller.current_color))

    def set_previous_image(self):
        self.update_img(self.controller.get_previous_colored_image())

    def update_img(self, img):
        test = self.PIL_to_qimage(img)
        pixmap = QPixmap.fromImage(test)
        self.image_label.setPixmap(pixmap)

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
        self.previous_colored_image_queue = LifoQueue()
        self.current_color = [210, 4, 45]
        self.saved_image = None

    def color_teeth(self, x, y, color):
        teeth_mask_data = np.array(self.teeth_mask)
        colored_image_data = np.array(self.colored_image)
        target_color = teeth_mask_data[y, x]
        if np.array_equal(target_color, np.array([0, 0, 0, 0])):
            return self.colored_image
        if (target_color[0] == 20 and target_color[2] == 10) or (target_color[2] == 20):
            target_color[2] = target_color[0]
        # noinspection PyUnresolvedReferences
        mask = (teeth_mask_data == target_color).all(axis=-1)
        colored_image_data[mask] = color + [255]
        self.previous_colored_image_queue.put(self.colored_image.copy())
        self.colored_image = Image.fromarray(colored_image_data, "RGBA")
        return self.colored_image

    def set_color(self, color):
        self.current_color = color

    def get_previous_colored_image(self):
        if not self.previous_colored_image_queue.empty():
            self.colored_image = self.previous_colored_image_queue.get()
        return self.colored_image

    def get_teeth_image(self):
        return self.colored_image


class ButtonColor(QPushButton):
    def __init__(self, color: list, foo_to_set, parent_layout):
        super().__init__()
        self.color = color
        self.foo_to_set = foo_to_set
        self.parent_layout = parent_layout
        color_css = f"rgb({color[0]}, {color[1]}, {color[2]})"
        darker_hover_color = self.darken_rgb_color(color_css, 30)
        self.default_style = f"""
            QPushButton {{
                background-color: {color_css};
                border: 1px solid #b0b0b0;  
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
                margin: 5px;
            }}
            QPushButton:hover {{
                background-color: {darker_hover_color};
            }}
        """
        self.selected_style = f"""
            QPushButton {{
                background-color: {color_css};
                border: 3px solid #000000;  
                padding: 6px;  
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
                margin: 5px;
            }}
        """
        self.setStyleSheet(self.default_style)
        self.setFixedSize(50, 50)
        self.clicked.connect(self.on_click)

    @staticmethod
    def darken_rgb_color(rgb_string, percentage):
        rgb_values = rgb_string.strip('rgb()').split(',')
        r, g, b = int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2])

        if r == 27 and g == 18 and b == 18:
            return "rgb(50, 50, 50)"

        r = int(r * (1 - percentage / 100))
        g = int(g * (1 - percentage / 100))
        b = int(b * (1 - percentage / 100))

        r = max(0, min(r, 255))
        g = max(0, min(g, 255))
        b = max(0, min(b, 255))

        return f"rgb({r}, {g}, {b})"

    def set_selected(self, selected: bool):
        if selected:
            self.setStyleSheet(self.selected_style)
        else:
            self.setStyleSheet(self.default_style)

    def on_click(self):
        for i in range(self.parent_layout.count()):
            widget = self.parent_layout.itemAt(i).widget()
            if isinstance(widget, ButtonColor):
                widget.set_selected(widget is self)  # Select only this button
        self.foo_to_set(self.color)


class ButtonUndo(QPushButton):
    def __init__(self, foo):
        super().__init__()
        self.clicked.connect(foo)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon('static/images/undo.png'))
        self.setIconSize(QSize(30, 30))
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                border: 1px solid #b0b0b0;  
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #d0d0d0; 
            }
        """)


class ButtonSave(QPushButton):
    def __init__(self, foo):
        super().__init__()
        self.clicked.connect(foo)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon('static/images/save.png'))
        self.setIconSize(QSize(30, 30))
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                border: 1px solid #b0b0b0;  
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #d0d0d0; 
            }
        """)
