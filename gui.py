import tkinter as tk
import os
from platform import system
from grid import Grid
import pygame as pg
import time

root = tk.Tk()
root.title('IHC - Reconocimiento de voz')

# Embed for pygame window
embed = tk.Frame(root, width=800, height=600)
embed.grid(columnspan=(600), rowspan=500)  # Adds grid
embed.pack(side=tk.LEFT)  # packs window to the left

# Button window
buttonwin = tk.Frame(root, width=75, height=500)
buttonwin.pack(side=tk.LEFT)

# Set up os environment variables
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
if system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Initialize pygame
PG_WIDTH, PG_HEIGHT, CELL_SIZE = 800, 600, 100
pg.init()
screen = pg.display.set_mode((PG_WIDTH, PG_HEIGHT))

# create Grid object (scr_width, scr_height, cell_size, color)
grid = Grid(PG_WIDTH, PG_HEIGHT, CELL_SIZE, 'white')

# main loop
def main():
    running = True
    clock = pg.time.Clock() 

    while running:
        # Handle pygame events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Clear the screen
        screen.fill(pg.Color('black'))

        # Draw the grid
        grid.draw(screen)

        # Update the display
        pg.display.update()

        # Limit the loop to 30 frames per second
        clock.tick(30)

        # Update the Tkinter window
        root.update_idletasks()
        root.update()

main()

# Close pygame and the Tkinter window
pg.quit()
root.quit()