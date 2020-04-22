# Variables, keybindings
import arcade

# Main values
game_name = 'Ice, water and steam!'
game_version = 'alpha'
game_title = game_name + ' ' + game_version
screen_width = 1200
screen_height = 600
screen_update_rate = 1/60
skip_intro = False
game_scene = ('intro',
              'screen')

# Graphics options:
start_fullscreen = False
allow_resizable_window = False
allow_visible_mouse = True

# Developer mode
developermode = True
gridScreenStart = 0
gridScreenStep = 50

def get_start_scene(self, check_no_intro):
    if skip_intro:
        _start_scene = game_scene[1]
    else:
        _start_scene = game_scene[0]
    return _start_scene

# Default keybindings
key_developer_mode = arcade.key.BACKSPACE
