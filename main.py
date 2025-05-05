from constants import *
import pygame
import player
import asteroid
import asteroidfield
import circleshape
import shot



def main():

    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #create groups for game, that not everything is updated the same way?? i guess -> less updates
    updateble_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    asteroidfield_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    #add Player objects to the groups
    player.Player.containers = (updateble_group, drawable_group)
    #add Asteroid objects to the groups
    asteroid.Asteroid.containers = (asteroids_group, updateble_group, drawable_group)
    #add asteroid objects to groups
    asteroidfield.AsteroidField.containers = (updateble_group)

    shot.Shot.containers = (updateble_group, drawable_group, shot_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock() #tick clock 60fps
    dt = 0

    #create player
    player_obj = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield_obj = asteroidfield.AsteroidField()

    while True:
        screen.fill((0, 0 ,0))
        for drawable_obj in drawable_group:
            drawable_obj.draw(screen)
        #rotate player
        updateble_group.update(dt)

        for a in asteroids_group:
            if circleshape.CircleShape.collision_check(player_obj, a):
                return
        
        for a in asteroids_group:
            for b in shot_group:
                if circleshape.CircleShape.collision_check(a, b):
                    asteroid.Asteroid.split(a)
                    b.kill()
            
            
            
        #refresh screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000


    









if __name__ == "__main__":
    main()

print("Game over!")