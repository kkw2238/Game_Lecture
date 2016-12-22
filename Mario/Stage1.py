from pico2d import *

import Collision
import FrameWork
import Class_Mario
import Class_Back_Ground
import Class_Exit
import Class_Key
import Stage2
import time

mario       = None
Marios      = None
back_ground = None
exits       = None
Key         = None
Key_Dish    = None
MAX_Timer   = 300
Start_Time  = 0
Pass_Time   = 0
Font        = None

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

def DRAW(frame_time):
    global exits , back_ground , Marios , Key , Key_Dish
    back_ground.draw()
    exits.draw()

    for Mario in Marios:
        Mario.draw()

    Key.draw()
    Key_Dish.draw()

    TIME()

    update_canvas()

def handle_events(frame_time):
    global running
    global Marios
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            for Mario in Marios:
                if Mario.X <= Key.Key_X + 15 and Mario.X >= Key.Key_X - 15:
                    if Mario.Y <= Key.Key_Y + 15 and Mario.Y >= Key.Key_Y - 15:
                        Mario.Grab = True

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_x):
            for Mario in Marios:
                if Mario.Grab == True:
                    Mario.Grab = False

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_v):
            ENTER()

        else :
            for mario in Marios :
                mario.Handle_Event(event)

def UPDATE(frame_time):
    global Marios , Key , exits
    Exit_Mario = 0

    for Mario in Marios :
        Mario.update(frame_time,Marios)
        Mario.Key_Collision(exits)

        if Mario.Exit == True :
            Exit_Mario += 1

        if (Mario.Grab == True):
            Key.UPDATE(Mario)
            exits.UPDATE(Key)

    if Exit_Mario == 6 :
        back_ground.Stop_BGM()
        exits.Play_Clear_Sound()
        delay(3)
        FrameWork.push_state(Stage2)

def exit():
    global mario, Marios, back_ground, exits , Key , Key_Dish
    del(Marios)
    del(back_ground)
    del(exits)
    del(Key)
    del(Key_Dish)
    close_canvas()

def Game_Over():
    Game_Over = load_image('./Resource/GameOver.png')
    Game_Over.clip_draw(0, 0, 962, 530, 481, 265)
    Font.draw(300, 265, 'Game Over', (255, 255, 255))
    Game_Over_Sound = load_music('./Music/Game_Over_Sound.mp3')
    Game_Over_Sound.play(1)
    delay(7)
    FrameWork.push_state(State_Start)

def ENTER():
    global mario, Marios, back_ground, exits, running, Key, Key_Dish , Start_Time , Pass_Time , Font

    POSITION_KEY_X , POSITION_KEY_Y = 481 , 195
    POSITION_EXIT_X , POSITION_EXIT_Y = 850 , 194

    Marios = Class_Mario.Create_Marios()
    exits = Class_Exit.Exit()
    back_ground = Class_Back_Ground.Back_Ground()

    Key = Class_Key.Key()
    Key_Dish = Class_Key.Key_Dish()

    exits.X = POSITION_EXIT_X
    exits.Y = POSITION_EXIT_Y

    Key.Key_X = POSITION_KEY_X
    Key.Key_Y = POSITION_KEY_Y
    Key_Dish.Key_Dish_X = POSITION_KEY_X
    Key_Dish.Key_Dish_Y = POSITION_KEY_Y - 20

    running = True

    exits.Open = False

    back_ground.Play_BGM()

    Start_Time = time.clock()
    Pass_Time = Start_Time

    if Font == None :
        Font = load_font('ENCR10B.TTF',30)

def TIME() :
    global MAX_Timer , Font , Start_Time , Pass_Time
    Pass_Time = time.clock() - Start_Time
    MAX_Timer = 300
    MAX_Timer -= Pass_Time
    Minute = MAX_Timer // 60
    Second = (MAX_Timer - 60 * Minute)

    if MAX_Timer > 0 :
        Font.draw(350, 650, ('Time : 0%d : %d' % (Minute, Second)), (0, 0, 0))

    else :
        Game_Over()