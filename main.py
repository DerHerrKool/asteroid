import pygame
import player
import asteroid
import asteroidfield
import shot
import constants
import logger 
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    shot.Shot.containers = (shots, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable

    player1 = player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))
    asteroid_field = asteroidfield.AsteroidField()

    while True:
        logger.log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        screen.fill("black")

        updatable.update(dt)

        for asteroid_sprite in asteroids:
            if asteroid_sprite.collides_with(player1):
                logger.log_event("player_hit")
                print("Game over!")
                sys.exit()
      
        for asteroid_sprite in asteroids:
            for shot_sprite in shots:
                if asteroid_sprite.collides_with(shot_sprite):
                    logger.log_event("asteroid_shot")
                    asteroid_sprite.split()
                    shot_sprite.kill()
 
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
               
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
