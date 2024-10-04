import pygame
from circleshape import *


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):        
        self.position += self.velocity * dt