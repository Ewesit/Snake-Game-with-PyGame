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
#Define the Snake class
class Snake:
    def __init__(self):
        self.segments = [(100, 100)] #This line creates an attribute called segments for the object (self). 
        #It's a list containing a single tuple (100, 100). This tuple represents the initial position of the snake.
        self.direction = "Right"   #This line creates another attribute called direction for the object (self). 
        #It's a string set to "Right", indicating the initial direction of the snake.


# Start the tkinter event loop
window.mainloop()

