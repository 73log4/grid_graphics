import pygame


# ------ dimensions ----------------------------------------------------------------------------------------------------

SCREEN_SIZE_X = 660
SCREEN_SIZE_Y = 660

TEXT_BOX_HIGH = 50
TEXT_LEFT_PAD = 20

DEFAULT_X_SQUARES = 20  # default value for GridGraphics class
DEFAULT_Y_SQUARES = (SCREEN_SIZE_Y * DEFAULT_X_SQUARES) // SCREEN_SIZE_X

LINE_WIDTH = 1


# ------ font ----------------------------------------------------------------------------------------------------------

FONT_SIZE = 24
FONT_TYPE = 'arial'
DEFAULT_FONT_COLOR = (38, 50, 56)

# ------ colors --------------------------------------------------------------------------------------------------------

BACKGROUND = (255, 255, 255)
LINE_COLOR = (200, 200, 200)

# ------ color library -------------------------------------------------------------------------------------------------

GREEN = (40, 180, 99)
RED = (231, 76, 60)
YELLOW = (241, 196, 15)
BLUE = (52, 152, 219)

# ------- events dictionary --------------------------------------------------------------------------------------------

events_dic = {
    pygame.K_RIGHT: "RIGHT_KEY",
    pygame.K_LEFT: "LEFT_KEY",
    pygame.K_UP: "UP_KEY",
    pygame.KEYDOWN: "DOWN_KEY"
}
