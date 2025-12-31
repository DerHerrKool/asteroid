import pygame
import circleshape
import shot
import constants

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90) * self.radius / 1.5
       
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
            if self.cooldown_timer < 0:
                self.cooldown_timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.cooldown_timer <= 0:
            self.shoot()
            self.cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                self.rotate(dt)
            if keys[pygame.K_RIGHT]:
                self.rotate(-dt)
        else:
            if keys[pygame.K_LEFT]:
                self.rotate(-dt)
            if keys[pygame.K_RIGHT]:
                self.rotate(dt)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, -1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.position += rotated_vector * constants.PLAYER_SPEED * dt

    

    def shoot(self):
        shot_fired = shot.Shot(self.position.x, self.position.y)
        #direction = pygame.Vector2(0, -1).rotate(self.rotation)
        #shot_fired.velocity = direction * constants.PLAYER_SHOOT_SPEED
        shot_fired.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED


    


        










