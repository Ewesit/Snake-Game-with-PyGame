# Import the tkinter module and all its functions and classes
from tkinter import *

# Import the random module
import random


# Set the width and height of the game window
WIDTH = 800
HEIGHT = 600

# Set the size of each segment of the snake
SEG_SIZE = 20

# Set a flag to indicate whether the game is currently in progress
IN_GAME = True

# Create a new tkinter window
window = Tk()

# Set the title of the window
window.title("Snake Game")

# Disable window resizing
window.resizable(False, False)

# Create a canvas widget that fills the window and set its background color to black
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")

# Pack the canvas widget into the window
canvas.pack()

# Add the rest of your game code here

# Start the tkinter event loop
window.mainloop()

