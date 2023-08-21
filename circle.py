import pygame,sys
from pygame import Vector2 as Vec2

class Ball():
    def __init__(self, pos, acc, size, color, w, h):
        self.pos = Vec2(pos)
        self.ppos = Vec2(pos) + Vec2(0.000001, 0.000001)
        self.acc = acc
        self.rad = size
        self.color = color
        self.h = h
        self.w = w

    def updatepos(self,dt):
        vel = self.pos - self.ppos
        vel.clamp_magnitude(self.rad)

        self.ppos.x = self.pos.x
        self.ppos.y = self.pos.y
        self.pos = self.pos + 0.99 * vel + self.acc * dt * dt

        self.acc.x = 0
        self.acc.y = 0

    def applyForce(self,force):
        self.acc += force

        
    def satisfyConstrain(self):
        if self.pos.x < self.rad:
            temp = self.pos.x
            self.pos.x = self.rad
            self.ppos.x = self.pos.x + temp - self.ppos.x
        if self.pos.y < self.rad:
            temp = self.pos.y
            self.pos.y = self.rad
            self.ppos.y = temp + self.ppos.y - self.pos.y
            
        if self.pos.x > self.w - self.rad:
            temp = self.pos.x
            self.pos.x = self.w - self.rad
            self.ppos.x = self.pos.x + temp - self.ppos.x
        if self.pos.y > self.h - self.rad:
            temp = self.pos.y
            self.pos.y = self.h - self.rad
            self.ppos.y = self.pos.y + temp - self.ppos.y

    def checkCollision(self,other):
        if self == other:
            return
        dist = self.pos.distance_to(other.pos)
        if dist < self.rad + other.rad:
            penetration_dist = (self.rad + other.rad - dist) / 2
            mv = self.pos - other.pos
            mv.scale_to_length(penetration_dist)
            mv = mv / 2
            self.pos += mv
            other.pos -= mv

    def show(self,screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
        