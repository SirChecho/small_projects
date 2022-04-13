import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.frame_index     = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction =self.direction.normalize() # direction will always be 1

        self.hitbox.x += self.direction.x * speed      # changes x coordinate of the surface
        self.collision('horizontal')

        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')

        self.rect.center = self.hitbox.center

    def collision(self,direction):

        if direction == 'horizontal':
            for sprite in self.obstacle_sprites: #checking sprites for collisions
                if sprite.hitbox.colliderect(self.hitbox): #if there is some collision:
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left #right side of player can't pass left side of obstacle
                    if self.direction.x <0: #moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom