import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

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
   pygame.display.flip()