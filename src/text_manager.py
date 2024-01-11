import pygame
import grid_settings as st


class TextManager:

    def __init__(self):
        self.font = pygame.font.SysFont(st.FONT_TYPE, st.FONT_SIZE)
        self.text = ""
        self.text_surface = self.font.render(self.text, True, st.DEFAULT_FONT_COLOR, st.BACKGROUND)
        self.background = pygame.Rect(0, 0, st.SCREEN_SIZE_X, st.TEXT_BOX_HIGH)

    def get_text_surface(self):
        return self.text_surface

    def get_font(self):
        return self.font

    def set_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, st.DEFAULT_FONT_COLOR, st.BACKGROUND)

    def clear_text(self):
        self.set_text("")
