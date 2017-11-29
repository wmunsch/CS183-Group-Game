#Main engine
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
blackFadeScreen = pygame.Surface((1280,720))
#ui = pygame.Surface(())
ui = pygame.image.load('graphics/charUI.png')
ui = ui.convert_alpha()
ui = pygame.transform.scale(ui,(275,90))
#blackFadeScreen.fill((255,255,255))
#blackFadeScreen.setAlpha()
done = False
framerate = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
 
    hasKey= False

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('graphics/character.png')
        self.surf = pygame.transform.scale(self.surf,(76,112))
        self.animation_speed = 10
        self.animation_speed = self.animation_speed
        self.rect = self.surf.get_rect()
        self.rect.move_ip(600,400) #player spawn point
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

######## this converts all the colors or something which increases performance############
        for i in range(0,4):
            self.walk_up_ani[i] = self.walk_up_ani[i].convert_alpha()
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
            self.walk_down_ani[i] = self.walk_down_ani[i].convert_alpha()

        #self.noi = 4
        self.current_frame = 0
        self.time = 0
        self.isCasting = False
        self.manaTime = 0


    def update(self, pressed_keys):
###########auto mana regen over time####################
        self.manaTime += 1
        if (self.manaTime % 60 == 0 and self.mana < 34):
            self.mana += self.mana_regen

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
            self.downspeed = 4
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

        elif pressed_keys[pygame.K_2]:
            if (self.mana >= 5 and self.isCasting==False):
                #cast spell here
                self.isCasting = True
                self.mana = self.mana - 5

#########this makes it so you only cast once per keypress##########
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                self.isCasting = False




    speed = 4
    leftspeed = 4
    rightspeed =4
    downspeed =4
    upspeed =4
    x = 640
    y = 350
    health = 34#34 is max health, or 170pixels/5
    mana = 20
    mana_regen = 1
    direction = 1





class Slime(pygame.sprite.Sprite):
    seenPlayer = False
    direction = 1
    def __init__(self):
        self.surf = pygame.image.load('graphics/slime1.png')
        self.surf = pygame.transform.scale(self.surf,(84,88))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(800,400)
        self.animation_speed = 10
        #self.walk_up_ani = [pygame.transform.scale(pygame.image.load('slime1.png'),(92,124)),
         #   pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
          #  pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
           # pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124))]
        self.walk_left_ani = [pygame.transform.scale(pygame.image.load('graphics/slimeleftF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF4.png'),(92,124))]
        self.walk_right_ani = [pygame.transform.scale(pygame.image.load('graphics/slimerightF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF4.png'),(92,124))]
        #self.walk_down_ani = [pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
         #   pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
          #  pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124)),
           # pygame.transform.scale(pygame.image.load('graphics/slime1.png'),(92,124))]
        for i in range(0,4):
            #self.walk_up_ani[i] = self.walk_up_ani[i].convert_alpha()
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
            #self.walk_down_ani[i] = self.walk_down_ani[i].convert_alpha()

        
        self.current_frame = 0
        self.time = 0
    
    def moveLeft(self):
        self.leftspeed = 2
        self.rect.move_ip(-self.leftspeed, 0)
        self.time += 1
        if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1
        self.surf = self.walk_left_ani[self.current_frame]
    
    def moveRight(self):
        self.rightspeed = 2
        self.rect.move_ip(self.rightspeed, 0)
        self.time += 1
        if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1
        self.surf = self.walk_right_ani[self.current_frame]
        
    def update(self):
        if self.direction == 0:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight2)):
                self.direction = 1
            else:
                self.moveRight()
        if self.direction == 1:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft2)):
                self.direction = 0
            else:
                self.moveLeft()
                
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)

class Room1:
    roomimage = pygame.image.load('graphics/room2.png')
    roomimage = roomimage.convert()
    roomimage = pygame.transform.scale(roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,720)
    wallLeft2 = Wall(0,0,0,0)
    wallRight1 = Wall(1180,0,100,240)
    wallRight2 = Wall(1180,420,100,160)
    wallTop1 = Wall(0,0,570,50)
    wallTop2 = Wall(720,0,560,50)
    wallBottom1 = Wall(0,600,1280,60)
    wallBottom2 = Wall(0,0,0,0)
    wallMiddle = Wall(300,0,180,330)
    wallMiddle2 = Wall(0,0,0,0)
    wallMiddle3 = Wall(0,0,0,0)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(0,0,0,0)
    rightDoor = Wall(1200,240,100,180)
    leftDoor = Wall(0,0,0,0)


class Room2:
    def __init__(self):
        self.roomimage = pygame.image.load('graphics/room4.png')
        self.roomimage = self.roomimage.convert()
        self.roomimage = pygame.transform.scale(self.roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,720)
    wallLeft2 = Wall(0,0,0,0)
    wallRight1 = Wall(1180,0,100,240)
    wallRight2 = Wall(1180,420,100,160)
    wallTop1 = Wall(0,0,1280,50)
    wallTop2 = Wall(0,0,0,0)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(310,300,160,130)
    wallMiddle2 = Wall(790,300,160,130)
    wallMiddle3 = Wall(0,0,0,0)
    topDoor = Wall(0,0,0,0)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(1180,240,100,180)
    leftDoor = Wall(0,0,0,0)

class Room3:
    def __init__(self):
        self.roomimage = pygame.image.load('graphics/room5.png')
        self.roomimage = self.roomimage.convert()
        self.roomimage = pygame.transform.scale(self.roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,240)
    wallLeft2 = Wall(0,420,100,160)
    wallRight1 = Wall(1180,0,100,720)
    wallRight2 = Wall(0,0,0,0)
    wallTop1 = Wall(0,0,570,50)
    wallTop2 = Wall(720,0,560,50)
    wallBottom1 = Wall(0,600,1280,60)
    wallBottom2 = Wall(0,0,0,0)
    wallMiddle = Wall(0,0,0,0)
    wallMiddle2 = Wall(0,0,0,0)
    wallMiddle3 = Wall(0,0,0,0)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(0,0,0,0)
    rightDoor = Wall(0,0,0,0)
    leftDoor = Wall(0,240,70,180)

class Key(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load('graphics/bosskey.png')
        self.surf = pygame.transform.scale(self.surf,(28,64)) 
        self.rect = self.surf.get_rect()
        self.rect.move_ip(600,400)
        
class Room4:
    def __init__(self):
        self.roomimage = pygame.image.load('graphics/room6.png')
        self.roomimage = self.roomimage.convert()
        self.roomimage = pygame.transform.scale(self.roomimage,(1280,720))
    key = Key()
    wallLeft1 = Wall(0,0,100,240)
    wallLeft2 = Wall(0,420,100,160)
    wallRight1 = Wall(1180,0,100,720)
    wallRight2 = Wall(0,0,0,0)
    wallTop1 = Wall(0,0,570,50)
    wallTop2 = Wall(720,0,560,50)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(0,0,0,0)
    wallMiddle2 = Wall(0,0,0,0)
    wallMiddle3 = Wall(0,0,0,0)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(0,0,0,0)
    leftDoor = Wall(0,240,70,180)



class Bossroom:
    def __init__(self):
        self.roomimage = pygame.image.load('graphics/bossroom3.png')
        self.roomimage = self.roomimage.convert()
        self.roomimage = pygame.transform.scale(self.roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,720)
    wallLeft2 = Wall(0,0,0,0)
    wallRight1 = Wall(1180,0,100,720)
    wallRight2 = Wall(0,0,0,0)
    wallTop1 = Wall(0,0,1280,50)
    wallTop2 = Wall(0,0,0,0)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(0,200,460,110)
    wallMiddle2 = Wall(800,200,500,110)
    wallMiddle3 = Wall(460,100,400,110)
    topDoor = Wall(0,0,0,0)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(0,0,0,0)
    leftDoor = Wall(0,0,0,0)
    
    

#use this to update the current room when changing rooms
#def updateCurrentRoom(room):
    #currentroom = room
def changeRooms(roomName):
    timer = 0
    global currentroom
    currentroom = roomName
    #blackFadeScreen.set_alpha(0)
    #screen.blit(blackFadeScreen,(0,0))
    #while timer < 2550:
        #timer+=1
        #print(timer)
        #blackFadeScreen.set_alpha(timer%10)
        #blackFadeScreen.set_alpha(100)
        #screen.blit(blackFadeScreen,(0,0))


fadeAlpha = 1

def checkCollision(self, sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    return(col)




player = Player()
firstroom = Room1()
secondroom = Room2()
thirdroom = Room3()
fourthroom = Room4()
bossroom = Bossroom()
currentroom = firstroom
bosskey = Key()
slime = Slime()
sprites_alive = pygame.sprite.Group()
sprites_walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()



## add monster sprites to this group to draw them to the screen
sprites_alive.add(player)
#sprites_alive.add(slime)                                  #Causes error, not sure why -------------------------------------------------



sprites_walls.add(firstroom.wallLeft1)
all_sprites.add(sprites_alive,sprites_walls)

fade = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed_keys = pygame.key.get_pressed()

        screen.blit(currentroom.roomimage,(0,0)) #draws the current map/room
        pygame.draw.rect(screen,(255,0,0), (102,25,player.health*5,30),0) #draws the health bar
        pygame.draw.rect(screen,(0,0,255), (102,68,player.mana*5,30),0) #draws the mana bar
        screen.blit (ui,(10,10))#draws the ui to the screen

        for entity in sprites_alive: #this draws the sprites in the sprites_alive group (player and monsters)
            screen.blit(entity.surf, entity.rect)
        if currentroom == firstroom:
            screen.blit(slime.surf,slime.rect)
            
        if currentroom == fourthroom and player.hasKey == False:
            screen.blit(bosskey.surf,bosskey.rect)
            
###############These if statements check for collision with player and walls and if true sets the players speed to 0###############
        #Locks door unless key has been picked up
        if(currentroom == fourthroom):
            if (checkCollision(pygame.sprite.Sprite,player, currentroom.key)):
                player.hasKey = True
        else:
            if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft2)):
                player.leftspeed =0
            if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight2)):
                player.rightspeed =0
            if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop2)):
                player.upspeed = 0
            if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom2)):
                player.downspeed = 0
            if (checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle3)):
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
###############These check for collision with the doors and loads new rooms and moves player#####################
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.topDoor)):
            if (currentroom == firstroom):
                changeRooms(secondroom)
                player.rect.move_ip(0,500)
            elif (currentroom == thirdroom):
                changeRooms(fourthroom)
                player.rect.move_ip(0,500)
            
            elif (currentroom == fourthroom and player.hasKey == True):
                changeRooms(bossroom)
                player.rect.move_ip(0,500)
            elif (currentroom == fourthroom and player.hasKey == False):
                player.upspeed = 0
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.bottomDoor)):
            if (currentroom == secondroom):
                changeRooms(firstroom)
            elif (currentroom == fourthroom):
                changeRooms(thirdroom)
            elif (currentroom == bossroom):
                changeRooms(fourthroom)
            player.rect.move_ip(0,-500)
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.rightDoor)):
            if (currentroom == firstroom):
                changeRooms(thirdroom)
            elif (currentroom == secondroom):
                changeRooms(fourthroom)
            player.rect.move_ip(-1030,0)
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.leftDoor)):
            if (currentroom == thirdroom):
                changeRooms(firstroom)
            elif (currentroom == fourthroom):
                changeRooms(secondroom)
            player.rect.move_ip(1020,0)

        player.update(pressed_keys) ###this calls the update method in player which checks for keypresses and handles movement/attacks
        slime.update()
        #use the following for collision detection between player and enemies
        #if pygame.sprite.spritecollideany(player, enemies):
            #player takes damage and is pushed back?

        ##(102, 25) for health bar
        ##(102, 68) for mana bar


        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
