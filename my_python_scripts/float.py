import pygame
import random
from pygame.locals import *
import numpy as np
import numpy.core._dtype_ctypes

WinW = 600
WinH = 600

class floater(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(floater, self).__init__()

        self.coords = np.array(coords)

        self.rect = self.image.get_rect(center = (WinW / 2, WinH / 2))
        self._image_from_coords()

    def _image_from_coords(self):
        self.image = pygame.Surface((np.amax(self.coords[:,0], 0), np.amax(self.coords[:,1], 0)))
        pygame.draw.polygon(self.image, (255,255,255), self.coords)

pygame.init()

screen = pygame.display.set_mode((WinW, WinH))#, pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

sprites = pygame.sprite.Group()
sprites.add(floater([[0,0],
                     [50,50],
                     [0,50]]))

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                continue

    pressed_keys = pygame.key.get_pressed()

    screen.blit(background, (0, 0))

    sprites.draw(screen)
    #for sprite in sprites:
    #    screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    #pygame.display.update
    
pygame.quit()
