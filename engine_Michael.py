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
icenovaicon = pygame.image.load('graphics/icenovaicon.png')
icenovaicon = icenovaicon.convert()
icenovaicon = pygame.transform.scale(icenovaicon,(80,76))
icenovaicongrey = pygame.image.load('graphics/icenovaicongrey.png')
icenovaicongrey = icenovaicongrey.convert()
icenovaicongrey = pygame.transform.scale(icenovaicongrey,(80,76))
#blackFadeScreen.fill((255,255,255))
#blackFadeScreen.setAlpha()
done = False
framerate = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('graphics/player_walking_downF1.png')
        self.surf = pygame.transform.scale(self.surf,(92,124))
        self.animation_speed = 10
        self.animation_speed = self.animation_speed
        self.rect = self.surf.get_rect()
        self.rect = self.rect.inflate(-5,-30)
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
        self.cast_ice_ani = [pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF4.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF5.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF6.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF7.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF8.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_cast_iceF9.png'),(92,124))]

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
        self.fallingTime = 0
        self.falling = False
        self.hasKey = False
        self.castingTime = 0
        self.frameOn = 0
        self.castingIceNova = False
        self.icenovacooldown = 0
        self.startCountingCooldown = False


    def update(self, pressed_keys):
        if (self.falling == False and self.fallingTime > 0):
            self.fallingTime = 0
###########auto mana regen over time####################
        self.manaTime += 1
        if (self.manaTime % 60 == 0 and self.mana < 34):
            self.mana += self.mana_regen
########## handles spell cooldowns #################
        if (self.startCountingCooldown == True):
            self.icenovacooldown +=1
            if (self.icenovacooldown % 400 == 0):
                self.startCountingCooldown = False
                self.icenovacooldown = 0
############starts the cast animation##############
        if (self.isCasting == True):
            self.castingTime += 1
            if (self.castingTime % 8 == 0):
                if (self.frameOn < 7):
                    self.surf = self.cast_ice_ani[self.frameOn]
                    self.frameOn +=1
                elif (self.frameOn == 7):
                    icenova.surf = icenova.animation[0]
                    self.castingIceNova = True
                    self.surf = self.cast_ice_ani[self.frameOn]
                    self.frameOn +=1
                elif (self.frameOn >7 and self.frameOn <9):
                    self.surf = self.cast_ice_ani[self.frameOn]
                    self.frameOn +=1
                else:
                    self.frameOn = 0
                    self.isCasting = False
                    self.castingTime = 0
                    self.surf = self.walk_down_ani[0]
######### walking up animation ##############
        if pressed_keys[pygame.K_UP]:
            if (self.isCasting == False):
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
            if (self.isCasting == False):
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
            if (self.isCasting == False):
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
            if (self.isCasting == False):
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

        elif pressed_keys[pygame.K_3]:
            if (self.isCasting == False and self.startCountingCooldown == False and self.mana >= 10):#(self.mana >= 10 and self.isCasting ==False):
                xdistance = self.rect.x - icenova.rect.x - 150
                ydistance = self.rect.y -icenova.rect.y - 105
                icenova.rect.move_ip(xdistance, ydistance)
                self.startCountingCooldown = True
                self.mana -= 10
                #self.castingIceNova = True
                self.isCasting = True




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
    #direction = 1
    def __init__(self):
        super(Slime, self).__init__()
        self.surf = pygame.image.load('graphics/slime1.png')
        self.surf = pygame.transform.scale(self.surf,(84,88))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(800,400)
        self.animation_speed = 10
        self.walk_left_ani = [pygame.transform.scale(pygame.image.load('graphics/slimeleftF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF4.png'),(68,60))]
        self.walk_right_ani = [pygame.transform.scale(pygame.image.load('graphics/slimerightF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF4.png'),(68,60))]
        self.frozen_right = pygame.transform.scale(pygame.image.load('graphics/slimefrozenright.png'),(68,60))
        self.frozen_left = pygame.transform.scale(pygame.image.load('graphics/slimefrozenleft.png'),(68,60))
        for i in range(0,4):
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
        self.frozen_right = self.frozen_right.convert_alpha()
        self.frozen_left = self.frozen_left.convert_alpha()
        
        self.direction = 0
        self.current_frame = 0
        self.time = 0
        self.frozen = False
        self.speed = 2
        self.frozenCounter = 0
        self.distance = 50
        self.newInstruction = False
    

    def moveLeft(self):
        self.leftspeed = self.speed
        self.rect.move_ip(-self.leftspeed, 0)
        self.time += 1
        if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1
        self.surf = self.walk_left_ani[self.current_frame]

    def moveRight(self):
        self.rightspeed = self.speed
        self.rect.move_ip(self.rightspeed, 0)
        self.time += 1
        if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1
        self.surf = self.walk_right_ani[self.current_frame]

    def moveUp(self):
        self.rect.move_ip(0, -self.speed)
        self.time += 1
        if (self.time % 12 == 0):
            if(self.current_frame>2):
                self.current_frame = 0
            else:
                self.current_frame+=1
        self.surf = self.walk_left_ani[self.current_frame]
        
    def moveDown(self):
        self.rect.move_ip(0, self.speed)
        self.time += 1
        if (self.time % 12 == 0):
            if(self.current_frame>2):
                self.current_frame = 0
            else:
                self.current_frame+=1

        self.surf = self.walk_right_ani[self.current_frame]

    def update(self):
        if self.frozen == False:
            self.distance -=1
        print (self.distance)
        if self.direction == 0:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight2)) or (checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle3)):
                print("WALL")
                self.newInstruction = True
            else:
                self.moveRight()
                
        if self.direction == 1:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallTop2)) or (checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle3)):
                print("WALL")
                self.newInstruction = True
            else: 
                self.moveUp()
        
        if self.direction == 2:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft2)) or (checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle3)):
                print("WALL")
                self.newInstruction = True
            else:
                self.moveLeft()
                
        if self.direction == 3:
            if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallBottom2)) or (checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle3)):
                #print("WALL")
                self.newInstruction = True
            else:
                self.moveDown()
        
        if self.distance == 0:
            self.newInstruction = True
            #print("Change")
        
        if self.frozen == True:
            if (self.direction == 0):
                self.surf = self.frozen_right
            else: 
                self.surf = self.frozen_left
            self.frozenCounter +=1
            if (self.frozenCounter == 10):
                self.frozen = False
                self.frozenCounter = 0
                self.speed = 1
        if (self.newInstruction == True):
            #directionList = [0,1,2,3]                 
            #directionList.remove(self.direction)          #These two lines make it so the same direction can't be chosen twice
            self.distance = random.randint(100,200)
            self.direction = random.choice(directionList)
            self.newInstruction = False
                

class Key(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load('graphics/bosskey.png')
        self.surf = pygame.transform.scale(self.surf,(28,64))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(1100,200)

class IceNova(pygame.sprite.Sprite):
    def __init__(self):
        super(IceNova, self).__init__()
        self.surf = pygame.image.load('graphics/icenova0.png')
        self.surf = pygame.transform.scale(self.surf,(392,392))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(400,200) #player spawn point
        self.animation = [pygame.transform.scale(pygame.image.load('graphics/icenova0.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova1.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova2.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova3.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova4.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova5.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova6.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova7.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova8.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova6.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova7.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova9.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova10.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova11.png'),(392,392)),
            pygame.transform.scale(pygame.image.load('graphics/icenova12.png'),(392,392))]
            #pygame.image.load('graphics/blank.png')]
        for i in range(0,13):
            self.animation[i] = self.animation[i].convert_alpha()

        self.frameOn = 0
        self.castingTime = 0
        self.counter = 0
        self.canFreeze = False
    def update(self):
############starts the animation##############
        self.castingTime += 1
        if (self.castingTime % 7 == 0):
            self.canFreeze = True
            #if (self.frameOn == 0):
            if (self.frameOn < 7):
                self.frameOn +=1
                self.surf = self.animation[self.frameOn]

            elif(self.frameOn >6 and self.frameOn < 12):
                
                self.counter +=1
                if (self.counter % 5 == 0):
                    self.surf = self.animation[self.frameOn]
                    self.frameOn +=1

            elif(self.frameOn >11 and self.frameOn <15):
                self.surf = self.animation[self.frameOn]
                self.frameOn +=1
            else:
                self.frameOn = 0
                self.castingTime = 0
                self.counter = 0
                player.castingIceNova = False
                self.canFreeze = False
                #self.surf = null#self.animation[self.frameOn]

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,width,height)

class room1:
    roomimage = pygame.image.load('graphics/room2.png')
    roomimage = roomimage.convert()
    roomimage = pygame.transform.scale(roomimage,(1280,720))
    #roomfloor = pygame.image.load('graphics/floor2b.png')
    #roomfloor= roomfloor.convert()
    #roomfloor = pygame.transform.scale(roomfloor,(1280,720))
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
    wallMiddle4 = Wall(0,0,0,0)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(0,0,0,0)
    rightDoor = Wall(1200,240,100,180)
    leftDoor = Wall(0,0,0,0)


class Room2:
    def __init__(self,imagepath):
        self.roomimage = pygame.image.load(imagepath)
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
    wallMiddle4 = Wall(0,0,0,0)
    topDoor = Wall(0,0,0,0)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(1180,240,100,180)
    leftDoor = Wall(0,0,0,0)

class Room3:
    def __init__(self,imagepath):
        self.roomimage = pygame.image.load(imagepath)
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
    wallMiddle = Wall(100,50,350,150)
    wallMiddle2 = Wall(100,430,350,300)
    wallMiddle3 = Wall(820,50,200,350)
    wallMiddle4 = Wall(900,50,500,160)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(0,0,0,0)
    rightDoor = Wall(0,0,0,0)
    leftDoor = Wall(0,240,70,180)


class Room4:
    def __init__(self,imagepath):
        self.roomimage = pygame.image.load(imagepath)
        self.roomimage = self.roomimage.convert()
        self.roomimage = pygame.transform.scale(self.roomimage,(1280,720))
    wallLeft1 = Wall(0,0,100,240)
    wallLeft2 = Wall(0,420,100,160)
    wallRight1 = Wall(1180,0,100,720)
    wallRight2 = Wall(0,0,0,0)
    wallTop1 = Wall(0,0,570,50)
    wallTop2 = Wall(720,0,560,50)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(500,50,70,70)
    wallMiddle2 = Wall(700,50,65,75)
    wallMiddle3 = Wall(990,400,60,30)
    wallMiddle4 = Wall(0,0,0,0)
    topDoor = Wall(570,0,150,10)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(0,0,0,0)
    leftDoor = Wall(0,240,70,180)

class Bossroom:
    def __init__(self,imagepath):
        self.roomimage = pygame.image.load(imagepath)
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
    wallMiddle4 = Wall(0,0,0,0)
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


icenova = IceNova()
slime1 = Slime()
player = Player()
firstroom = room1()
bosskey = Key()
secondroom = Room2('graphics/room4.png')
thirdroom = Room3('graphics/room5b.png')
fourthroom = Room4('graphics/room6.png')
bossroom = Bossroom('graphics/bossroom3.png')
currentroom = firstroom
sprites_alive = pygame.sprite.Group()
sprites_walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

## add monster sprites to this group to draw them to the screen
sprites_alive.add(player)
sprites_alive.add(slime1)
#sprites_alive.add(icenova)


sprites_walls.add(firstroom.wallLeft1)
all_sprites.add(sprites_alive,sprites_walls)

fade = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        pressed_keys = pygame.key.get_pressed()

        screen.blit(currentroom.roomimage,(0,0))

        if (player.castingIceNova == True):
            icenova.update()
            screen.blit(icenova.surf,icenova.rect)

####### drawing spell icons #################################
        if (player.startCountingCooldown == False):
            screen.blit(icenovaicon,(1000,10))
        else :
            screen.blit(icenovaicongrey,(1000,10))

        for entity in sprites_alive: #this draws the sprites in the sprites_alive group (player and monsters)
            screen.blit(entity.surf, entity.rect)


        if currentroom == fourthroom and player.hasKey == False:
            screen.blit(bosskey.surf,bosskey.rect)



        pygame.draw.rect(screen,(255,0,0), (102,25,player.health*5,30),0) #draws the health bar
        pygame.draw.rect(screen,(0,0,255), (102,68,player.mana*5,30),0) #draws the mana bar
        screen.blit (ui,(10,10))#draws the ui to the screen

###############These if statements check for collision with player and walls and if true sets the players speed to 0###############
        if(currentroom == fourthroom):
            if (checkCollision(pygame.sprite.Sprite,player, bosskey)):
                player.hasKey = True

        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallLeft2)):
            player.leftspeed =0
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight2)):
            player.rightspeed =0
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop2)):
            player.upspeed = 0
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom2)):
            player.downspeed = 0
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle3) or
        checkCollision(pygame.sprite.Sprite, player, currentroom.wallMiddle4)):
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
            if (currentroom == thirdroom and player.direction == 1):
                player.upspeed = 0
                player.rect.move_ip(0,-2)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.upspeed = 4
            if (currentroom == thirdroom and player.direction == 4):
                player.upspeed = 0
                player.rect.move_ip(-2,0)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.leftspeed = 4
            if (currentroom == thirdroom and player.direction == 2):
                player.upspeed = 0
                player.rect.move_ip(2,0)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.rightspeed = 4
            if (currentroom == thirdroom and player.direction == 3):
                player.upspeed = 0
                player.rect.move_ip(0,2)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.downspeed = 4

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

            
################Spell collision with slime ###########################
        if (checkCollision(pygame.sprite.Sprite, icenova, slime1)):
            if (icenova.canFreeze == True):
                slime1.frozen = True
                slime1.speed = 0
            
############### Player Collision with slime ##########################
        if (checkCollision(pygame.sprite.Sprite, player,slime1)):
            if (slime1.frozen == True):
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
            
        player.update(pressed_keys) ###this calls the update method in player which checks for keypresses and handles movement/attacks
        slime1.update()
        #use the following for collision detection between player and enemies
        #if pygame.sprite.spritecollideany(player, enemies):
            #player takes damage and is pushed back?

        ##(102, 25) for health bar
        ##(102, 68) for mana bar


        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
