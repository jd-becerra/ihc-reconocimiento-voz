# src/gui.py
import tkinter as tk
import os
from platform import system
import pygame as pg
from src.grid import Grid
import src.voice_recognition as voice_recognition

def start_app():
    voice = voice_recognition.VoiceRecognition()
    VOICE_TEXT = 'Da click en el boton para empezar a hablar'
    VOICE_ENABLED = False

    pg.init()

    root = tk.Tk()
    root.title('IHC - Reconocimiento de voz')

    # Embed for pygame window
    embed = tk.Frame(root, width=800, height=600)
    embed.grid(columnspan=(600), rowspan=500)  # Adds grid
    embed.pack(side=tk.LEFT)  # packs window to the left

    # GUI window
    guiwin = tk.Frame(root, width=75, height=500)
    guiwin.pack(side=tk.RIGHT)
    # Add button that makes VOICE_ENABLED = not VOICE_ENABLED
    button = tk.Button(guiwin, text='Grabar voz', command=voice.toggle)
    button.pack(side=tk.TOP)
    # Add display of voice text
    voice_display = tk.Label(guiwin, text=VOICE_TEXT)
    voice_display.pack(side=tk.TOP)


    # Set up os environment variables
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    if system() == 'Windows':
        os.environ['SDL_VIDEODRIVER'] = 'windib'

    # Initialize pygame
    PG_WIDTH, PG_HEIGHT, CELL_SIZE = 800, 600, 100
    screen = pg.display.set_mode((PG_WIDTH, PG_HEIGHT))

    # create Grid object (scr_width, scr_height, cell_size, color)
    grid = Grid(PG_WIDTH, PG_HEIGHT, CELL_SIZE, 'white')

    # main loop
    running = True
    clock = pg.time.Clock() 

    while running:
        # Handle pygame events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update the voice recognition if enabled
        if voice.enabled:
            voice_text = voice.listen()
            voice_display.config(text=voice_text)

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

    # Close pygame and the Tkinter window
    pg.quit()
    root.destroy()
