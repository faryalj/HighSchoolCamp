"""
title: pygame_practice
author: Faryal
date: 2019-06-14 09:48
"""

import pygame

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.

PI = 3.141592653
white = (255, 255, 255)
brown = (222, 184, 135)
black = (0, 0, 0)
pink = (255, 105, 180)
dark_brown = (139, 69, 19)
blue = (100, 149, 237)
jeans = (25, 25, 112)
screen.fill(white)

done = False
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, pink, [260 + x, 330 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, brown, [200 + x, 100 + y], 70)
    pygame.draw.circle(screen, black, [200 + x, 100 + y], 70, 10)

    pygame.draw.ellipse(screen, white, [215 + x, 75 + y, 25, 15])
    pygame.draw.ellipse(screen, white, [160 + x, 75 + y, 25, 15])

    pygame.draw.circle(screen, dark_brown, [228 + x, 82 + y], 6)
    pygame.draw.circle(screen, dark_brown, [172 + x, 82 + y], 6)

    pygame.draw.arc(screen, pink, [176 + x, 82 + y, 50, 60], PI, 0, 5)

    pygame.draw.rect(screen, brown, [180 + x, 158 + y, 40, 40])
    pygame.draw.rect(screen, black, [140 + x, 158 + y, 40, 40])
    pygame.draw.rect(screen, black, [140 + x, 158 + y, 40, 40])
    pygame.draw.rect(screen, blue, [150 + x, 199 + y, 100, 120])
    pygame.draw.rect(screen, jeans, [150 + x, 315 + y, 46, 180])
    pygame.draw.rect(screen, jeans, [205 + x, 315 + y, 46, 180])

    pygame.draw.ellipse(screen, blue, [120 + x, 195 + y, 50, 40])
    pygame.draw.ellipse(screen, blue, [225 + x, 195 + y, 50, 40])

    pygame.draw.line(screen, brown, [130 + x, 230 + y], [125 + x, 350 + y], 10)
    pygame.draw.line(screen, brown, [260 + x, 230 + y], [270 + x, 350 + y], 10)

# Loop as long as done == False
while not done:
    ball_pos += ball_change
    if ball_pos > 70:
        ball_change -= 1
    elif ball_pos < 200:
        ball_change += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    x_coord += x_speed
    y_coord += y_speed

    x_speed = 0
    y_speed = 0

    screen.fill(white)

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(60)
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.


# Be IDLE friendly
pygame.quit(s)




