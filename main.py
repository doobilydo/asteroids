# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)
    AsteroidField.containers = (group_updatable,)

    asteroid_field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for o in group_updatable:
            o.update(dt)

        for asteroid in group_asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        for o in group_drawable:
            o.draw(screen)

        
        pygame.display.flip()
        dt = clock.tick(60)/1000 




if __name__ == "__main__":
    main()


