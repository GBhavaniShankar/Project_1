import pyglet
from pyglet.sprite import Sprite
from pyglet.window import Window, mouse
from resourses import *
from drum_set import DrumSet
from piano_board import PianoBoard

# Variables
is_visible = False

game = Window(800, 600)

menu_batch = pyglet.graphics.Batch()
drum_set_batch = pyglet.graphics.Batch()
background = Sprite(background_img)
logo = Sprite(logo_img, batch=menu_batch)
loading = Sprite(loading_img, batch=menu_batch)
drums = Sprite(drums_img, batch=menu_batch)
piano = Sprite(piano_img, batch=menu_batch)
drum_set = DrumSet()
piano_board = PianoBoard()


loading.scale = 0.3
loading.opacity = 120
loading.position = 400 - (loading.width / 2), 80, 0
drums.scale = 1.1
drums.position = 400 - (drums.width / 2), 320, 0
piano.position = 400 - (piano.width / 2), 20, 0


drums.visible = False
piano.visible = False
drum_set.visible = False
piano_board.visible = False


def show_menu(dt):
    global is_visible
    drums.visible = True
    piano.visible = True
    logo.visible = False
    loading.visible = False


def on_sprite(sprite, x, y):
    return sprite.x <= x <= sprite.x + sprite.width and \
        sprite.y <= y <= sprite.y + sprite.height


@game.event
def on_draw():
    game.clear()
    background.draw()
    menu_batch.draw()
    drum_set.draw()
    piano_board.draw()

@game.event
def on_key_press(symbol, modifier):
    if drum_set.visible:
        drum_set.key_press(symbol)
    if piano_board.visible:
        piano_board.key_press(symbol)


@game.event
def on_mouse_motion(x, y, dx, dy):
    if on_sprite(drums, x, y):
        drums.scale = 1.2
    else:
        drums.scale = 1.1

    if on_sprite(piano, x, y):
        piano.scale = 1.1
    else:
        piano.scale = 1



@game.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if on_sprite(drums, x, y) and drums.visible:
            drums.visible = False
            piano.visible = False
            drum_set.visible = True
        if on_sprite(piano, x, y) and piano.visible:
            drums.visible = False
            piano.visible = False
            piano_board.visible = True


pyglet.clock.schedule_once(show_menu, 3)
pyglet.app.run()
