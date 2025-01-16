from circleshape import *
import random
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return None
        else:
            # Spawn two new asteroids
            asteroid_1 = Asteroid(self.position.x, self.position.y, 
                                  self.radius - constants.ASTEROID_MIN_RADIUS)
            asteroid_2 = Asteroid(self.position.x, self.position.y, 
                                  self.radius - constants.ASTEROID_MIN_RADIUS)
            random_angle = random.uniform(20,50)
            speed = 1.2

            asteroid_1.velocity = pygame.Vector2(self.velocity)
            asteroid_1.velocity = asteroid_1.velocity.rotate(random_angle) * speed
            asteroid_2.velocity = pygame.Vector2(self.velocity)
            asteroid_2.velocity = asteroid_2.velocity.rotate(random_angle * -1) * speed
            
            return asteroid_1, asteroid_2