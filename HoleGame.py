import os
import pygame
import random

_image_library = {}

gamestart = False
tutorial = False
screenwidth = 500
screenheight = 700
framecount = 0


class hole:
    def __init__(self):
        self

    def draw(self):
        coords = pygame.mouse.get_pos()
        x = coords[0]
        y = coords[1]
        ellipserect = pygame.Rect(x, y, 100, 50)
        pygame.draw.ellipse(screen, (0, 0, 0), ellipserect)


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


#initialize hole
gamehole = hole()
#Game starts here
pygame.init()
#Initialize clock
clock = pygame.time.Clock()
# Set up the drawing window
screen = pygame.display.set_mode([screenwidth, screenheight])
# Run until the user asks to quit
done = False

time_since_last_action = 0



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    framecount += 1

    gamehole.draw()

    screen.blit(get_image('/Users/nplotkin/PycharmProjects/HoleGame/neckbeard.png'), (200, 200))

    # dt = clock.tick()
    # time_since_last_action += dt
    # Flip the display
    pygame.display.flip()
    screen.fill((200, 200, 200))
    # tick the clock
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
