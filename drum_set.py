from pyglet.sprite import Sprite
from pyglet.media import *
from pyglet.window.key import *
from resourses import drum_set_img


def play_sound(sound_file):
    sound = load(sound_file)
    sound.play()

class DrumSet(Sprite):

    def __init__(self):
        super().__init__(drum_set_img)

    def key_press(self,symbol):
        if symbol == B: # Bass Drum
            play_sound('assets/sfx/bass_drum_sound.mp3')
        if symbol == V: # High Tom
            play_sound('assets/sfx/high_tom_drum_sound.mp3')
        if symbol == N: # Mid Tom
            play_sound('assets/sfx/high_tom_drum_sound.mp3')
        if symbol == M: # Low Tom
            play_sound('assets/sfx/mid_tom_drum_sound.mp3')
        if symbol == C: # Snare Drum
            play_sound('assets/sfx/snare_drum_sound.mp3')
        if symbol == Z: # Ride Cymbal
            play_sound('assets/sfx/ride_cymbal_sound.mp3')
        if symbol == X: # Crash Cymbal
            play_sound('assets/sfx/crash_cymbal_sound.mp3')