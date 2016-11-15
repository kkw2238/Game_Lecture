from pico2d import *
import json
import Class_Exit

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
        self.Grab = False
        self.Exit = False
        self.Jump = Mario.Jump_None
        self.Jump_State = 0
        self.Name = 'noname'
        self.Where = Mario.Right

    def draw(self):
        if self.Exit == False :
            if self.Select == False :
                self.image_Mario.clip_draw(0 , 50 * self.Where , 52, 50, self.X, self.Y)
                self.image_Number.clip_draw(20 * (self.Num - 1), 0, 20, 18, self.X, self.Y + 34)
            else :
                self.image_Mario.clip_draw(52 * self.State , 50 * self.Where , 52  , 50 , self.X ,self.Y)
                self.image_Number.clip_draw(20 * (self.Num - 1) , 0 , 20 , 18 , self.X , self.Y + 34)

    def update(self):

        if self.Select :
            if (self.Move , self.Jump) == (True , self.Jump_None) :
                self.X = max( 26 , self.X + self.Speed )
                self.X = min( 938 , self.X )
                self.State = self.State % 2 + 1
            elif self.Move == True :

                self.X = max(26, self.X + self.Speed)
                self.X = min(938, self.X)

            if self.Jump != self.Jump_None :
                self.State = 3

    def Key_Collision(self , Exit):
        if Exit.Open == True and self.Exit == False:
            if self.X <= Exit.X + 24 and self.X >= Exit.X - 24 :
                if self.Y <= Exit.Y + 24 and self.Y >= Exit.Y - 24 :
                    self.Exit = True
                    self.Select = False
                    self.X = 6974


    def Handle_Event(self, event):
            if   (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_1):
                    if self.Num == 1 :
                        KEYPAD(self)

            if   (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_2):
                    if self.Num == 2 :
                        KEYPAD(self)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_3):
                    if self.Num == 3 :
                        KEYPAD(self)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_4):
                    if self.Num == 4 :
                        KEYPAD(self)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_5):
                    if self.Num == 5 :
                        KEYPAD(self)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_6):
                    if self.Num == 6 :
                        KEYPAD(self)

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                    if self.Select:
                        self.Speed = 10
                        self.Where = self.Right

                        if self.Jump == self.Jump_None:
                            self.State = 1
                        self.Move = True

            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                    if self.Select:
                        self.Speed = 0

                        if self.Jump == self.Jump_None:
                            self.State = 0
                        self.Move = False

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                    if self.Select:
                        self.Speed = -10
                        self.Where = self.Left

                        if self.Jump == self.Jump_None:
                            self.State = 1
                        self.Move = True

            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                if self.Select:
                    self.Speed = 0

                    if self.Jump == self.Jump_None:
                        self.State = 0
                    self.Move = False

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if self.Select:
                    if self.Jump == 0:
                        self.Jump = self.Jump_Up
                        self.Jump_State = -6
                        self.State = 3


def KEYPAD(mario):
    if mario.Select == False:
        mario.Select = True
        mario.image_Mario = load_image('Mario.png')

    elif mario.Select == True:
         mario.image_Mario = load_image('Mario_Null.png')
         mario.Select = False
         mario.Speed = 0
         mario.State = 0
         mario.Where = mario.Right
         mario.Move = False


def Block(MARIO , Marios):
    for mario in Marios:

        if MARIO.Num != mario.Num:
            if MARIO.X < mario.X + 26 and MARIO.X > mario.X - 26:

                if MARIO.Y -26 <= mario.Y + 26 and MARIO.Y -26 >= mario.Y - 26 and MARIO.Jump == MARIO.Jump_Down:

                    MARIO.Y = mario.Y + 52

                    MARIO.Jump = MARIO.Jump_None

                    MARIO.Jump_State = 0

                    if MARIO.Move == True:
                        MARIO.State = 1

                    else:
                        MARIO.State = 0

                if MARIO.Y -26 <= mario.Y + 26 and MARIO.Y -26 >= mario.Y - 26 and MARIO.Jump == MARIO.Jump_Down:

                    MARIO.Y = mario.Y + 52

                    MARIO.Jump = MARIO.Jump_None

                    MARIO.Jump_State = 0

                    if MARIO.Move == True:

                        MARIO.State = 1

                    else:

                        MARIO.State = 0

            if MARIO.X + 26 > mario.X - 26 and MARIO.X + 26 < mario.X + 26:

                if MARIO.Y == mario.Y:

                    MARIO.X = mario.X - 52



                if MARIO.Y - 26 <= mario.Y + 26 and MARIO.Y - 26 >= mario.Y - 26 and MARIO.Jump == MARIO.Jump_Down:

                    MARIO.Y = mario.Y + 52

                    MARIO.Jump = MARIO.Jump_None

                    MARIO.Jump_State = 0

                    if MARIO.Move:

                        MARIO.State = 1

                    else:

                        MARIO.State = 0


                if MARIO.Y + 26 < mario.Y + 26 and MARIO.Y + 26 > mario.Y - 26 and MARIO.Jump == MARIO.Jump_Up:

                    MARIO.Y = mario.Y - 52

                    MARIO.Jump = MARIO.Jump_Down

                    MARIO.Jump_State = 0


                if MARIO.Y + 26 < mario.Y + 26 and MARIO.Y + 26 > mario.Y - 26 and MARIO.Jump == MARIO.Jump_Up:

                    MARIO.Y = mario.Y - 52

                    MARIO.Jump = MARIO.Jump_Down

                    if MARIO.Move == True:

                        MARIO.State = 1

                    else:

                        MARIO.State = 0

            if MARIO.X - 26 < mario.X + 26 and MARIO.X - 26 > mario.X - 26:

                if MARIO.Y == mario.Y:

                    MARIO.X = mario.X + 52



                if MARIO.Y - 26 <= mario.Y + 26 and MARIO.Y - 26 >= mario.Y - 26 and MARIO.Jump == MARIO.Jump_Down:

                    MARIO.Y = mario.Y + 52

                    MARIO.Jump = MARIO.Jump_None

                    MARIO.Jump_State = 0

                    if MARIO.Move == True:
                        MARIO.State = 1

                    else:
                        MARIO.State = 0



                if MARIO.Y + 26 < mario.Y + 26 and MARIO.Y + 26 > mario.Y - 26 and MARIO.Jump == MARIO.Jump_Up:

                    MARIO.Y = mario.Y - 52

                    MARIO.Jump = MARIO.Jump_Down

                    if MARIO.Move == True:

                        MARIO.State = 1

                    else:

                        MARIO.State = 0




def Create_Marios():
    Mario_Data_File = open("Mario_State.txt","r")
    Mario_Data = json.load(Mario_Data_File)
    Mario_Data_File.close()
    Marios = []
    for Name in Mario_Data :
        mario = Mario()
        mario.Name = Name
        mario.Num = Mario_Data[Name]['Num']
        mario.X = Mario_Data[Name]['X']
        mario.Y = Mario_Data[Name]['Y']
        Marios.append(mario)
    return Marios