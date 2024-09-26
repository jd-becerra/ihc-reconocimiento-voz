import pygame as pg

class Grid:
    def __init__(self, width, height, cell_size, color='black'):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = width // cell_size
        self.rows = height // cell_size
        self.fill_color = pg.Color(color)
        self.player_sprite = pg.image.load('src/mono.png')
        self.player_sprite = pg.transform.scale(self.player_sprite, (cell_size, cell_size))
        self.player_position = (self.columns // 2, self.rows // 2)

    def draw(self, surface):
        for x in range(0, self.width, self.cell_size):
            pg.draw.line(surface, self.fill_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pg.draw.line(surface, self.fill_color, (0, y), (self.width, y))
        self.draw_player(surface)

    def get_cell(self, x, y):
        return x // self.cell_size, y // self.cell_size
    
    def get_rect(self, x, y):
        return pg.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
    
    def get_cell_center(self, x, y):
        return self.get_rect(x, y).center
    
    def draw_in_cell(self, surface, color, x, y):
        pg.draw.rect(surface, color, self.get_rect(x, y))

    def draw_player(self, surface):
        player_center = self.get_cell_center(*self.player_position)
        surface.blit(self.player_sprite, self.player_sprite.get_rect(center=player_center))
    def move_player(self, dx, dy):
        new_x = self.player_position[0] + dx
        new_y = self.player_position[1] + dy
        if 0 <= new_x < self.columns and 0 <= new_y < self.rows:
            self.player_position = new_x, new_y
    