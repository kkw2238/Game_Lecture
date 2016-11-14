from pico2d import *
import Class_Key

class Exit:
    def __init__(self):
        self.image = load_image('Door.png')
        self.Open = True
        self.X = 850
        self.Y = 194

    def draw(self):
        self.image.clip_draw(48 * self.Open , 0 , 48 , 48 , self.X , self.Y)

    def UPDATE(self , Key):
        if Key.Key_X <= self.X + 24 and Key.Key_X >= self.X - 24 :
            if Key.Key_Y <= self.Y + 24 and Key.Key_Y >= self.Y - 24 :
                self.Open = True
                Key.Open = True