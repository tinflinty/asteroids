import random

from LOGGER import log_event
import pygame
from  constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from  circleshape import CircleShape


class Asteroid(CircleShape):
    ## rendering asteroids as circles
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, LINE_WIDTH)

    ## updating position of asteroids across screen
    def update(self, dt):
        self.position += self.velocity * dt

    ## math for splitting asteroids when hit
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            ang_1 = self.velocity.rotate(angle)
            ang_2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_1.velocity = ang_1 * 1.2
            asteroid_2.velocity = ang_2 * 1.2
