from pico2d import *

import Class_Mario
import Class_Back_Ground
import Class_Exit
import Stage1


import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"

else :
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

#
mario       = None
Marios      = None
press_start = None
back_ground = None
exits       = None
logo        = None

class Press_Start:
    def __init__(self):
        self.Press_C = load_image('Press_C_Start.png')
        self.Print = False
        self.Count = 0

    def draw(self):
        if self.Print :
            self.Press_C.draw(481,300)

    def update(self) :
        if self.Print == False :
            self.Count += 1
            if self.Count == 15 :
                self.Print = True
                self.Count = 0

        elif self.Print == True :
            self.Count += 1
            if self.Count == 15:
                self.Print = False
                self.Count = 0

class Logo:
    def __init__(self):
        self.image_logo = load_image('Main_Rogo.png')

    def draw(self):
        self.image_logo.draw(481,530)


def UPDATE():
    global press_start , Marios
    Exit_Mario = 0
    press_start.update()

    for Mario in Marios :
        JUMP(Mario)
        Mario.update()
        Class_Mario.Block(Mario, Marios)
        Mario.Key_Collision(exits)
        if Mario.Exit == True :
            Exit_Mario += 1

    if Exit_Mario == 6 :
        exit()
        Stage1.Create_Stage()


#
def DRAW():
    global exits , press_start , back_ground , Marios , logo
    back_ground.draw()
    press_start.draw()
    exits.draw()
    for Mario in Marios:
        Mario.draw()
    logo.draw()
    update_canvas()

def JUMP(Mario):
    global Marios

    down = 0
    Jerge_down = False
    if Mario.Y >= 244:
        for MARIO in Marios:
            if (Mario.X < MARIO.X + 26 and Mario.X > MARIO.X - 26):
                if Mario.Y - 26 > MARIO.Y + 26:
                    down += 1
                if Mario.Y + 26 <= MARIO.Y - 26:
                    down += 1
                else:
                    Jerge_down = True

            else:
                down += 1

        if (down, Mario.Jump) == (5, Mario.Jump_None):
            Mario.Jump = Mario.Jump_Down
            Mario.Jump_State = 1
            Mario.State = 3

    if Mario.Jump == Mario.Jump_Up:
        if Mario.Jump_State == 0:
            Mario.Jump = Mario.Jump_Down
        Mario.Y = Mario.Y + Mario.Jump_State ** 2
        Mario.Jump_State += 1

    if Mario.Jump == Mario.Jump_Down:
        Mario.Y = Mario.Y - Mario.Jump_State ** 2
        if Mario.Jump_State < 5:
            Mario.Jump_State += 1

    if Mario.Y < 194:
        Mario.Y = 194
        Mario.Jump = Mario.Jump_None
        Mario.Jump_State = 0
        if Mario.Move == True:
            Mario.State = 1
        else:
            Mario.State = 0


def handle_events():
    global running
    global Marios
    global Key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            exit()
            Stage1.Create_Stage()

        else :
            for mario in Marios :
                mario.Handle_Event(event)

def exit():
    global press_start, exits, logo
    del(press_start)
    del(logo)
    del(exits)

def main() :

    open_canvas(962,700)


    global mario , Marios , press_start , back_ground , exits , logo , running

    running = True
    Marios = Class_Mario.Create_Marios()
    exits = Class_Exit.Exit()
    press_start = Press_Start()
    back_ground = Class_Back_Ground.Back_Ground()
    logo = Logo()

    while(running):
        UPDATE()
        DRAW()
        handle_events()
        delay(0.02)

    close_canvas()

if __name__ == '__main__':
    main()