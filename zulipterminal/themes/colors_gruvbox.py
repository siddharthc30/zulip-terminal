"""
COLORS FOR GRUVBOX THEMES
-------------------------
Contains color definitions or functions common across gruvbox themes.
For further details on themefiles look at the theme contribution guide.

This file uses the official gruvbox colors where possible.
For color reference see:
    https://github.com/morhetz/gruvbox/blob/master/colors/gruvbox.vim
"""
from enum import Enum

from zulipterminal.config.color import color_properties


# fmt: off
# NOTE: The 24bit color codes use 256 color which can be
# enhanced to be truly 24bit.
# NOTE: The 256code format can be moved to h0-255 to
# make use of the complete range instead of only 216 colors.

class GruvBoxColor(Enum):
    # color          =  16code          256code   24code
    DEFAULT          = 'default         default   default'
    DARK0_HARD       = 'black           h234      #1d2021'
    GRAY_244         = 'dark_gray       h244      #928374'
    LIGHT2           = 'white           h250      #d5c4a1'
    LIGHT4           = 'light_gray      h248      #bdae93'
    BRIGHT_BLUE      = 'light_blue      h109      #83a598'
    BRIGHT_GREEN     = 'light_green     h142      #b8bb26'
    BRIGHT_RED       = 'light_red       h167      #fb4934'
    NEUTRAL_PURPLE   = 'light_magenta   h132      #b16286'
    NEUTRAL_BLUE     = 'dark_cyan       h66       #458588'
    NEUTRAL_YELLOW   = 'brown           h172      #d79921'
    FADED_BLUE       = 'dark_blue       h24       #076678'
    FADED_YELLOW     = 'brown           h136      #b57614'
    FADED_RED        = 'dark_red        h88       #9d0006'
    LIGHT0_HARD      = 'white           h230      #f9f5d7'
    GRAY_245         = 'dark_gray       h245      #928374'
    DARK2            = 'black           h239      #504945'
    DARK4            = 'black           h243      #7c6f64'
    BRIGHT_YELLOW    = 'brown           h214      #fabd2f'
    FADED_GREEN      = 'dark_green      h100      #79740e'


# fmt: on


DefaultBoldColor = color_properties(GruvBoxColor, "BOLD")
