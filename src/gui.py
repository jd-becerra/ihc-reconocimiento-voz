# src/gui.py
import tkinter as tk
import os
from platform import system
import pygame as pg
from src.grid import Grid
from src.voice_recognition import VoiceRecognition


def start_app():
    voice = VoiceRecognition()

    pg.init()

    root = tk.Tk()
    root.title('IHC - Reconocimiento de voz')

    # Move player with arrow keys
    root.bind('<Up>', lambda e: grid.move_player(0, -1))
    root.bind('<Down>', lambda e: grid.move_player(0, 1))
    root.bind('<Left>', lambda e: grid.move_player(-1, 0))
    root.bind('<Right>', lambda e: grid.move_player(1, 0))

    # Embed for pygame window
    embed = tk.Frame(root, width=800, height=600)
    embed.grid(columnspan=(600), rowspan=500)  # Adds grid
    embed.pack(side=tk.LEFT)  # packs window to the left

    # GUI window
    guiwin = tk.Frame(root, width=75, height=500)
    guiwin.pack(side=tk.RIGHT)
    # Add button that makes VOICE_ENABLED = not VOICE_ENABLED
    def toggle_button():
        voice.toggle()
        # Change button color to red if voice is enabled, else to gray
        button.config(bg='red' if voice.enabled else 'gray')
        button.config(text='Grabando...' if voice.enabled else 'Click para grabar voz')
    
    button = tk.Button(guiwin, text='Click para grabar voz', command=toggle_button)
    button.pack(side=tk.TOP)
    # Add display of voice text
    welcome_banner = 'Da click en el boton para empezar a hablar' if voice.microphone else 'ERROR: No se pudo acceder al microfono'
    voice_display = tk.Label(guiwin, text=welcome_banner, wraplength=300)
    voice_display.pack(side=tk.TOP)


    # Set up os environment variables
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    if system() == 'Windows':
        os.environ['SDL_VIDEODRIVER'] = 'windib'

    # Initialize pygame
    PG_WIDTH, PG_HEIGHT, CELL_SIZE = 800, 600, 100
    screen = pg.display.set_mode((PG_WIDTH, PG_HEIGHT))
    line_color = 'white'
    # create Grid object (scr_width, scr_height, cell_size, color)
    grid = Grid(PG_WIDTH, PG_HEIGHT, CELL_SIZE, line_color)

    def voice_move_player(command):
        command = command.lower()
        if command == 'norte':
            grid.move_player(0, -1)
        elif command == 'sur':
            grid.move_player(0, 1)
        elif command == 'este':
            grid.move_player(-1, 0)
        elif command == 'oeste':
            grid.move_player(1, 0)
        elif command == 'noreste':
            grid.move_player(-1, -1)
        elif command == 'noroeste':
            grid.move_player(1, -1)
        elif command == 'sureste':
            grid.move_player(-1, 1)
        elif command == 'suroeste':
            grid.move_player(1, 1)

    # main loop
    running = True
    clock = pg.time.Clock() 
    log_output = ''

    while running:
        # Handle pygame events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update the voice recognition if enabled
        if voice.enabled:
            # Move player based on voice command
            if voice.output != '':
                out = voice.output.lower()
                log_output += out + '\n'
                voice_move_player(out)
            voice.output = ''
            voice_display.config(text=log_output)

        # Clear the screen
        screen.fill(pg.Color('black' if line_color == 'white' else 'white'))

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