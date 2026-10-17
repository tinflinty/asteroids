from turtle import update

from shot import Shot
import pygame
from asteroid import Asteroid
from constants import  PLAYER_SHOOT_COOLDOWN_SECONDS, SCREEN_HEIGHT,  SCREEN_WIDTH
from LOGGER import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    ## BASIC GAME FUNCTIONALITY, CLOCK, SCREEN SIZE
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ## ASSIGN CONTAINERS TO CLASSES
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    ## CREATE INITIAL GAME OBJECTS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable ,shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SHOOT_COOLDOWN_SECONDS)
    asteroid_field = AsteroidField()

    ## sets Delta time
    dt = 0.0


    ## MAIN GAME LOOP ##
    while True:
        log_state()

        ## closes window when player hits the exit window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ## any game updates
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        ## checks for collisions between player and asteroid
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        ## draws anything needed, screen does screen background and loop does sprites
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        ## game tick
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
