import pygame

# Define constants for the screen width and height
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 718

# Color constants
COLOR_VIOLET = (237, 201, 255)
COLOR_TAUPE = (119,160, 169)
COLOR_PEACH = (255, 185, 151)
COLOR_PURPLE = (127, 90, 131)
COLOR_CHERRY = (140, 33, 85)
COLOR_LIGHT = (255, 219, 201)
COLOR_LINES = (255, 183, 146)

def drawGrid():
    blockSize = 30
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            grid = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, COLOR_LINES, grid, 1)

# Game board (window)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(COLOR_LIGHT)

# Shapes class
class Shape(object):
    rows = 20
    columns = 20

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()