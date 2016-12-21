def Block(MARIO , Marios):
    Size_X , Size_Y = 52 , 50

    for mario in Marios:
        if MARIO.Num != mario.Num and mario.Select == False and MARIO.Jump != MARIO.Jump_Down:
            if RIGHT(MARIO) > LEFT(mario) and RIGHT(MARIO) < RIGHT(mario) : #Left Collision
                if Mario_Air(MARIO,mario) or MARIO.Y == mario.Y :
                    MARIO.X = mario.X - Size_X

            elif LEFT(MARIO) < RIGHT(mario) and LEFT(MARIO) > LEFT(mario) :  #Right Collision
                if Mario_Air(MARIO,mario) or MARIO.Y == mario.Y :
                    MARIO.X = mario.X + Size_X

        elif MARIO.Num != mario.Num and mario.Select == True and MARIO.Jump != MARIO.Jump_Down:

            if RIGHT(MARIO) > LEFT(mario) and RIGHT(MARIO) < RIGHT(mario) :
                if Mario_Air(MARIO,mario) or MARIO.Y == mario.Y :
                    MARIO.X = mario.X - Size_X

            elif LEFT(MARIO) < RIGHT(mario) and LEFT(MARIO) > LEFT(mario) :
                if Mario_Air(MARIO,mario) or MARIO.Y == mario.Y :
                    MARIO.X = mario.X + Size_X

def Air_BLOCK(MARIO, Marios) :
    Size_X, Size_Y = 52, 50

    for mario in Marios :
        if MARIO.Num != mario.Num :
            if LEFT(MARIO) > LEFT(mario) and LEFT(MARIO) < RIGHT(mario) :
                if DOWN(MARIO) < UP(mario) and DOWN(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Down:
                    MARIO.Jump = MARIO.Jump_None
                    MARIO.Jump_State = 0
                    MARIO.Y = mario.Y + Size_Y
                    mario.Y = MARIO.Y - Size_Y
                    if MARIO.Move:
                        MARIO.State = 1
                    else:
                        MARIO.State = 0

                elif UP(MARIO) < UP(mario) and UP(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Up:
                    MARIO.Y = mario.Y - Size_Y
                    mario.Y = MARIO.Y + Size_Y
                    MARIO.Jump = MARIO.Jump_Down
                    MARIO.Jump_State = 0

            elif RIGHT(MARIO) > LEFT(mario) and RIGHT(MARIO) < RIGHT(mario) :
                if DOWN(MARIO) < UP(mario) and DOWN(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Down:
                    MARIO.Jump = MARIO.Jump_None
                    MARIO.Jump_State = 0
                    MARIO.Y = mario.Y + Size_Y

                    if MARIO.Move:
                        MARIO.State = 1
                    else:
                        MARIO.State = 0

                elif UP(MARIO) < UP(mario) and UP(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Up:
                    MARIO.Y = mario.Y - Size_Y
                    MARIO.Jump = MARIO.Jump_Down
                    MARIO.Jump_State = 0

            elif MARIO.X == mario.X :
                if DOWN(MARIO) < UP(mario) and DOWN(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Down:
                    MARIO.Jump = MARIO.Jump_None
                    MARIO.Jump_State = 0
                    MARIO.Y = mario.Y + Size_Y
                    mario.Y = MARIO.Y - Size_Y

                    if MARIO.Move:
                        MARIO.State = 1
                    else:
                        MARIO.State = 0

                elif UP(MARIO) < UP(mario) and UP(MARIO) > DOWN(mario) and MARIO.Jump == MARIO.Jump_Up:
                    MARIO.Y = mario.Y - Size_Y
                    mario.Y = MARIO.Y + Size_Y
                    MARIO.Jump = MARIO.Jump_Down
                    MARIO.Jump_State = 0

def LEFT(MARIO) :
    return MARIO.X - 26

def RIGHT(MARIO) :
    return MARIO.X + 26

def DOWN(MARIO) :
    return MARIO.Y - 25

def UP(MARIO) :
    return MARIO.Y + 25

def Mario_Air(MARIO,mario) :
    return DOWN(MARIO) < UP(mario) and DOWN(MARIO) > DOWN(mario)