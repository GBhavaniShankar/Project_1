from pyglet.sprite import Sprite
from pyglet.media import load
from pyglet.window.key import B, V, N, M, C, Z, X
from resourses import drum_set_img, stick_img


def play_sound(sound_file):  # creating a function to load an audio file from its destination and play that track
    sound = load(sound_file)
    sound.play()


class DrumSet(Sprite):  # Creating a class so that we can play drums with the defined functions under it

    def __init__(self):
        super().__init__(drum_set_img)  # putting the image of drum set on the background

    def key_press(self, symbol, stick, bl):  # Assigning specific keys for certain sounds
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

    def key_release(self, symbol, bl):  # To make the black dot on the bass drum, disappear after the hitting
        if symbol == B:
            bl.visible = False


class Stick(Sprite):  # to create a stick sprite so that the animation of playing the drum will be more realistic

    def __init__(self):
        super().__init__(stick_img)  # to put the stick sprite in the drum set
        self.scale = 0.2
        self.set(445, 250, -90)

    def set(self, x, y, rotation):  # to make the stick move
        self.rotation = rotation
        self.x = x
        self.y = y

    def default_state(self):  # setting the default place for stick
        self.set(445, 250, -90)
