from pyglet.sprite import Sprite
from pyglet.media import *
from pyglet.window.key import *
from resourses import drum_set_img, stick


def play_sound(sound_file):
    sound = load(sound_file)
    sound.play()


class DrumSet(Sprite):

    def __init__(self):
        super().__init__(drum_set_img)

    def key_press(self, symbol, stick, bl):
        if symbol == B:  # Bass Drum
            play_sound('assets/sfx/drum_sfx/bass_drum_sound1.mp3')
            bl.scale = 2.7
            bl.position = 345, 140, 0
            bl.opacity = 170
            bl.visible = True
        if symbol == V:  # High Tom
            play_sound('assets/sfx/drum_sfx/Tom 1.mp3')
            stick.set(370, 270, -100)
        if symbol == N:  # Mid Tom
            play_sound('assets/sfx/drum_sfx/Tom 2.mp3')
            stick.set(560, 270, -100)
        if symbol == M:  # Floor Tom
            play_sound('assets/sfx/drum_sfx/Floor tom.mp3')
            stick.set(340, 330, -340)
        if symbol == C:  # Snare Drum
            play_sound('assets/sfx/drum_sfx/Snare.mp3')
            stick.set(365, 105, -130)
        if symbol == Z:  # Ride Cymbal
            play_sound('assets/sfx/drum_sfx/ride_cymbal_sound1.mp3')
            stick.set(300, 250, -130)
        if symbol == X:  # Crash Cymbal
            play_sound('assets/sfx/drum_sfx/crash_cymbal_sound.mp3')
            stick.set(520, 250, -30)


    def key_release(self, symbol, bl):
        if symbol == B:
            bl.visible = False


class Stick(Sprite):

    def __init__(self):
        super().__init__(stick)
        self.scale = 0.2
        self.set(445, 250, -90)

    def set(self, x, y, rotation):
        self.rotation = rotation
        self.x = x
        self.y = y

    def default_state(self):
        self.set(445, 250, -90)
