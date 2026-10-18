
from  import Shot
import pygame
from  import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS
from  import CircleShape
import


class Player(CircleShape):
    def __init__(self, x: float, y: float, shot_cooldown: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    ## RENDERS SHIP AS TRIAGLE
    def draw(self, screen):
        pygame.draw.polygon(screen,"green", self.triangle() ,LINE_WIDTH)

    ## PLAYER INPUT
    def update(self, dt: float) -> None:
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()
        # rotational movement
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        # forward backward movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        # shooting command
        if keys[pygame.K_SPACE]:
            self.shoot()

    ## TRIANGLE MATH USED IN DRAW()
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    ## LOGIC OF PLAYER ROTATION
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    ## LOGIC OF PLAYER MOVEMENT
    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    ## LOGIC FOR SHOOTING
    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            direction *= PLAYER_SHOOT_SPEED
            shot.velocity = direction
