import pyglet  # Importing our main library pyglet
from pyglet.sprite import Sprite
from pyglet.window import Window, mouse
from resourses import *
from drum_set import DrumSet, Stick
from piano_board import PianoBoard
from Tabala import Tabala

# Variables
is_visible = False

game = Window(800, 600)  # Initializing the window

menu_batch = pyglet.graphics.Batch()  # creating a batch so that all the sprites under this batch can be called at once
background = Sprite(background_img)  # converting all loaded pics and animations into sprites
logo = Sprite(logo_img, batch=menu_batch)
loading = Sprite(loading_img, batch=menu_batch)
drums = Sprite(drums_img, batch=menu_batch)
tabala = Sprite(tabala_img, batch=menu_batch)
piano = Sprite(piano_img, batch=menu_batch)
black_spot = Sprite(black_spot_img)
white_spot = Sprite(white_spot_img)

# calling all the functions defined in respective classes
drum_set = DrumSet()
stick = Stick()
piano_board = PianoBoard()
tabala_set = Tabala()

# setting the coordinates, size, opacity of the respective sprites
loading.scale = 0.3
loading.opacity = 120
loading.position = 400 - (loading.width / 2), 80, 0
drums.scale = 1.1
drums.position = 200 - (drums.width / 2), 320, 0
piano.position = 400 - (piano.width / 2), 20, 0
tabala.position = 600 - (tabala.width / 2), 320, 0

# the main part of our project, playing with visibilities, i.e. to make the respective sprites draw all at once and
# be able to see the respective sprites whenever they are called
drums.visible = False
piano.visible = False
tabala.visible = False
drum_set.visible = False
piano_board.visible = False
black_spot.visible = False
white_spot.visible = False
stick.visible = False
tabala_set.visibility(False)


def show_menu(dt):  # creating the menu page with only respective sprites visible
    global is_visible
    drums.visible = True
    piano.visible = True
    tabala.visible = True
    logo.visible = False
    loading.visible = False


def on_sprite(sprite, x, y):  # Creating the function that takes the sprite as input and returns its coordinates
    return sprite.x <= x <= sprite.x + sprite.width and \
        sprite.y <= y <= sprite.y + sprite.height


@game.event
def on_draw():  # Draws all the sprites at once
    game.clear()
    background.draw()
    menu_batch.draw()
    drum_set.draw()
    piano_board.draw()
    black_spot.draw()
    white_spot.draw()
    tabala_set.draw()
    stick.draw()


@game.event
def on_key_press(symbol, modifier):  # creating function that will be telling that a certain symbol, here key is pressed
    if drum_set.visible:
        drum_set.key_press(symbol, stick, black_spot)
    if piano_board.visible:
        piano_board.key_press(symbol, black_spot, white_spot)
    if tabala_set.is_visible():
        tabala_set.on_key_press(symbol)


@game.event
def on_key_release(symbol, modifier):  # to assign works nto be done after the release of specific key
    if piano_board.visible:
        piano_board.key_release(symbol, black_spot, white_spot)
    if tabala_set.is_visible():
        tabala_set.on_key_release(symbol)
    if stick.visible:
        stick.default_state()
    if drum_set.visible:
        drum_set.key_release(symbol, black_spot)


@game.event
def on_mouse_motion(x, y, dx, dy):  # to tell that our cursor is on particular sprite
    if on_sprite(drums, x, y):
        drums.scale = 1.2
    else:
        drums.scale = 1.1

    if on_sprite(piano, x, y):
        piano.scale = 1.1
    else:
        piano.scale = 1

    if on_sprite(tabala, x, y):
        tabala.scale = 1.2
    else:
        tabala.scale = 1.1


@game.event
def on_mouse_press(x, y, button, modifiers):  # to create a specific response on mouse click
    if button == mouse.LEFT:
        if on_sprite(drums, x, y) and drums.visible:
            drums.visible = False
            piano.visible = False
            tabala.visible = False
            drum_set.visible = True
            stick.visible = True
        if on_sprite(piano, x, y) and piano.visible:
            drums.visible = False
            piano.visible = False
            tabala.visible = False
            piano_board.visible = True
        if on_sprite(tabala, x, y) and tabala.visible:
            drums.visible = False
            piano.visible = False
            tabala.visible = False
            tabala_set.visibility(True)


pyglet.clock.schedule_once(show_menu, 2)  # function that takes function that is to be executed and after how much
# time it is to be executed

pyglet.app.run()  # Running the given code in a window
