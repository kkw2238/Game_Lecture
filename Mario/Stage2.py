from pico2d import *

import Collision
import FrameWork
import Class_Mario
import Class_Back_Ground
import Class_Exit
import Class_Key

mario       = None
Marios      = None
back_ground = None
exits       = None
Key         = None
Key_Dish    = None

def DRAW(frame_time):
    global exits , back_ground , Marios , Key , Key_Dish
    back_ground.draw()
    exits.draw()

    for Mario in Marios:
        Mario.draw()

    Key.draw()
    Key_Dish.draw()

    update_canvas()

def handle_events(frame_time):
    global running
    global Marios
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_m):
            for Mario in Marios:
                if Mario.X <= Key.Key_X + 15 and Mario.X >= Key.Key_X - 15:
                    if Mario.Y <= Key.Key_Y + 15 and Mario.Y >= Key.Key_Y - 15:
                        Mario.Grab = True

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_m):
            for Mario in Marios:
                if Mario.Grab == True:
                    Mario.Grab = False

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_v):
            ENTER()

        else :
            for mario in Marios :
                mario.Handle_Event(event)


def UPDATE(frame_time):
    global Marios, Key, exits
    Exit_Mario = 0

    for Mario in Marios:
        Mario.update(frame_time, Marios)
        Collision.Block(Mario, Marios)
        Mario.Key_Collision(exits)
        if Mario.Exit == True:
            Exit_Mario += 1

        if (Mario.Grab == True):
            Key.UPDATE(Mario)
            exits.UPDATE(Key)

    if Exit_Mario == 6:
        back_ground.Stop_BGM()
        exits.Play_Clear_Sound()
        delay(3)


def exit():
    global mario, Marios, back_ground, exits , Key , Key_Dish
    del(Marios)
    del(back_ground)
    del(exits)
    del(Key)
    del(Key_Dish)
    close_canvas()

def ENTER():
    global mario, Marios, back_ground, exits , running , Key , Key_Dish

    Marios = Class_Mario.Create_Marios()
    exits = Class_Exit.Exit()
    back_ground = Class_Back_Ground.Back_Ground()

    Key = Class_Key.Key()
    Key_Dish = Class_Key.Key_Dish()

    exits.X = 850
    exits.Y = 194

    Key.Key_X = 481
    Key.Key_Y = 600
    Key_Dish.Key_Dish_X = 481
    Key_Dish.Key_Dish_Y = 580

    exits.Open = False