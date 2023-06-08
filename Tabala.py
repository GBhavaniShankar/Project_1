from pyglet.sprite import Sprite
from pyglet import *
from pyglet.window.key import *
from resourses import *


def play_sound(sound_file):  # creating a function to load an audio file from its destination and play that track
    sound = media.load(sound_file)
    sound.play()


class Tabala:  # creating tabala set to play with tabala

    def __init__(self):  # assigning coordinates for different sprites involved in this tabala set
        self.outer_tabala_1 = Sprite(outer_tabala_1_img, x=20, y=150, z=0)
        self.outer_tabala_2 = Sprite(outer_tabala_2_img, x=380, y=150, z=0)
        self.outer_tabala_2.scale = 1.2
        self.middle_tabala_1 = Sprite(middle_tabala_1_img, x=75, y=205, z=0)
        self.middle_tabala_2 = Sprite(middle_tabala_2_img, x=445, y=220, z=0)
        self.middle_tabala_2.scale = 1.2
        self.inner_tabala_1 = Sprite(inner_tabala_1_img, x=118, y=245, z=0)
        self.inner_tabala_2 = Sprite(inner_tabala_2_img, x=497, y=268, z=0)
        self.inner_tabala_2.scale = 1.2
        self.tabala_visibility = False

    def draw(self):  # drawing all the components of the tabala
        self.outer_tabala_1.draw()
        self.outer_tabala_2.draw()
        self.middle_tabala_1.draw()
        self.middle_tabala_2.draw()
        self.inner_tabala_1.draw()
        self.inner_tabala_2.draw()

    def visibility(self, is_visible):  # setting the visibility of all the components of the tabala, to same as that
        # of the tabala class
        self.outer_tabala_1.visible = is_visible
        self.outer_tabala_2.visible = is_visible
        self.middle_tabala_1.visible = is_visible
        self.middle_tabala_2.visible = is_visible
        self.inner_tabala_1.visible = is_visible
        self.inner_tabala_2.visible = is_visible
        self.tabala_visibility = is_visible

    def on_key_press(self, symbol):  # to play certain sounds on pressing specific keys and do some custom animations
        if symbol == A:
            self.outer_tabala_1.position = 6, 133, 0
            self.outer_tabala_1.scale = 1.1
            play_sound('assets/sfx/tabala_sfx/outer1.mp3')
        if symbol == J:
            self.outer_tabala_2.x = 366
            self.outer_tabala_2.y = 133
            self.outer_tabala_2.scale = 1.3
            play_sound('assets/sfx/tabala_sfx/outer2.mp3')
        if symbol == S:
            self.middle_tabala_1.x = 62
            self.middle_tabala_1.y = 196
            self.middle_tabala_1.scale = 1.1
            play_sound('assets/sfx/tabala_sfx/middle1.mp3')
        if symbol == D:
            self.inner_tabala_1.x = 111
            self.inner_tabala_1.y = 238
            self.inner_tabala_1.scale = 1.1
            play_sound('assets/sfx/tabala_sfx/inner1.mp3')
        if symbol == K:
            self.middle_tabala_2.x = 433
            self.middle_tabala_2.y = 205
            self.middle_tabala_2.scale = 1.3
            play_sound('assets/sfx/tabala_sfx/middle2.mp3')
        if symbol == L:
            self.inner_tabala_2.x = 490
            self.inner_tabala_2.y = 263
            self.inner_tabala_2.scale = 1.3
            play_sound('assets/sfx/tabala_sfx/inner2.mp3')

    def on_key_release(self, symbol):  # resets the tabala sprites to its default place
        if symbol == A:
            self.outer_tabala_1.scale = 1
            self.outer_tabala_1.position = 20, 150, 0
        if symbol == J:
            self.outer_tabala_2.x = 380
            self.outer_tabala_2.y = 150
            self.outer_tabala_2.scale = 1.2
        if symbol == S:
            self.middle_tabala_1.x = 75
            self.middle_tabala_1.y = 205
            self.middle_tabala_1.scale = 1
        if symbol == D:
            self.inner_tabala_1.x = 118
            self.inner_tabala_1.y = 245
            self.inner_tabala_1.scale = 1
        if symbol == K:
            self.middle_tabala_2.x = 445
            self.middle_tabala_2.y = 220
            self.middle_tabala_2.scale = 1.2
        if symbol == L:
            self.inner_tabala_2.x = 497
            self.inner_tabala_2.y = 268
            self.inner_tabala_2.scale = 1.2

    def is_visible(self):  # setting the visibility of tabala set
        return self.tabala_visibility
