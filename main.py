import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

# Color constants
COLOR_VIOLET = (237, 201, 255)
COLOR_TAUPE = (119,160, 169)
COLOR_PEACH = (255, 185, 151)
COLOR_PURPLE = (127, 90, 131)
COLOR_CHERRY = (140, 33, 85)
COLOR_LIGHT = (255, 219, 201)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize pygame
pygame.init()

# Variable to keep the main loop running
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with color
    window.fill(COLOR_LIGHT)

    pygame.display.flip()