from pico2d import *

class Exit:
    def __init__(self):
        self.image = load_image('Door.png')
        self.Open = True

    def draw(self):
        self.image.clip_draw(48 * self.Open , 0 , 48 , 48 , 850 , 170 + 24)