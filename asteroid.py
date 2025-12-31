import pygame
import circleshape
import constants
import logger
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        logger.log_event("asteroid_split")

        split_angle = random.uniform(20, 50)

        first_split_velocity = self.velocity.rotate(split_angle)
        second_split_velocity = self.velocity.rotate(-split_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        
        first_new_asteroid.velocity = first_split_velocity * 1.2
        second_new_asteroid.velocity = second_split_velocity * 1.2


        

