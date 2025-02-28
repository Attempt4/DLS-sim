import numpy as np
import matplotlib.pyplot as plt
import pygame

from random import randint as rint

def Gaussian(x,s,m):
    return (1/(np.sqrt(2*np.pi*s))*np.exp(-(x-m)**2 / s**2))


##  Define a system of particles with a Gaussian size distribution


WIDTH, HEIGHT = 800, 600

MARGIN_BUFFER = 100

class np_config:

    def __init__(self):
        self.x = rint(0+MARGIN_BUFFER,WIDTH-MARGIN_BUFFER)
        self.y = rint(0+MARGIN_BUFFER,HEIGHT-MARGIN_BUFFER)
        self.vx = rint(0,40)/10
        self.vy = rint(0,40)/10
        self.R = rint(0,10)


N = 100

Particles =  [np_config() for _ in range(N)]





import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle with Velocity")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Circle properties

# Clock for controlling FPS
clock = pygame.time.Clock()

delta_time = 1.00

running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position with velocity
    for p in Particles:
        p.x += delta_time * p.vx
        p.y += delta_time * p.vy

        # Bounce off walls
        if p.x - p.R <= 0 or p.x + p.R >= WIDTH:
            p.vx *= -1  # Reverse X velocity
        if p.y - p.R <= 0 or p.y + p.R >= HEIGHT:
            p.vy *= -1  # Reverse Y velocity

        # Draw the circle
        pygame.draw.circle(screen, RED, [p.x, p.y], p.R)

    # Update the display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()