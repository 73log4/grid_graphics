import pygame
import grid_settings as st
from grid_square import GridSquare
from text_manager import TextManager


class GridGraphics:
    """
    A graphical interface for a grid. The interface aims at hiding all
    the pygame facilities in a clear way. The grid squares can be colored and hold values.
    The interface supports coloring/clearing squares and holding the window without change.
    """

    def __init__(self, x=st.DEFAULT_X_SQUARES, y=st.DEFAULT_Y_SQUARES):
        GridGraphics.init_pygame()

        self.x_dim, self.y_dim = x, y
        self.sq_size = (st.SCREEN_SIZE_X / x, st.SCREEN_SIZE_Y / y)
        self.grid = [[GridSquare(j, i, self.sq_size) for j in range(x)] for i in range(y)]
        self.pos = [(xx, yy) for xx in range(self.x_dim) for yy in range(self.y_dim)]

        self.text_manager = TextManager()
        self.text_changed = False

        self.changed_squares = set()

        self.screen = pygame.display.set_mode((st.SCREEN_SIZE_X, st.SCREEN_SIZE_Y + st.TEXT_BOX_HIGH))
        self.screen.fill(st.BACKGROUND)

        self.events = pygame.event.get()

        self.update()

    @staticmethod
    def init_pygame():
        pygame.init()
        pygame.display.set_caption('Grid')

    def valid_square(self, x, y, err=True):
        """ raise a range error if square is out of grid range"""
        if not (0 <= x < self.x_dim and 0 <= y < self.y_dim):
            if err:
                exit(f"Error: square coordinate ({x}, {y}) is out of range")
            return False
        return True

    def __getitem__(self, cor):
        """ get the item at position [x, y] (not [x][y]) """
        x, y = cor
        self.valid_square(x, y)
        return self.grid[y][x]

    def update_square(self, x, y):
        self.changed_squares.add((x, y))

    def color_square(self, x, y, color):
        sq = self[x, y]
        sq.color = color
        sq.color_filled = True
        self.update_square(x, y)

    def color_rectangle(self, x, y, width, height, color):
        for i in range(width):
            for j in range(height):
                self.color_square(x + i, y + j, color)

    def add_image(self, x, y, image_path, pad=1):
        """
        adds the image to the grid to the specified square. the image can have padding,
        which is represented by a percentage of the square
        """
        sq = self[x, y]
        sq.set_image(pygame.image.load(image_path).convert_alpha(), pad)
        self.update_square(x, y)

    def display_text(self, text):
        self.text_manager.set_text(text)
        self.text_changed = True

    def clear_square_color(self, x, y):
        self[x, y].clear_color()
        self.update_square(x, y)

    def clear_square_image(self, x, y):
        self[x, y].clear_image()
        self.update_square(x, y)

    def clear_all(self):
        for x, y in self.pos:
            sq = self[x, y]
            if sq.color_filled or sq.image_filled:
                self.clear_square_color(x, y)
                self.clear_square_image(x, y)
                self.update_square(x, y)

    def hold(self, delay_s=float("inf")):
        """ don't change the grid for a number of seconds but still keep track of window updates """
        start_time = pygame.time.get_ticks()
        delay_ms = delay_s * 1000
        while pygame.time.get_ticks() < start_time + delay_ms:
            self.update(delay_seconds=0, hold=True)

    def get_events(self):
        """ returns a list with string representations of the possible events that are covered """
        events, events_str = [ev for ev in self.events], []
        for e in events:
            if e.type == pygame.KEYDOWN:
                key_type = e.key
                if key_type in st.events_dic:
                    events_str.append(st.events_dic[key_type])
        return events_str

    def load_events(self, hold=False):
        new_events = pygame.event.get()
        events = []
        for ev in new_events:
            if ev.type in st.COVERED_EVENTS:
                events.append(ev)
        if hold:
            self.events += events
        else:
            self.events = events


    def check_for_window_events(self):
        """ check for any window events """
        for ev in self.events:
            if ev.type == pygame.QUIT:
                exit()

    def draw_text(self):
        if self.text_changed:
            pygame.draw.rect(self.screen, st.BACKGROUND, self.text_manager.background)

            text_surface = self.text_manager.get_text_surface()
            text_rect = text_surface.get_rect()
            text_rect.topleft = (st.TEXT_LEFT_PAD, (st.TEXT_BOX_HIGH - text_rect.height) // 2)
            self.screen.blit(text_surface, text_rect)
            self.text_changed = False

    def clear_text(self):
        self.text_manager.clear_text()
        self.text_changed = True

    def draw_grid_squares(self):
        for x, y in self.changed_squares:
            sq = self.grid[y][x]
            if sq.color_filled:  # square has some color
                pygame.draw.rect(self.screen, sq.color, sq.rect)
            else:
                pygame.draw.rect(self.screen, st.BACKGROUND, sq.rect)  # draw background color
            if sq.image_filled:
                self.screen.blit(sq.image, sq.image_rect)

    def draw_grid_lines(self):
        for y in range(self.y_dim):
            start_pos = (0, y * self.sq_size[1] + st.TEXT_BOX_HIGH)
            end_pos = (st.SCREEN_SIZE_X, y * self.sq_size[1] + st.TEXT_BOX_HIGH)
            pygame.draw.line(self.screen, st.LINE_COLOR, start_pos, end_pos, st.LINE_WIDTH)
        for x in range(1, self.x_dim):
            start_pos = (x * self.sq_size[0], st.TEXT_BOX_HIGH)
            end_pos = (x * self.sq_size[0], st.SCREEN_SIZE_Y + st.TEXT_BOX_HIGH)
            pygame.draw.line(self.screen, st.LINE_COLOR, start_pos, end_pos, st.LINE_WIDTH)

    def update(self, delay_seconds=0, hold=False):
        """ draw the current state of the grid, save events and update the pygame display"""
        self.check_for_window_events()

        self.draw_text()
        self.draw_grid_squares()
        self.draw_grid_lines()

        self.load_events(hold)

        pygame.display.update()
        self.changed_squares.clear()

        if delay_seconds:
            self.hold(delay_seconds)
