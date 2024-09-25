import pygame as pg

class Grid:
    def __init__(self, width, height, cell_size, color='black'):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = width // cell_size
        self.rows = height // cell_size
        self.fill_color = pg.Color(color)

    def draw(self, surface):
        for x in range(0, self.width, self.cell_size):
            pg.draw.line(surface, self.fill_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pg.draw.line(surface, self.fill_color, (0, y), (self.width, y))

    def get_cell(self, x, y):
        return x // self.cell_size, y // self.cell_size
    
    def get_rect(self, x, y):
        return pg.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
    
    def get_cell_center(self, x, y):
        return self.get_rect(x, y).center
    
    def draw_in_cell(self, surface, color, x, y):
        pg.draw.rect(surface, color, self.get_rect(x, y))