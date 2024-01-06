import pygame
import grid_settings as st


class GridSquare:
    """
    A class that represents a square in the grid of a GridGraphics class.
    has a color attribute and a filled attribute, which is true when the
    square holds some color
    """

    def __init__(self, c=None):
        self.color = c
        self.filled = (c is not None)


class GridGraphics:
    """
    A graphical interface for a grid. The interface aims at hiding all
    the pygame facilities in a clear way. The grid squares can be colored and hold values.
    The interface supports coloring/clearing squares and holding the window without change.
    """

    def __init__(self, x, y):
        GridGraphics.init_pygame()

        self.grid = [[GridSquare() for j in range(x)] for i in range(y)]
        self.dim = (x, y)
        self.sq_size = (st.SCREEN_SIZE_X // x, st.SCREEN_SIZE_Y // y)
        self.pos = [(xx, yy) for xx in range(self.dim[0]) for yy in range(self.dim[1])]

        self.screen = pygame.display.set_mode((st.SCREEN_SIZE_X, st.SCREEN_SIZE_Y))

        self.events = pygame.event.get()

        self.update()

    @staticmethod
    def init_pygame():
        pygame.init()
        pygame.display.set_caption('Grid')

    def valid_square(self, x, y):
        """ raise a range error if square is out of grid range"""
        if not (0 <= x < self.dim[0] and 0 <= y < self.dim[1]):
            exit(f"Error: square coordinate ({x}, {y}) is out of range")

    def __getitem__(self, cor):
        """ get the item at position [x, y] (not [x][y]) """
        x, y = cor
        self.valid_square(x, y)
        return self.grid[y][x]

    def color_square(self, x, y, color):
        sq = self[x, y]
        sq.color = color
        sq.filled = True

    def clear_square(self, x, y):
        sq = self[x, y]
        sq.color = None
        sq.filled = False

    def clear_all(self):
        for x, y in self.pos:
            self.clear_square(x, y)

    def hold(self, delay_s):
        """ don't change the grid for a number of ms but still keep track of window updates """
        start_time = pygame.time.get_ticks()
        delay_ms = delay_s * 1000
        while pygame.time.get_ticks() < start_time + delay_ms:
            self.update()

    def get_events(self):
        """ returns a list with string representations of the possible events that are covered """
        events_type, events_str = [ev.type for ev in self.events], []
        for t in events_type:
            if t in st.events_dic:
                events_str.append(st.events_dic[t])
        return events_str

    def check_for_window_events(self):
        """ check for any window events """
        for ev in self.events:
            if ev.type == pygame.QUIT:
                exit()

    def draw_grid_squares(self):
        for x, y in self.pos:
            sq = self.grid[y][x]
            if sq.filled:  # square has some color
                r_coordinate = (x * self.sq_size[0], y * self.sq_size[1])
                r = pygame.Rect(*r_coordinate, self.sq_size[0], self.sq_size[1])
                pygame.draw.rect(self.screen, sq.color, r)

    def draw_grid_lines(self):
        for y in range(self.dim[1]):
            start_pos = (0, y * self.sq_size[1])
            end_pos = (st.SCREEN_SIZE_X, y * self.sq_size[1])
            pygame.draw.line(self.screen, st.LINE_COLOR, start_pos, end_pos, st.LINE_WIDTH)
        for x in range(1, self.dim[0]):
            start_pos = (x * self.sq_size[0], 0)
            end_pos = (x * self.sq_size[0], st.SCREEN_SIZE_X)
            pygame.draw.line(self.screen, st.LINE_COLOR, start_pos, end_pos, st.LINE_WIDTH)

    def update(self):
        """ draw the current state of the grid, save events and update the pygame display"""
        self.check_for_window_events()

        self.screen.fill(st.BACKGROUND)
        self.draw_grid_squares()
        self.draw_grid_lines()

        pygame.display.update()
        self.events = pygame.event.get()




