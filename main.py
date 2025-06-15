import pyglet
from pyglet.sprite import Sprite
from pyglet.window import Window, mouse, key
from resourses import *
from drum_set import DrumSet, Stick
from piano_board import PianoBoard
from Tabala import Tabala

# Window and UI Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACK_BUTTON_WIDTH = 100
BACK_BUTTON_HEIGHT = 40
BUTTON_PADDING = 60

# Variables
is_visible = False

game = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

class BackButton(Sprite):
    def __init__(self):
        # Create a circular background
        circle_size = 40
        image = pyglet.image.SolidColorImagePattern(
            color=(40, 40, 40, 180)  # Dark gray with some transparency
        ).create_image(circle_size, circle_size)
        
        super().__init__(image)
        self.visible = False
        self.x = 30
        self.y = WINDOW_HEIGHT - 60
        
        # Create label with arrow and styling
        self.label = pyglet.text.Label(
            '←',  # Simple left arrow character
            font_name='Arial Black',  # Bold font
            font_size=24,
            x=self.x + circle_size//2,
            y=self.y + circle_size//2,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 255)  # White text
        )
        
        # Add subtle shadow effect
        self.shadow = pyglet.text.Label(
            '←',
            font_name='Arial Black',
            font_size=24,
            x=self.x + circle_size//2 + 1,
            y=self.y + circle_size//2 - 1,
            anchor_x='center',
            anchor_y='center',
            color=(0, 0, 0, 100)  # Semi-transparent black
        )

    def draw(self):
        if self.visible:
            super().draw()
            self.shadow.draw()  # Draw shadow first
            self.label.draw()   # Draw arrow on top
    
    def set_hover(self, hovering):
        """Change appearance on hover"""
        if hovering:
            self.opacity = 255
            self.label.color = (255, 255, 255, 255)  # Bright white
            self.scale = 1.1  # Slightly larger
        else:
            self.opacity = 200
            self.label.color = (220, 220, 220, 255)  # Slightly dimmed
            self.scale = 1.0  # Normal size

# Initialize sprites and batches
menu_batch = pyglet.graphics.Batch()
background = Sprite(background_img)
logo = Sprite(logo_img, batch=menu_batch)
loading = Sprite(loading_img, batch=menu_batch)
drums = Sprite(drums_img, batch=menu_batch)
tabala = Sprite(tabala_img, batch=menu_batch)
piano = Sprite(piano_img, batch=menu_batch)
black_spot = Sprite(black_spot_img)
white_spot = Sprite(white_spot_img)

# Initialize instruments
drum_set = DrumSet()
stick = Stick()
piano_board = PianoBoard()
tabala_set = Tabala()
back_button = BackButton()

# Configure sprite properties
loading.scale = 0.3
loading.opacity = 120
loading.position = WINDOW_WIDTH//2 - loading.width//2, 80, 0
drums.scale = 1.1
drums.position = 200 - drums.width//2, 320, 0
piano.position = WINDOW_WIDTH//2 - piano.width//2, 20, 0
tabala.position = 600 - tabala.width//2, 320, 0

def init_sprites():
    """Initialize sprite visibility states"""
    drums.visible = False
    piano.visible = False
    tabala.visible = False
    drum_set.visible = False
    piano_board.visible = False
    black_spot.visible = False
    white_spot.visible = False
    stick.visible = False
    tabala_set.visibility(False)
    back_button.visible = False
    logo.visible = True
    loading.visible = True

def hide_all_instruments():
    """Hide all instrument sprites and overlays."""
    drums.visible = False
    piano.visible = False
    tabala.visible = False
    drum_set.visible = False
    piano_board.visible = False
    black_spot.visible = False
    white_spot.visible = False
    stick.visible = False
    tabala_set.visibility(False)
    back_button.visible = True

def show_menu(dt):
    """Show the main menu after loading."""
    global is_visible
    hide_all_instruments()
    drums.visible = True
    piano.visible = True
    tabala.visible = True
    logo.visible = False
    loading.visible = False
    back_button.visible = False

def on_sprite(sprite, x, y):
    """Check if coordinates are within sprite bounds"""
    return sprite.x <= x <= sprite.x + sprite.width and \
           sprite.y <= y <= sprite.y + sprite.height

@game.event
def on_draw():
    """Draw all sprites"""
    game.clear()
    background.draw()
    menu_batch.draw()
    drum_set.draw()
    piano_board.draw()
    black_spot.draw()
    white_spot.draw()
    tabala_set.draw()
    stick.draw()
    back_button.draw()

@game.event
def on_key_press(symbol, modifier):
    """Handle key press events"""
    if symbol == key.ESCAPE:
        show_menu(0)
        return
        
    if drum_set.visible:
        drum_set.key_press(symbol, stick, black_spot)
    if piano_board.visible:
        piano_board.key_press(symbol, black_spot, white_spot)
    if tabala_set.is_visible():
        tabala_set.on_key_press(symbol)

@game.event
def on_key_release(symbol, modifier):
    """Handle key release events"""
    if piano_board.visible:
        piano_board.key_release(symbol, black_spot, white_spot)
    if tabala_set.is_visible():
        tabala_set.on_key_release(symbol)
    if stick.visible:
        stick.default_state()
    if drum_set.visible:
        drum_set.key_release(symbol, black_spot)

@game.event
def on_mouse_motion(x, y, dx, dy):
    """Handle mouse hover effects"""
    if back_button.visible and on_sprite(back_button, x, y):
        back_button.set_hover(True)
    else:
        back_button.set_hover(False)
    
    drums.scale = 1.2 if on_sprite(drums, x, y) else 1.1
    piano.scale = 1.1 if on_sprite(piano, x, y) else 1
    tabala.scale = 1.2 if on_sprite(tabala, x, y) else 1.1

@game.event
def on_mouse_press(x, y, button, modifiers):
    """Handle mouse click events"""
    if button == mouse.LEFT:
        if back_button.visible and on_sprite(back_button, x, y):
            show_menu(0)
        elif on_sprite(drums, x, y) and drums.visible:
            hide_all_instruments()
            drum_set.visible = True
            stick.visible = True
        elif on_sprite(piano, x, y) and piano.visible:
            hide_all_instruments()
            piano_board.visible = True
        elif on_sprite(tabala, x, y) and tabala.visible:
            hide_all_instruments()
            tabala_set.visibility(True)

# Initialize sprite states
init_sprites()

# Schedule menu display
pyglet.clock.schedule_once(show_menu, 2)

# Start the application
pyglet.app.run()