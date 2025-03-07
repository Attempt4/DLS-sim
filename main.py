import numpy as np
import matplotlib.pyplot as plt
import pygame

from scipy.fft import fft

import numpy as np

from random import randint as rint


##  Gaussian Distribution functions - normalised
def Gaussian(x,s,m):

    norm = np.sqrt(2 * np.pi * s)

    return (1/(norm)*np.exp(-(x-m)**2 / s**2))



##  For x values between 0 and 1 only
def reverse_Gaussian(x,s,m):
    parity = (-1) ** rint(1,10)

    norm = np.sqrt(2 * np.pi * s)

    return m - parity * s * (-np.log(x))**0.5



##  Define a system of particles with a Gaussian size distribution

WIDTH, HEIGHT = 800, 600

MARGIN_BUFFER = 40

par_mu = 2.00
par_sigma = 0.70


class np_config:

    def __init__(self):
        
        seed = reverse_Gaussian(rint(0,100)*0.01, par_sigma, par_mu)

        self.x = rint(0+MARGIN_BUFFER,WIDTH-MARGIN_BUFFER)
        self.y = rint(0+MARGIN_BUFFER,HEIGHT-MARGIN_BUFFER)
        self.vx = reverse_Gaussian(rint(0,100)*0.01, 2.00, 0.00)
        self.vy = reverse_Gaussian(rint(0,100)*0.01, 2.00, 0.00)
        self.R = seed


##  Define an array of N Particle objects

N = 300


Intensity_fluc_ = []


Particles =  [np_config() for _ in range(N)]

P_R = [float(Particles[_].R) for _ in range(N)]

#plt.hist(np.array(P_R), 15, range=[par_mu - 2*par_sigma, par_mu + 2*par_sigma])

#plt.show()

##  Initialize Pygame
pygame.init()

##  Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle with Velocity")

##  Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

QUAD = 120

##  Circle properties

##  Clock for controlling FPS
clock = pygame.time.Clock()

delta_time = 0.1



running = True

for i in range(1000):

    if i % 1000 == 0:
        print(i)

    shield_buffer = 0
    screen.fill(WHITE)  ##  Clear screen

    ##  Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##  Update position for each particle in the system
    for p in Particles:

        ##  Update Velocity
        p.x += delta_time * p.vx
        p.y += delta_time * p.vy

        ##  Momentum Exchance Calculation
        for q in Particles:
            if abs(p.x - q.x) <= abs(p.R + q.R) and abs(p.y - q.y) <= abs(p.R + q.R) and q != p:
                u1 = p.vx
                u2 = q.vx
                m1 = p.R
                m2 = q.R
                p.vx = ( (m1 - m2) * u1 + 2 * m2 * u2 ) / (m1 + m2)
                q.vx = ( (m2 - m1) * u2 + 2 * m1 * u1 ) / (m1 + m2)

                u1 = p.vy
                u2 = q.vy
                p.vy = ( (m1 - m2) * u1 + 2 * m2 * u2 ) / (m1 + m2)
                q.vy = ( (m2 - m1) * u2 + 2 * m1 * u1 ) / (m1 + m2)

                

        ##  Bounce off walls
        if p.x - p.R <= 0 or p.x + p.R >= WIDTH:
            p.vx *= -1  # Reverse X velocity
        if p.y - p.R <= 0 or p.y + p.R >= HEIGHT:
            p.vy *= -1  # Reverse Y velocity


        ##  Bound within Quadrat
        if (p.x >= 0.5 * ( WIDTH - QUAD ) and p.x <= 0.5 * ( WIDTH + QUAD )) and (p.y >= 0.5 * ( HEIGHT - QUAD ) and p.y <= 0.5 * ( HEIGHT + QUAD )):
            shield_buffer += p.R**2



        ##  Draw the circle
        pygame.draw.circle(screen, RED, [p.x, p.y], p.R)
        pygame.draw.rect(screen, BLUE, pygame.Rect(0.5 * ( WIDTH - QUAD ), 0.5 * ( HEIGHT - QUAD ), QUAD, QUAD),  2)

    ##  Update the display
    pygame.display.flip()

    ##  Limit FPS
    #clock.tick(120)

    Intensity_fluc_.append(np.pi * shield_buffer * QUAD**-2)

    #print(np.pi * shield_buffer * QUAD**-2)

Intensity_fluc_ = np.array(Intensity_fluc_)

fluc_Spectrum_ = fft(Intensity_fluc_)

plt.plot(fluc_Spectrum_)

plt.show()

pygame.quit()