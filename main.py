from lib2to3.pygram import python_grammar_no_print_statement
import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Define constants for the play area with and height
PLAY_WIDTH = 300
PLAY_HEIGHT = 600

# Global variables
block_size = 30
top_left_x = (SCREEN_WIDTH - PLAY_WIDTH) // 2
top_left_y = SCREEN_HEIGHT - PLAY_HEIGHT

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    QUIT,
)

# Color constants
S_COLOR = (237, 201, 255)
Z_COLOR = (119,160, 169)
I_COLOR = (255, 185, 151)
O_COLOR = (127, 90, 131)
J_COLOR = (140, 33, 85)
L_COLOR = (22, 93, 108)
T_COLOR = (232, 131, 180)
BG_COLOR = (255, 219, 201)
GRID_COLOR = (255, 183, 146)

# Shape formats

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# Shapes represented by index 0-6
shapes = [S, Z, I, O, J, L, T]
shape_colors = [S_COLOR, Z_COLOR, I_COLOR, O_COLOR, J_COLOR, L_COLOR, T_COLOR]

class Shape(object):
    def __init__(self, column, row, shape):
        self.col = column
        self.row = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid():
    '''
    To keep track on locked positions
    '''

    grid = [[BG_COLOR for x in range(10)] for x in range(20)]

    #TODO: check for locked positions

    return grid

def convert_shape_format(shape):
    '''
    Take shape format and create actual shape from reading 0's
    Returns the coordinates for where the shape will be drawn
    '''
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def draw_grid(surface, row, col):
    '''
    Draw line for every row and column in play area
    pygame.draw.line(surface, color, start_pos(coordinates), end_pos(coordinates))
    '''
    for i in range (row):
        # Start pos = upper left, End pos = end of play area
        # Y increased by block_size to get right spacing
        pygame.draw.line(surface, GRID_COLOR, (top_left_x, top_left_y + i * block_size), (top_left_x + PLAY_WIDTH, top_left_y + i * block_size))
        for j in range(col):
            pygame.draw.line(surface, GRID_COLOR, (top_left_x + j * block_size, top_left_y), (top_left_x + j * block_size, top_left_y + PLAY_HEIGHT))

def draw_screen(surface):
    surface.fill(BG_COLOR)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    draw_grid(surface, 20, 10)

    # Draw out play area border
    pygame.draw.rect(surface, GRID_COLOR, (top_left_x, top_left_y, PLAY_WIDTH, PLAY_HEIGHT), 5)

def get_shape():
    '''
    Returns a random shape format from list of shapes
    '''
    return Shape(5, 0, random.choice(shapes))

# Initialize pygame
pygame.init()

# Main game loop
def main():
    global grid 
    grid = create_grid()

    # Variable to keep the main loop running
    change_piece = False
    running = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while running:

        # Keep track of fall time
        fall_speed = .27
        fall_time += clock.get_rawtime()
        clock.tick()

        # Listen for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                quit()
        
        draw_screen(window)
        pygame.display.update()        

def main_menu():
    main()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

main_menu() # Start gane