from pyglet.sprite import Sprite
from pyglet.media import *
from pyglet.window.key import *
from resourses import piano_board_img


def play_sound(sound_file):
    sound = load(sound_file)
    sound.play()

class PianoBoard(Sprite):


    def __init__(self):
        super().__init__(piano_board_img)

    def key_press(self,symbol):
        if symbol == Z:
            play_sound('assets/sfx/piano_sfx/Bo.mp3')
        if symbol == X:
            play_sound('assets/sfx/piano_sfx/C2.mp3')
        if symbol == C:
            play_sound('assets/sfx/piano_sfx/E3.mp3')
        if symbol == V:
            play_sound('assets/sfx/piano_sfx/F4.mp3')
        if symbol == B:
            play_sound('assets/sfx/piano_sfx/G5.mp3')
        if symbol == N:
            play_sound('assets/sfx/piano_sfx/C6.mp3')
        if symbol == M:
            play_sound('assets/sfx/piano_sfx/G6.mp3')


        # if symbol == S:
        #     play_sound('assets/sfx/piano_sfx/F1.mp3')
        # if symbol == D:
        #     play_sound('assets/sfx/piano_sfx/Bb-[AudioTrimmer.com].mp3')
        # if symbol == G:
        #     play_sound('assets/sfx/piano_sfx/c#-[AudioTrimmer.com].mp3')
        # if symbol == H:
        #     play_sound('assets/sfx/piano_sfx/d#-[AudioTrimmer.com].mp3')
        # if symbol == J:
        #     play_sound('assets/sfx/piano_sfx/g#-[AudioTrimmer.com].mp3')


