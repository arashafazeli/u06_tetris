import pygame

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

def drawGrid():
    blockSize = 30
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            grid = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, COLOR_LINES, grid, 1)

def drawShape():
    pygame.draw.rect(window, COLOR_CHERRY, rect)

# Game board (window)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(COLOR_LIGHT)

# Shapes class
class Shape(object):
    rows = 20
    columns = 24
    def __init__(self, column, row, shape, color):
        self.column = column
        self.row = row
        self.shape = shape
        self.color = color
        self.rotation = 0

# Initialize pygame
pygame.init()

# Variable to keep the main loop running
running = True

# Main game loop
while running:

    # Draw out grid
    drawGrid()

    # Listen for user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pygame.display.flip()

pygame.quit()