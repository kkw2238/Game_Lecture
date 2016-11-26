from pico2d import *

import Class_Mario
import Class_Back_Ground
import Class_Exit
import Class_Key
import Stage2

mario       = None
Marios      = None
back_ground = None
exits       = None
Key         = None
Key_Dish    = None

def JUMP(Mario):
    global Marios

    down = 0
    Jerge_down = False
    if Mario.Y >= 244:
        for MARIO in Marios:
            if (Mario.X < MARIO.X + 26 and Mario.X > MARIO.X - 26) :
                    if Mario.Y - 26 > MARIO.Y + 26:
                        down += 1
                    if Mario.Y + 26 <= MARIO.Y - 26:
                        down += 1
                    else:
                        Jerge_down = True

            else :
                down += 1

        if (down , Mario.Jump) == (5 , Mario.Jump_None):
            Mario.Jump = Mario.Jump_Down
            Mario.Jump_State = 1
            Mario.State = 3

    if Mario.Jump == Mario.Jump_Up:
        if Mario.Jump_State == 0 :
            Mario.Jump = Mario.Jump_Down
        Mario.Y = Mario.Y + Mario.Jump_State ** 2
        Mario.Jump_State += 1

    if Mario.Jump == Mario.Jump_Down:
        Mario.Y = Mario.Y - Mario.Jump_State ** 2
        if Mario.Jump_State < 5 :
            Mario.Jump_State += 1

    if Mario.Y < 194 :
        Mario.Y = 194
        Mario.Jump = Mario.Jump_None
        Mario.Jump_State = 0
        if Mario.Move == True :
            Mario.State = 1
        else :
            Mario.State = 0

def DRAW():
    global exits , back_ground , Marios , Key , Key_Dish
    back_ground.draw()
    exits.draw()

    for Mario in Marios:
        Mario.draw()

    Key.draw()
    Key_Dish.draw()

    update_canvas()

def handle_events():
    global running
    global Marios
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
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
            Create_Stage()

        else :
            for mario in Marios :
                mario.Handle_Event(event)

##
def UPDATE():
    global Marios , Key , exits

    for Mario in Marios :
        if Mario.Select == True :
            Mario.update()
            JUMP(Mario)

    for Mario in Marios :
        if Mario.Select == False :
            Mario.update()
            JUMP(Mario)

    EXIT_Mario = 0
    for Mario in Marios :
        if Mario.Select == True :
            Class_Mario.Block(Mario, Marios)
            Mario.Key_Collision(exits)
            if(Mario.Grab == True) :
                Key.UPDATE(Mario)
                exits.UPDATE(Key)

            if Mario.Exit == True :
                EXIT_Mario += 1

    for Mario in Marios:
        if Mario.Select == False:
            Class_Mario.Block(Mario, Marios)
            Mario.Key_Collision(exits)
            if (Mario.Grab == True):
                Key.UPDATE(Mario)
                exits.UPDATE(Key)

            if Mario.Exit == True:
                EXIT_Mario += 1

    if EXIT_Mario == 6 :
        Stage2.Create_Stage()

def exit():
    global mario, Marios, back_ground, exits , Key , Key_Dish
    del(Marios)
    del(back_ground)
    del(exits)
    del(Key)
    del(Key_Dish)
    close_canvas()


def Create_Stage():
    global mario, Marios, back_ground, exits , running , Key , Key_Dish

    Marios = Class_Mario.Create_Marios()
    exits = Class_Exit.Exit()
    back_ground = Class_Back_Ground.Back_Ground()

    Key = Class_Key.Key()
    Key_Dish = Class_Key.Key_Dish()

    exits.X = 850
    exits.Y = 194

    Key.Key_X = 481
    Key.Key_Y = 195
    Key_Dish.Key_Dish_X = 481
    Key_Dish.Key_Dish_Y = 175

    running = True

    exits.Open = False

    Stage1()

def Stage1() :
    global running
    while(running):
        handle_events()
        UPDATE()
        DRAW()
        delay(0.02)

    close_canvas()

if __name__ == '__Stage1__':
    Stage1()