from pico2d import *
import Collision
import json

class Mario:
    PIXEL_PER_METER = (3.0 / 0.3)

    RUN_SPEED_KMPH = 80.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    image_Mario = None
    image_Number = None
    Jump_None , Jump_Up , Jump_Down = 0 , 1 , 2
    Run_Right , Run_Left = 1 , -1
    Right, Left = 0, 1

    Jump_Sound = None

    def __init__(self):
        if Mario.image_Mario == None :
            Mario.image_Mario = load_image('./Resource/Mario_Null.png')
        if Mario.image_Number == None :
            Mario.image_Number = load_image('./Resource/Number_40.png')
        if Mario.Jump_Sound == None :
            Mario.Jump_Sound = load_wav('./Music/Jump.wav')
            Mario.Jump_Sound.set_volume(30)

        self.Num = 0
        self.X = 0
        self.Y = 194
        self.Grab = False
        self.State = 0
        self.Select = False
        self.Move = False
        self.Move_State = Mario.Run_Right
        self.Exit = False
        self.Jump = Mario.Jump_None
        self.Jump_State = 0
        self.Name = 'noname'
        self.Where = Mario.Right

    def Play_Jump_Sound(self):
        Mario.Jump_Sound.play(1)

    def draw(self):
        self.image_Mario.clip_draw(52 * self.State , 50 * self.Where , 52  , 50 , self.X ,self.Y)
        self.image_Number.clip_draw(20 * (self.Num - 1) , 0 , 20 , 18 , self.X , self.Y + 34)

    def update(self,frame_time,marios):

        if self.Select :

            distance = self.Move_State * Mario.RUN_SPEED_PPS * frame_time

            self.JUMP(marios, frame_time)
            Collision.Air_BLOCK(self, marios)

            if (self.Move , self.Jump) == (True , self.Jump_None) :

                self.X = max( 26 , self.X + distance )
                self.X = min( 938 , self.X )
                self.State = self.State % 2 + 1

                Collision.Block(self,marios)

            elif self.Move == True and self.Jump != Mario.Jump_None :

                self.X = max(26, self.X + distance)
                self.X = min(938, self.X)

                Collision.Block(self, marios)


            if self.Jump != self.Jump_None :
                self.State = 3

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
                        self.Move_State = Mario.Run_Right
                        self.Where = self.Right

                        if self.Jump == self.Jump_None:
                            self.State = 1
                        self.Move = True

            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                    if self.Select:
                        if self.Jump == self.Jump_None:
                            self.State = 0
                        self.Move = False

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                    if self.Select:
                        self.Move_State = Mario.Run_Left
                        self.Where = self.Left

                        if self.Jump == self.Jump_None:
                            self.State = 1
                        self.Move = True

            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                if self.Select:

                    if self.Jump == self.Jump_None:
                        self.State = 0
                    self.Move = False

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if self.Select:
                    if self.Jump == 0:
                        self.Jump = self.Jump_Up
                        self.Jump_State = - 30
                        self.State = 3
                        self.Play_Jump_Sound()

    def Key_Collision(self, Exit):

        if Exit.Open == True and self.Exit == False:

            if self.X <= Exit.X + 24 and self.X >= Exit.X - 24:

                if self.Y <= Exit.Y + 24 and self.Y >= Exit.Y - 24:
                    self.Exit = True

                    self.Select = False

                    self.X = 10000

    def JUMP(self,Marios,frame_time):
        down = 0
        distance = Mario.RUN_SPEED_PPS * frame_time
        Size_X, Size_Y = 52, 50
        Half_X, Half_Y = Size_X / 2 , Size_Y / 2
        if self.Y >= 244:
            for MARIO in Marios:
                if MARIO.Num != self.Num :
                    if (self.X < MARIO.X + Half_X and self.X > MARIO.X - Half_X):
                        if self.Y > MARIO.Y + Size_Y:
                            down += 1
                        if self.Y < MARIO.Y :
                            down += 1
                    else:
                        down += 1

            print(down, self.Jump ,self.Num)

            if down == 5 and self.Jump == self.Jump_None:
                self.Jump = self.Jump_Down
                self.Jump_State = 1
                self.State = 3

        if self.Jump == self.Jump_Up:
            if self.Jump_State == 0:
                self.Jump = self.Jump_Down
            self.Y += distance
            self.Jump_State += 1

        if self.Jump == self.Jump_Down:
            self.Y -= distance
            if self.Jump_State < 5:
                self.Jump_State += 1

        if self.Y < 194:
            self.Y = 194
            self.Jump = self.Jump_None
            self.Jump_State = 0
            if self.Move == True:
                self.State = 1
            else:
                self.State = 0

def KEYPAD(mario):
    if (mario.Select , mario.Exit) == (False , False):
        mario.Select = True
        mario.image_Mario = load_image('./Resource/Mario.png')

    elif mario.Select == True:
         mario.image_Mario = load_image('./Resource/Mario_Null.png')
         mario.Select = False
         mario.Speed = 0
         mario.State = 0
         mario.Where = mario.Right
         mario.Move = False

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