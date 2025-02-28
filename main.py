import numpy as np
import matplotlib.pyplot as plt
import pygame

from random import randint as rint

def Gaussian(x,s,m):
    return (1/(np.sqrt(2*np.pi*s))*np.exp(-(x-m)**2 / s**2))


##  Define a system of particles with a Gaussian size distribution

class np_config:
    x = 0



    

import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle with Velocity")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties
radius = 20
position = np.array([WIDTH // 2, HEIGHT // 2], dtype=float)  # Position vector
velocity = np.array([3, 2], dtype=float)  # Velocity vector

# Clock for controlling FPS
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position with velocity
    position += velocity

    # Bounce off walls
    if position[0] - radius <= 0 or position[0] + radius >= WIDTH:
        velocity[0] *= -1  # Reverse X velocity
    if position[1] - radius <= 0 or position[1] + radius >= HEIGHT:
        velocity[1] *= -1  # Reverse Y velocity

    # Draw the circle
    pygame.draw.circle(screen, RED, position.astype(int), radius)

    # Update the display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()