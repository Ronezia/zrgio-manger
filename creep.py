import random
import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.position = Vector2(random.randint(0,1295),random.randint(0,995))
        self.rayon = 5
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10

    def ghost (self):
        pass







    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)






#random.randint(0,800).x,random.randint(0,800).y