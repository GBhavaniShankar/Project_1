import pyglet.graphics
from pyglet.sprite import Sprite
from pyglet.media import *
from pyglet.window.key import *
from resourses import piano_board_img, black_spot_img



def play_sound(sound_file):
    sound = load(sound_file)
    sound.play()

class PianoBoard(Sprite):


    def __init__(self):
        super().__init__(piano_board_img)

    def key_press(self, symbol, bl, ws):
        if symbol == Z:
            play_sound('assets/sfx/piano_sfx/Bo.mp3')
            bl.scale = 2.7
            bl.position = 0, 30, 0
            bl.visible = True
        if symbol == X:
            play_sound('assets/sfx/piano_sfx/C2.mp3')
            bl.scale = 2.7
            bl.position = 114, 30, 0
            bl.visible = True
        if symbol == C:
            play_sound('assets/sfx/piano_sfx/E3.mp3')
            bl.scale = 2.7
            bl.position = 229, 30, 0
            bl.visible = True
        if symbol == V:
            play_sound('assets/sfx/piano_sfx/F4.mp3')
            bl.scale = 2.7
            bl.position = 343, 30, 0
            bl.visible = True
        if symbol == B:
            play_sound('assets/sfx/piano_sfx/G5.mp3')
            bl.scale = 2.7
            bl.position = 457, 30, 0
            bl.visible = True
        if symbol == N:
            play_sound('assets/sfx/piano_sfx/C6.mp3')
            bl.scale = 2.7
            bl.position = 571, 30, 0
            bl.visible = True
        if symbol == M:
            play_sound('assets/sfx/piano_sfx/G6.mp3')
            bl.scale = 2.7
            bl.position = 686, 30, 0
            bl.visible = True
        if symbol == S:
            play_sound('assets/sfx/piano_sfx/sec key.mp3')
            ws.scale = 1.7
            ws.position = 68, 250, 0
            ws.visible = True
        if symbol == D:
            play_sound('assets/sfx/piano_sfx/Bb-[AudioTrimmer.com].mp3')
            ws.scale = 1.7
            ws.position = 194, 250, 0
            ws.visible = True
        if symbol == G:
            play_sound('assets/sfx/piano_sfx/c#-[AudioTrimmer.com].mp3')
            ws.scale = 1.7
            ws.position = 408, 250, 0
            ws.visible = True
        if symbol == H:
            play_sound('assets/sfx/piano_sfx/d#-[AudioTrimmer.com].mp3')
            ws.scale = 1.7
            ws.position = 533, 250, 0
            ws.visible = True
        if symbol == J:
            play_sound('assets/sfx/piano_sfx/g#-[AudioTrimmer.com].mp3')
            ws.scale = 1.7
            ws.position = 660, 250, 0
            ws.visible = True


    def key_release(self, symbol, bl, ws):
        if symbol == Z:
            bl.visible = False
        if symbol == X:
            bl.visible = False
        if symbol == C:
            bl.visible = False
        if symbol == V:
            bl.visible = False
        if symbol == B:
            bl.visible = False
        if symbol == N:
            bl.visible = False
        if symbol == M:
            bl.visible = False
        if symbol == S:
            ws.visible = False
        if symbol == D:
            ws.visible = False
        if symbol == G:
            ws.visible = False
        if symbol == H:
            ws.visible = False
        if symbol == J:
            ws.visible = False

