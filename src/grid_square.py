import pygame
import grid_settings as st


class GridSquare:
    """
    A class that represents a square in the grid of a GridGraphics class.
    has a color attribute and a filled attribute, which is true when the
    square holds some color
    """

    def __init__(self, x, y, sq_size):
        r_coordinate = (x * sq_size[0], y * sq_size[1] + st.TEXT_BOX_HIGH)
        self.rect = pygame.Rect(*r_coordinate, sq_size[0], sq_size[1])
        self.sq_size = sq_size

        self.color = None
        self.color_filled = False

        self.image = None
        self.image_rect = None
        self.image_filled = False

    def set_image(self, image, pad=1):
        """
        loads and adds the image to the square, the image can have padding,
        which is represented by a percentage of the square
        """
        image_size = (image.get_width(), image.get_height())
        max_ratio = min(self.sq_size[0] / image_size[0], self.sq_size[1] / image_size[1]) * pad

        image = pygame.transform.scale(image, (image_size[0] * max_ratio, image_size[1] * max_ratio))

        self.image_rect = image.get_rect()
        self.image_rect.center = self.rect.center

        self.image = image
        self.image_filled = True

    def clear_image(self):
        self.image = None
        self.image_filled = False

    def set_color(self, color):
        self.color = color
        self.color_filled = True

    def clear_color(self):
        self.color = None
        self.color_filled = False

    def clear(self):
        self.clear_color()
        self.clear_image()
