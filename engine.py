#Main engine
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 700))
done = False
framerate = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('graphics/character.png')
        self.surf = pygame.transform.scale(self.surf,(76,112))
        self.animation_speed = 10
        self.animation_speed = self.animation_speed
        self.rect = self.surf.get_rect()
        self.rect.move_ip(600,400)
        self.walk_up_ani = [pygame.transform.scale(pygame.image.load('graphics/player_walking_upF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_upF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_upF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_upF4.png'),(92,124))]
        self.walk_left_ani = [pygame.transform.scale(pygame.image.load('graphics/player_walking_leftF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_leftF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_leftF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_leftF4.png'),(92,124))]
        self.walk_right_ani = [pygame.transform.scale(pygame.image.load('graphics/player_walking_rightF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_rightF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_rightF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_rightF4.png'),(92,124))]
        self.walk_down_ani = [pygame.transform.scale(pygame.image.load('graphics/player_walking_downF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_downF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_downF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_walking_downF4.png'),(92,124))]

        #self.noi = 4
        self.current_frame = 0
        self.time = 0


    def update(self, pressed_keys):
######### walking up animation ##############
        if pressed_keys[pygame.K_UP]:
            self.leftspeed = 4
            self.rightspeed = 4
            self.downspeed = 4
            self.direction = 1
            self.rect.move_ip(0, -self.upspeed)
            self.time += 1
            if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1

            self.surf = self.walk_up_ani[self.current_frame]

######### walking down animation ##############
        elif pressed_keys[pygame.K_DOWN]:
            self.leftspeed = 4
            self.rightspeed = 4
            self.upspeed = 4
            self.direction = 3
            self.rect.move_ip(0, self.downspeed)
            self.time += 1
            if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1

            self.surf = self.walk_down_ani[self.current_frame]

######### walking left animation ##############
        elif pressed_keys[pygame.K_LEFT]:
            self.rightspeed = 4
            self.rightspeed = 4
            self.upspeed = 4
            self.direction = 4
            self.rect.move_ip(-self.leftspeed, 0)
            self.time += 1
            if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1

            self.surf = self.walk_left_ani[self.current_frame]

######### walking right animation ##############
        elif pressed_keys[pygame.K_RIGHT]:
            self.leftspeed = 4
            self.downspeed = 4
            self.upspeed = 4
            self.direction = 2
            self.rect.move_ip(self.rightspeed, 0)
            self.time += 1
            if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1

            self.surf = self.walk_right_ani[self.current_frame]


    speed = 4
    leftspeed = 4
    rightspeed =4
    downspeed =4
    upspeed =4
    x = 640
    y = 350
    health = 10
    direction = 1





class Goblin:
    x = 0
    y = 0
    health = 3


class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)

class room1:
    roomimage = pygame.image.load('graphics/room2.png')
    roomimage = roomimage.convert()
    roomimage = pygame.transform.scale(roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,720)
    wallLeft2 = Wall(0,0,0,0)
    wallRight1 = Wall(1180,0,100,240)
    wallRight2 = Wall(1180,420,100,160)
    wallTop1 = Wall(0,0,570,50)
    wallTop2 = Wall(720,0,560,50)
    wallBottom1 = Wall(0,610,1280,50)
    wallBottom2 = Wall(0,0,0,0)
    wallMiddle = Wall(300,0,180,330)
    



    #wallup = 60
    #walldown = 500
    #wallleft = 100
    #wallright = 1100


#use this to update the current room when changing rooms
#def updateCurrentRoom(room):
#    currentroom = room


def checkCollision(self, sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    return(col)


player = Player()
firstroom = room1()
currentroom = firstroom
sprites_alive = pygame.sprite.Group()
sprites_walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
## add sprites to this group to draw them to the screen
sprites_alive.add(player)

sprites_walls.add(firstroom.wallLeft1)
all_sprites.add(sprites_alive,sprites_walls)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        pressed_keys = pygame.key.get_pressed()

        #if (player.rect.left < currentmap.wallLeft.right):
           #player.rect.move_ip(5, 0)

        ##using this method of collision i dont know how to make walls in the middle of the screen
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft2)):
            player.leftspeed =0
            #player.rect.move_ip(5, 0)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight2)):
            player.rightspeed =0
            #player.rect.move_ip(-5, 0)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop2)):
            player.upspeed = 0
            #player.rect.move_ip(0, 5)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom2)):
            player.downspeed = 0
            #player.rect.move_ip(0, -5)
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle)):
            if (player.direction == 1): 
                player.upspeed =0
                player.rect.move_ip(0, 1)
            if (player.direction==2): 
                player.rightspeed = 0
                player.rect.move_ip(-1, 0)
            if (player.direction==3): 
                player.downspeed = 0
                player.rect.move_ip(0, -1)
            if (player.direction ==4):
                player.leftspeed =0
                player.rect.move_ip(1, 0)
            
            
        player.update(pressed_keys)

        #screen.fill((0,0,0)) dont use anymore
        screen.blit(firstroom.roomimage,(0,0))

        for entity in sprites_alive:
            screen.blit(entity.surf, entity.rect)

        #use the following for collision detection between player and enemies
        #if pygame.sprite.spritecollideany(player, enemies):
            #player.kill()


        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
