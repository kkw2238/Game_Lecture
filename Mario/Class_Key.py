from pico2d import *

import Class_Mario

class Key:
    image_Key = None

    def __init__(self):
        if Key.image_Key == None :
            Key.image_Key = load_image('./Resource/Key.png')

        self.Key_X = 0
        self.Key_Y = 0
        self.Open  = False

    def UPDATE(self, Mario):
        self.Key_X = Mario.X
        self.Key_Y = Mario.Y
        print("%d %d" , self.Key_X , self.Key_Y)

    def draw(self):
        if self.Open == False :
            self.image_Key.draw(self.Key_X ,self.Key_Y)

class Key_Dish:

    image_Keydish = None

    def __init__(self):
        if Key_Dish.image_Keydish == None:
            Key_Dish.image_Keydish = load_image('./Resource/Key_Dish.png')
        self.Key_Dish_X = 0
        self.Key_Dish_Y = 0

    def draw(self):
        self.image_Keydish.draw(self.Key_Dish_X, self.Key_Dish_Y)


