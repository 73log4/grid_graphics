import pygame


# ------ dimensions ----------------------------------------------------------------------------------------------------

SCREEN_SIZE_X = 600
SCREEN_SIZE_Y = 600

TEXT_BOX_HIGH = 40
TEXT_LEFT_PAD = 10

DEFAULT_Y_SQUARES = 20  # default value of squares in the Y direction
DEFAULT_X_SQUARES = (SCREEN_SIZE_X * DEFAULT_Y_SQUARES) // SCREEN_SIZE_Y

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
    pygame.K_DOWN: "DOWN_KEY"
}
