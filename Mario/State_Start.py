from pico2d import *

import Collision
import FrameWork
import Class_Mario
import Class_Back_Ground
import Class_Exit
import Stage1

mario       = None
Marios      = None
press_start = None
back_ground = None
exits       = None
logo        = None

class Press_Start:

    def __init__(self):
        self.Press_C = load_image('./Resource/Press_C_Start.png')
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
        self.image_logo = load_image('./Resource/Main_Rogo.png')

    def draw(self):
        self.image_logo.draw(481,530)

def ENTER():

    global mario, Marios, press_start, back_ground, exits, logo, running

    running = True
    Marios = Class_Mario.Create_Marios()
    exits = Class_Exit.Exit()
    press_start = Press_Start()
    back_ground = Class_Back_Ground.Back_Ground()
    logo = Logo()
    back_ground.Play_BGM()

def UPDATE(frame_time):
    global press_start , Marios , back_ground , exits
    Exit_Mario = 0
    press_start.update()

    for Mario in Marios :
        Mario.update(frame_time,Marios)
        Mario.Key_Collision(exits)
        if Mario.Exit == True :
            Exit_Mario += 1

    if Exit_Mario == 6 :
        back_ground.Stop_BGM()
        exits.Play_Clear_Sound()
        delay(3)
        FrameWork.push_state(Stage1)

def DRAW(frame_time):
    global exits , press_start , back_ground , Marios , logo
    back_ground.draw()
    press_start.draw()
    exits.draw()
    for Mario in Marios:
        Mario.draw()
    logo.draw()
    update_canvas()

def handle_events(frame_time):
    global running
    global Marios
    global Key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            Press_C = load_wav("./Music/Press_C_Sound.wav")
            Press_C.play()
            delay(1)
            del(Press_C)
            FrameWork.push_state(Stage1)

        else :
            for mario in Marios :
                mario.Handle_Event(event)

def exit():
    global press_start, exits, logo
    del(press_start)
    del(logo)
    del(exits)

