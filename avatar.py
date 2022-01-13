import random
from turtle import position

import pygame
from pygame.math import Vector2
from creep import Creep

import core


class Avatar:
    def __init__(self):
        self.position = Vector2(600,400)
        self.rayon = 20
        self.nourriture = 1
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 100
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxacc = 100
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 1
        self.vitessmax = 4
        self.taillemax = 300
        core.memory("c",Creep())



    def moov(self , destination):
        if destination is not None:
            #F=uk|l-lo|
            l=self.position.distance_to(destination)
            u=destination - self.position
            u=u.normalize()
            self.acceleration=u*self.k*abs(l-self.l0)


        #bilan des force


        #attention max force
        if self.acceleration.length() > self.maxacc:
            self.acceleration.scale_to_length(self.maxacc)

        #ajout de F a la vitess
        self.vitesse = self.vitesse + self.acceleration

        #attention max et min vitess
        if self.vitesse.length()>self.vitessmax:
            self.vitesse.scale_to_length(self.vitessmax)

        if self.vitesse.length() + 2 < self.vitessmin:
            self.vitesse.scale_to_length(self.vitessmin)

        #ajout vitesse a position
        self.position = self.position + self.vitesse

        #remise a zero de F
        self.acceleration = Vector2(0,0)

    def manger(self,creep):
        for idx, p in enumerate(creep):
            if p.position.distance_to(self.position) < self.rayon:
                creepTmp=p
                core.memory("listCreep").pop(idx)
                self.nourriture += 1
                self.takeWeight(creepTmp)
                print(self.nourriture,self.masse)
                core.memory("listCreep").append(Creep())

    def takeWeight (self,creep):
        self.masse += creep.masse















    def show(self):
        core.Draw.circle(self.couleur,self.position,self.rayon)
        core.Draw.line((1,43,92),self.position,self.position+self.vitesse*100,1)