import pygame
import os 
import random

class ramenbowl(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.vel = 5
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'ramenbowl.PNG')), (width, height))
    
    def move(self, direction):
        if direction == "RIGHT" and self.x + self.vel + self.width - 20 < 360:
            self.x += self.vel 
        if direction == "LEFT" and self.x - self.vel > -20:
            self.x -= self.vel 
    

class softegg(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height 
        self.vel = vel
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'softegg.PNG')), (width, height))

    def RESPAWN(self):
        self.x = random.randrange(0, 315)
        self.y = 5


class rottenegg(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.vel = vel 
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'hardegg.PNG')), (width, height))

    def RESPAWN(self):
        self.x = random.randrange(0, 315)
        self.y = 5

