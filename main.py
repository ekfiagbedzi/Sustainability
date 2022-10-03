import random

import pygame
from utils import scale_image, draw, Bin, Waste, Item
from score import score


# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

WASTE = ["Gloves.png", "Chemical powder.png", "Eppendorf.png", "Chemical powder.png", "Broken Flask.png", "Syringe Tip.png"]


# load images
LAB = Item("images/lab.jpg").load_image()
GLOVE = Waste("images/" + random.choice(WASTE)).load_image(50)
BIN1 = Bin(item_path="images/Bin.png", position=(0, 300), bin_type="images/Bin.png").load_image(75)
BIN2 = Bin(item_path="images/Bin.png", position=(100, 300), bin_type="images/Bin.png").load_image(75)
BIN3 = Bin(item_path="images/Bin.png", position=(200, 300), bin_type="images/Bin.png").load_image(75)
BIN4 = Bin(item_path="images/Bin.png", position=(300, 300), bin_type="images/Bin.png").load_image(75)

# set window
WIDTH, HEIGHT = LAB.get_width(), LAB.get_height()
GLOVE_SPEED = 1
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set window name
pygame.display.set_caption("Sustainability Game!!!")

# play background music
pygame.mixer.music.load("sounds/lab_radio.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# set frame rate per second
FPS = 60

## set initial image position
glove_x = random.randrange(0, WIDTH)
glove_y = 0

# code for main game
run = True
clock = pygame.time.Clock()
images = [(LAB, (0, 0)), (BIN1, (0, 300)), (BIN2, (100, 300)), (BIN3, (200, 300)), (BIN4, (300, 300))]
scoreboard = score(0, 500, 10)

while run:
    clock.tick(FPS)  # keep image at FPS 60 on all devices

    draw(WIN, images)  # draw all static images
    WIN.blit(GLOVE, (glove_x, glove_y))  # draw image of glove
    scoreboard.display(WIN)
    pygame.display.update()  # show your drawings on screen

    for event in pygame.event.get():

        # loop through all events
        if event.type == pygame.QUIT:  # if user presses clicks X
            run = False
            break

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:  # if user presses right arrow key
            glove_x += 100  # move object to the right
        elif key[pygame.K_LEFT]:  # if user presses left arrow key
            glove_x -= 100  # move object to the left
    glove_y += GLOVE_SPEED  # cause object to fall


    if glove_y > HEIGHT:  # if object moves off screen
        glove_x = random.randrange(0, WIDTH)  # new object falls from different x position on screen
        glove_y = -25  # bring new object at different position
        GLOVE = scale_image(pygame.image.load("images/" + random.choice(WASTE)), 50)  # select random waste
        scoreboard.add()

pygame.quit()
