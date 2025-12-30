import pygame
import player
import constants
import logger 
# import log_state



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
    player.Player.containers = (updatable, drawable)

    player1 = player.Player((constants.SCREEN_WIDTH / 2), (constants.SCREEN_HEIGHT / 2))


    while True:
        logger.log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        screen.fill("black")

        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
               
        dt = clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
