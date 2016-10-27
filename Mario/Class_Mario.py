from pico2d import *

class Mario:

    image_Mario = None
    image_Number = None
    Jump_None = 0
    Jump_Up = 1
    Jump_Down = 2
    Left = 1
    Right = 0

    def __init__(self):
        if Mario.image_Mario == None :
            Mario.image_Mario = load_image('Mario_Null.png')
        if Mario.image_Number == None :
            Mario.image_Number = load_image('Number_40.png')
        self.Num = 0
        self.X = 0
        self.Y = 194
        self.State = 0
        self.Select = False
        self.Move = False
        self.Speed = 0
        self.Exit = False
        self.Jump = Mario.Jump_None
        self.Jump_State = 0
        self.Down = 0
        self.Where = Mario.Right

    def draw(self):
        self.image_Mario.clip_draw(52 * self.State , 50 * self.Where , 52  , 50 , self.X ,self.Y)
        self.image_Number.clip_draw(20 * (self.Num - 1) , 0 , 20 , 18 , self.X , self.Y + 34)
    def update(self):
        if self.Move :
            self.X += self.Speed
     ##     if s##elf.X > 936 :
     ##         self.X = 936
     ##     elif self.X < 26 :
     ##         self.X = 26

     ##     if self.State == 1 :
     ##         self.State = 2
     ##     elif self.State == 2 :
     ##         self.State = 1
