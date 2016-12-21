from pico2d import *

class Back_Ground:

    bgm = None
    image_Bottom = None
    image_BackGround = None

    def __init__(self):
        if Back_Ground.image_Bottom == None :
            Back_Ground.image_Bottom = load_image('./Resource/Bottom_962.png')

        if Back_Ground.image_BackGround == None:
            Back_Ground.image_BackGround = load_image('./Resource/BackGround_Sky.png')

        if Back_Ground.bgm == None :
            Back_Ground.bgm = load_music('./Music/BGM.mp3')


    def Play_BGM(self):
        Back_Ground.bgm.repeat_play()

    def Stop_BGM(self):
        Back_Ground.bgm.stop()

    def draw(self):
        self.image_BackGround.clip_draw(0,0,962,530,481,435)
        self.image_Bottom.clip_draw(0,0,962,169,481,85)