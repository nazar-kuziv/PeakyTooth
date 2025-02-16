import io
from queue import LifoQueue

import numpy as np
from PIL import Image

from utils.environment import Environment


class ControllerMouthVisualisation:
    def __init__(self, view, previous_img=None):
        self.view = view
        self.teeth_mask = Image.open(Environment.resource_path("static/images/teeth_mask.png")).convert("RGBA")
        try:
            self.teeth_image = Image.open(io.BytesIO(previous_img)).convert("RGBA")
        except Exception:
            self.teeth_image = Image.open(Environment.resource_path("static/images/teeth.png")).convert("RGBA")
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

    def get_img_bytes(self):
        img_byte_arr = io.BytesIO()
        self.colored_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return img_byte_arr.getvalue()