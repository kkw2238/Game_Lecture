from pico2d import *
import Class_Key

class Exit:

    Clear_Sound = None

    def __init__(self):
        self.image = load_image('./Resource/Door.png')
        self.Open = True
        self.X = 850
        self.Y = 194

        if Exit.Clear_Sound == None :
            Exit.Clear_Sound = load_music("./Music/Clear.mp3")

    def draw(self):
        self.image.clip_draw(48 * self.Open , 0 , 48 , 48 , self.X , self.Y)

    def UPDATE(self , Key):
        if Key.Key_X <= self.X + 24 and Key.Key_X >= self.X - 24 :
            if Key.Key_Y <= self.Y + 24 and Key.Key_Y >= self.Y - 24 :
                self.Open = True
                Key.Open = True

    def Play_Clear_Sound(self):
        Exit.Clear_Sound.play(1)