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

# Define the Snake class
class Snake:
    def __init__(self):
        self.direction = "Up"  # Initial direction of the snake
        self.segments = [(100, 100)]  # Initial position of the snake
        self.direction = "Right"   # Initial direction of the snake

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - SEG_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + SEG_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - SEG_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + SEG_SIZE, head_y)
        self.segments = [new_head] + self.segments[:-1]

    def change_direction(self, event):
        global IN_GAME
        if IN_GAME:
            if event.keysym in ["Up", "Down", "Left", "Right"]:
                self.direction = event.keysym
            if event.keysym == "Up" and self.direction != "Down":
                self.direction = "Up"
            elif event.keysym == "Down" and self.direction != "Up":
                self.direction = "Down"
            elif event.keysym == "Left" and self.direction != "Right":
                self.direction = "Left"
            elif event.keysym == "Right" and self.direction != "Left":
                self.direction = "Right"
        else:
            if event.keysym == "Return":
                self.restart_game()


    def add_segment(self):
        self.segments.append(self.segments[-1])
    
    def restart_game(self):
        global IN_GAME
        IN_GAME = True
        self.segments = [(100, 100)]
        self.direction = "Right"
        food.position = (SEG_SIZE * random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE),
                        SEG_SIZE * random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE))

# Define the Food class
class Food:
    def __init__(self):
        self.position = (SEG_SIZE * random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE),
                         SEG_SIZE * random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE))

# Game functions
def game_loop():
    global IN_GAME
    if IN_GAME:
        snake.move()
        check_collision()
        check_boundary()
        redraw_canvas()
        canvas.after(100, game_loop)
    else:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Helvetica", 24))

def check_collision():
    if snake.segments[0] == food.position:
        snake.add_segment()
        food.position = (SEG_SIZE * random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE),
                          SEG_SIZE * random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE))

def check_boundary():
    if not (0 <= snake.segments[0][0] < WIDTH and 0 <= snake.segments[0][1] < HEIGHT):
        game_over()

def redraw_canvas():
    canvas.delete("all")
    for segment in snake.segments:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + SEG_SIZE, segment[1] + SEG_SIZE, fill="white")
    canvas.create_oval(food.position[0], food.position[1], food.position[0] + SEG_SIZE, food.position[1] + SEG_SIZE, fill="red")

def game_over():
    global IN_GAME
    IN_GAME = False

# Initialize game objects
snake = Snake()
food = Food()

# Redraw the canvas to display the initial state of the game
redraw_canvas()

# Bind the change_direction method to the key press event
window.bind("<KeyPress>", snake.change_direction)

# Start the game loop
game_loop()

# Start the tkinter event loop
window.mainloop()
