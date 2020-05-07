#pyinstaller --onefile fileName.py
# import the pygame module
import pygame

# import random for random numbers!
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *
import numpy as np
import numpy.core._dtype_ctypes

defWinW = 600
defWinH = 600

class blob(pygame.sprite.Sprite):
    def __init__(self):
        super(blob, self).__init__()
        self.maxSpeed = random.random()*80+20
        self.acceleration = random.random()*2+0.4
        self.deceleration = self.acceleration/4
        self.surf = pygame.Surface((1+np.log(self.maxSpeed)*4, np.log(self.maxSpeed)*4+1))
        self.surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.surf.get_rect(center=(random.randint(0, winW), random.randint(0, winH)))
        self.velocity = np.array([0,0])
        self.gravity = 1
        self.realVelocity = np.array([0,0])

    def update(self, pressed_keys):
        self.move(pressed_keys)
        self.checkBounds("bounce")
        
        
    def move(self, pressed_keys):
        decelerating = np.array([pressed_keys[K_a]==pressed_keys[K_d], pressed_keys[K_w]==pressed_keys[K_s]])
        if pressed_keys[K_w]:
            #decelerating[1] = pressed_keys[K_DOWN]
            if self.velocity[1] >= -self.maxSpeed:
                self.velocity[1] -= self.acceleration
        if pressed_keys[K_s]:
            #decelerating[1] = pressed_keys[K_UP]
            if self.velocity[1] <= self.maxSpeed:
                self.velocity[1] += self.acceleration
        if pressed_keys[K_a]:
            #decelerating[0] = pressed_keys[K_RIGHT]
            if self.velocity[0] >= -self.maxSpeed:
                self.velocity[0] -= self.acceleration
        if pressed_keys[K_d]:
            #decelerating[0] = pressed_keys[K_LEFT]
            if self.velocity[0] <= self.maxSpeed:
                self.velocity[0] += self.acceleration
        
        self.velocity = np.sign(self.velocity)*(0<np.abs(self.velocity)-self.deceleration*decelerating)*(np.abs(self.velocity)-self.deceleration *decelerating)
        
        self.rect.move_ip(self.velocity[0], self.velocity[1])

    def checkBounds(self, mode):
        if(mode == "bounce"):
            if self.rect.right > winW:
                self.rect.right = winW-self.velocity[0]
                self.velocity[0] = -self.velocity[0]
            elif self.rect.left < 0:
                self.rect.left = 0-self.velocity[0]
                self.velocity[0] = -self.velocity[0]
            elif self.rect.top < 0:
                self.rect.top = 0-self.velocity[1]
                self.velocity[1] = -self.velocity[1]
            elif self.rect.bottom > winH:
                self.rect.bottom = winH-self.velocity[1]
                self.velocity[1] = -self.velocity[1]
        if(mode == "wrap"):
            if self.rect.left > winW:
                self.rect.right = 0-self.rect.left%winW
            elif self.rect.right < 0:
                self.rect.left = winW+self.rect.right%winW
            elif self.rect.bottom < 0:
                self.rect.top = winH+self.rect.bottom%winH
            elif self.rect.top > winH:
                self.rect.bottom = 0-self.rect.top%winH
        else:
            if self.rect.left > winW:
                self.kill()
            elif self.rect.right < 0:
                self.kill()
            elif self.rect.bottom < 0:
                self.kill()
                self.rect.top = winH
            elif self.rect.top > winH:
                self.kill()
                self.rect.bottom = 0

# initialize pygame
pygame.init()

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
winW, winH = pygame.display.get_surface().get_size()

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1)

# create our 'player', right now he's just a rectangle
#player = Player()

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

blobs = pygame.sprite.Group()
#all_sprites.add(player)

running = True

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        for i in range(10):
            blobs.add(blob())
    if pressed_keys[K_r]:
        for entity in blobs:
            entity.kill()
        screen.blit(background, (0, 0))
    if pressed_keys[K_F11]:
        if screen.get_flags() & FULLSCREEN:
            pygame.quit()
            screen = pygame.display.set_mode((defWinW, defWinH), RESIZABLE)
        else:
            pygame.quit()
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        winW, winH = pygame.display.get_surface().get_size()
        background = pygame.Surface((winW,winH))
        
    blobs.update(pressed_keys)
    #print(pressed_keys[K_UP], pressed_keys[K_DOWN])
    
    for entity in blobs:    
        screen.blit(entity.surf, entity.rect)

    #pygame.display.update()
    pygame.display.flip()
pygame.quit()