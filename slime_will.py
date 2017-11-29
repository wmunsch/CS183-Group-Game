import pygame
from random import *
 
print randint(1, 100)

class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super(Slime, self).__init__()
        self.surf = pygame.image.load('graphics/slime1.png')
        self.surf = pygame.transform.scale(self.surf,(84,88))
        self.animation_speed = 10
        self.animation_speed = self.animation_speed
        self.rect = self.surf.get_rect()
        self.spawnX = 600
        self.spawnY = 400
        self.moveDistance = 0
        self.moveDirection = 0
        self.rect.move_ip(self.spawnX,self.spawnY) #player spawn point
        self.walk_left_ani = [pygame.transform.scale(pygame.image.load('graphics/slimeleftF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF4.png'),(68,60))]
        self.walk_right_ani = [pygame.transform.scale(pygame.image.load('graphics/slimerightF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF4.png'),(68,60))]
        self.walk_death_ani = [pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124))]

######## this converts all the colors or something which increases performance############
        for i in range(0,3):
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
            self.walk_death_ani[i] = self.walk_death_ani[i].convert_alpha()
            
        self.time = 0
        self.speed = 2
        
        def update(self):
            if (self.moveDistance < 1):
                self.moveDistance = randint(20,100)
                self.moveDirection = randint(1,4)
            self.time += 1
    
            if (self.moveDirection == 1 and self.moveDistance > 0):
                self.rect.move_ip(self.speed,0)
                self.moveDistance -= self.speed
                if (self.time % 12 == 0):
                    if(self.current_frame>2):
                        self.current_frame = 0
                    else:
                        self.current_frame+=1
                
                
                
                
                
                
                