from pico2d import *

class Back_Ground:
    def __init__(self):
        self.image_Bottom = load_image('Bottom_962.png')
        self.image_BackGround = load_image('BackGround_Sky.png')

    def draw(self):
        self.image_BackGround.clip_draw(0,0,962,530,481,435)
        self.image_Bottom.clip_draw(0,0,962,169,481,85)