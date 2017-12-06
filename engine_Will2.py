#Main engine
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
#blackFadeScreen = pygame.Surface((1280,720))
#blackFadeScreen = pygame.Rect(0,0,1280,720)
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
fireballicon = pygame.image.load('graphics/fireballicon.png')
fireballicon = fireballicon.convert()
fireballicon = pygame.transform.scale(fireballicon,(80,76))
fireballicongrey = pygame.image.load('graphics/fireballicongrey.png')
fireballicongrey = fireballicongrey.convert()
fireballicongrey = pygame.transform.scale(fireballicongrey,(80,76))
lightningicon = pygame.image.load('graphics/lightningicon.png')
lightningicon = lightningicon.convert()
lightningicon = pygame.transform.scale(lightningicon,(80,76))
lightningicongrey = pygame.image.load('graphics/lightningicongrey.png')
lightningicongrey = lightningicongrey.convert()
lightningicongrey = pygame.transform.scale(lightningicongrey,(80,76))
#blackFadeScreen.fill((255,255,255))
#blackFadeScreen.setAlpha()
done = False
framerate = pygame.time.Clock()
key_room = random.randint(2,4)
key_slime = random.randint(1,2)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('graphics/player_walking_downF1.png')
        self.surf = pygame.transform.scale(self.surf,(92,124))
        #self.surf = #offset x and y
        self.animation_speed = 10
        self.animation_speed = self.animation_speed
        self.rect = self.surf.get_rect()# self.surf.get_rect(width = 50, height= 90)
        #self.rect = self.rect.inflate(20, 40)
        #self.rect.center = (self.x+20,self.y+20)
        self.hitbox = pygame.Rect(self.rect.x+25,self.rect.y+55,50,65)
        #self.rect = pygame.Rect(0,0,50,90)#self.surf.get_rect()
        #self.rect = self.rect.inflate(-5,-30)
        self.rect.move_ip(600,400) #player spawn point
        self.hitbox.move_ip(self.rect.x,self.rect.y)


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
        self.cast_fireball_down_ani = [pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF4.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF5.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF6.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_downF7.png'),(92,124)),]
        self.cast_fireball_up_ani = [pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF1.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF2.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF3.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF4.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF5.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF6.png'),(92,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_upF7.png'),(92,124)),]
        self.cast_fireball_left_ani = [pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF1.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF2.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF3.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF4.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF5.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF6.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_leftF7.png'),(100,124)),]
        self.cast_fireball_right_ani = [pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF1.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF2.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF3.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF4.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF5.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF6.png'),(100,124)),
            pygame.transform.scale(pygame.image.load('graphics/player_fireball_rightF7.png'),(100,124)),]

######## this converts all the colors or something which increases performance############
        for i in range(0,4):
            self.walk_up_ani[i] = self.walk_up_ani[i].convert_alpha()
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
            self.walk_down_ani[i] = self.walk_down_ani[i].convert_alpha()
        for i in range(0,8):
            self.cast_ice_ani[i] = self.cast_ice_ani[i].convert_alpha()
        for i in range(0,6):
            self.cast_fireball_down_ani[i] = self.cast_fireball_down_ani[i].convert_alpha()
            self.cast_fireball_up_ani[i] = self.cast_fireball_up_ani[i].convert_alpha()
            self.cast_fireball_left_ani[i] = self.cast_fireball_left_ani[i].convert_alpha()
            self.cast_fireball_right_ani[i] = self.cast_fireball_right_ani[i].convert_alpha()

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
        self.fireballcooldown = 0
        self.fireCountingCooldown = False
        self.startCountingCooldown = False
        self.isCastingIce = False
        self.isCastingFire = False
        self.castingFireball = False
        self.spawnFireball = False
        self.invulnerable = False
        self.godTimer = 0


    def update(self, pressed_keys):
######### makes it so player can only be hit once every second ############
        if (self.invulnerable == True):
            self.surf
            self.godTimer +=1
            if (self.godTimer >= 80):
                self.invulnerable = False
                self.godTimer = 0


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

        if (self.fireCountingCooldown == True):
            self.fireballcooldown +=1
            if (self.fireballcooldown % 100 == 0):
                self.fireCountingCooldown = False
                self.fireballcooldown = 0
############starts the cast for ICENOVA animation##############
        if (self.isCastingIce == True):
            self.castingTime += 1
            if (self.castingTime % 5 == 0):
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
                    self.isCastingIce = False
                    self.isCasting = False
                    self.castingTime = 0
                    self.surf = self.walk_down_ani[0]
############# starts cast for fireball #####################
        if (self.isCastingFire == True):
            self.castingTime+=1
            if (self.castingTime %5 == 0):
                if (self.frameOn < 7):
                    if (self.direction == 1):
                        self.surf = self.cast_fireball_up_ani[self.frameOn]
                        self.frameOn +=1
                    elif (self.direction == 2):
                        self.surf = self.cast_fireball_right_ani[self.frameOn]
                        self.frameOn +=1
                    elif (self.direction == 3):
                        self.surf = self.cast_fireball_down_ani[self.frameOn]
                        self.frameOn +=1
                    if (self.direction == 4):
                        self.surf = self.cast_fireball_left_ani[self.frameOn]
                        self.frameOn +=1
                elif (self.frameOn >= 7):
                    #fireball.surf = fireball.animation[0]
                    #self.castingFireball = True
                    self.fireCountingCooldown == True
                    self.frameOn = 0
                    self.isCastingFire = False
                    self.isCasting = False
                    self.spawnFireball = True
                    fireball.isActive = True
                    self.castingTime = 0
                    if (self.direction == 1):
                        fireball.direction = 1
                        self.surf = self.walk_up_ani[0]
                    elif (self.direction == 2):
                        fireball.direction = 2
                        self.surf = self.walk_right_ani[0]
                    elif (self.direction == 3):
                        fireball.direction = 3
                        self.surf = self.walk_down_ani[0]
                    if (self.direction == 4):
                        fireball.direction = 4
                        self.surf = self.walk_left_ani[0]


######### walking up animation ##############
        if pressed_keys[pygame.K_UP]:
            if (self.isCasting == False):
                self.leftspeed = 4
                self.rightspeed = 4
                self.downspeed = 4
                self.direction = 1
                self.rect.move_ip(0, -self.upspeed)
                self.hitbox.move_ip(0, -self.upspeed)
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
                self.hitbox.move_ip(0, self.downspeed)
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
                self.hitbox.move_ip(-self.leftspeed, 0)
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
                self.hitbox.move_ip(self.rightspeed, 0)
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
                self.isCastingIce = True
                self.isCasting = True
        elif pressed_keys[pygame.K_1]:
            if (self.isCasting == False and self.fireCountingCooldown == False and self.mana >= 10):# and fireball.isActive == False):#(self.mana >= 10 and self.isCasting ==False):
                if (self.direction == 1):
                    xdistance = self.rect.x - fireball.rect.x + 60
                    ydistance = self.rect.y -fireball.rect.y +20
                    fireball.rect.move_ip(xdistance, ydistance)
                elif (self.direction ==2):
                    xdistance = self.rect.x - fireball.rect.x + 30
                    ydistance = self.rect.y -fireball.rect.y + 55
                    fireball.rect.move_ip(xdistance, ydistance)
                elif (self.direction ==3):
                    xdistance = self.rect.x - fireball.rect.x
                    ydistance = self.rect.y -fireball.rect.y + 20
                    fireball.rect.move_ip(xdistance, ydistance)
                elif (self.direction ==4):
                    xdistance = self.rect.x - fireball.rect.x - 30
                    ydistance = self.rect.y -fireball.rect.y +30
                    fireball.rect.move_ip(xdistance, ydistance)
                #self.mana -= 5
                self.isCastingFire = True
                self.isCasting = True
                self.fireCountingCooldown = True




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
    def __init__(self, x, y):
        super(Slime, self).__init__()
        self.surf = pygame.image.load('graphics/slime1.png')
        self.surf = pygame.transform.scale(self.surf,(84,88))
        self.rect = pygame.Rect(0,0,70,70)
        self.hitbox = pygame.Rect(self.rect.x+8,self.rect.y+21,50,35)
        #self.rect = self.surf.get_rect()
        self.rect.move_ip(x,y)
        self.hitbox.move_ip(self.rect.x,self.rect.y)
        self.animation_speed = 10
        self.walk_left_ani = [pygame.transform.scale(pygame.image.load('graphics/slimeleftF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimeleftF4.png'),(68,60))]
        self.walk_right_ani = [pygame.transform.scale(pygame.image.load('graphics/slimerightF1.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF2.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF3.png'),(68,60)),
            pygame.transform.scale(pygame.image.load('graphics/slimerightF4.png'),(68,60))]
        self.death_ani = [pygame.transform.scale(pygame.image.load('graphics/slimedeathF1.png'),(100,92)),
            pygame.transform.scale(pygame.image.load('graphics/slimedeathF2.png'),(100,92)),
            pygame.transform.scale(pygame.image.load('graphics/slimedeathF3.png'),(100,92)),
            pygame.transform.scale(pygame.image.load('graphics/slimedeathF4.png'),(100,92)),
            pygame.transform.scale(pygame.image.load('graphics/slimedeathF5.png'),(100,92))]
        self.frozen_right = pygame.transform.scale(pygame.image.load('graphics/slimefrozenright.png'),(68,60))
        self.frozen_left = pygame.transform.scale(pygame.image.load('graphics/slimefrozenleft.png'),(68,60))
        for i in range(0,4):
            self.walk_left_ani[i] = self.walk_left_ani[i].convert_alpha()
            self.walk_right_ani[i] = self.walk_right_ani[i].convert_alpha()
            self.death_ani[i] = self.death_ani[i].convert_alpha()
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
        self.isAlive = True
        self.isDying = False
        self.dyingtime = 0


    def moveLeft(self):
        self.leftspeed = self.speed
        self.rect.move_ip(-self.leftspeed, 0)
        self.hitbox.move_ip(-self.leftspeed, 0)
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
        self.hitbox.move_ip(self.rightspeed, 0)
        self.time += 1
        if (self.time % 12 == 0):
                if(self.current_frame>2):
                    self.current_frame = 0
                else:
                    self.current_frame+=1
        self.surf = self.walk_right_ani[self.current_frame]

    def moveUp(self):
        self.upspeed = self.speed
        self.rect.move_ip(0, -self.speed)
        self.hitbox.move_ip(0, -self.speed)
        self.time += 1
        if (self.time % 12 == 0):
            if(self.current_frame>2):
                self.current_frame = 0
            else:
                self.current_frame+=1
        self.surf = self.walk_left_ani[self.current_frame]

    def moveDown(self):
        self.downspeed = self.speed
        self.rect.move_ip(0, self.speed)
        self.hitbox.move_ip(0, self.speed)
        self.time += 1
        if (self.time % 12 == 0):
            if(self.current_frame>2):
                self.current_frame = 0
            else:
                self.current_frame+=1

        self.surf = self.walk_right_ani[self.current_frame]
    ############slime chase function#############
    def chase(self, player_rect):
        c = math.sqrt((player_rect.x - self.rect.x) ** 2 + (player_rect.y - self.rect.y)**2)
        try:
            x = (player_rect.x - self.rect.x) /c
            y = (player_rect.y - self.rect.y)/c
        except ZeroDivisionError:
            return False
        return(x,y)


###### this resets slime and spawns it when changing rooms##########
    def spawn(self, posx, posy):
        if (self.isSpawning == True):
            self.current_frame = 0
            distx = posx - self.rect.x
            disty = posy - self.rect.y
            self.rect.move_ip(distx,disty)
            self.hitbox.move_ip(distx,disty)
            self.isSpawning = False
        self.isAlive = True
        #self.isSpawning = False



    def update(self):
        ########The following three lines enable the slime chase function#############
        #new_pos = self.chase(player.hitbox)
        #if new_pos :
            #self.rect.x, self.rect.y = (self.rect.x + new_pos[0] * self.speed, self.rect.y + new_pos[1] * self.speed)


        if (self.frozen == False):
            self.distance -=1
        if (self.isAlive == True):
            if self.direction == 0:
                if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallRight2)or checkCollision(pygame.sprite.Sprite, self,currentroom.rightDoor)):
                    self.direction = 1
                else:
                    self.moveRight()
            elif self.direction == 1:
                if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallLeft2) or checkCollision(pygame.sprite.Sprite, self,currentroom.leftDoor)):
                    self.direction = 0
                else:
                    self.moveLeft()
            elif self.direction == 2:
                if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallTop2) or checkCollision(pygame.sprite.Sprite, self,currentroom.topDoor)):
                    self.direction = 3
                else:
                    self.moveUp()
            elif self.direction == 3:
                if (checkCollision(pygame.sprite.Sprite, self,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, self,currentroom.wallBottom2) or checkCollision(pygame.sprite.Sprite, self,currentroom.bottomDoor)):
                    self.direction = 2
                else:
                    self.moveDown()

        elif (self.isAlive == False):
            if (self.isDying == True):
                self.dyingtime += 1
                if (self.dyingtime % 7 == 0):
                    if(self.current_frame>3):
                        self.isDying = False
                        self.dyingtime = 0
                    else:
                        self.current_frame+=1
                self.surf = self.death_ani[self.current_frame]

        if (checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle2) or checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle3) or
        checkCollision(pygame.sprite.Sprite, self, currentroom.wallMiddle4)):
            if (self.direction == 1):
                self.direction = 0
            elif (self.direction==2):
                self.direction = 3
            elif (self.direction==3):
                self.direction = 2
            elif (self.direction ==0):
                self.direction = 1


        if self.distance == 0:
            self.newInstruction = True

        if (self.frozen == True and self.isAlive == True):
            if (self.direction == 0):
                self.surf = self.frozen_right
            else:
                self.surf = self.frozen_left
            self.frozenCounter +=1
            if (self.frozenCounter == 10):
                self.frozen = False
                self.frozenCounter = 0
                self.speed = 2
        if (self.newInstruction ==True):
            self.distance = random.randint(100,200)
            self.direction = random.randint(0,3)
            self.newInstruction = False


class Key(pygame.sprite.Sprite):
    def __init__(self, roomnum, slimenum):
        super(Key, self).__init__()
        self.surf = pygame.image.load('graphics/bosskey.png')
        self.surf = pygame.transform.scale(self.surf,(28,64))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(1100,200)
        self.room = roomnum
        self.slimenum = slimenum
    def update(self, slimerect):
        distx = slimerect.x - self.rect.x +25
        disty = slimerect.y - self.rect.y
        self.rect.move_ip(distx,disty)

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

class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super(Fireball, self).__init__()
        self.surf = pygame.image.load('graphics/fireballD1.png')
        self.surf = pygame.transform.scale(self.surf,(68,60))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(400,200)
        self.down_ani = [pygame.transform.scale(pygame.image.load('graphics/fireballD1.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballD2.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballD3.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballD4.png'),(32,76))]
        self.left_ani = [pygame.transform.scale(pygame.image.load('graphics/fireballL1.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballL2.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballL3.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballL4.png'),(76,32))]
        self.up_ani = [pygame.transform.scale(pygame.image.load('graphics/fireballU1.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballU2.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballU3.png'),(32,76)),
            pygame.transform.scale(pygame.image.load('graphics/fireballU4.png'),(32,76))]
        self.right_ani = [pygame.transform.scale(pygame.image.load('graphics/fireballR1.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballR2.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballR3.png'),(76,32)),
            pygame.transform.scale(pygame.image.load('graphics/fireballR4.png'),(76,32))]

        self.frameOn = 0
        self.castingTime = 0
        self.counter = 0
        self.direction = 1
        self.isActive = False

    def update(self):
        if (self.isActive == True):
            self.castingTime += 1
            if (self.castingTime % 7 == 0):
                if (self.frameOn < 3):
                    self.frameOn +=1
                else : self.frameOn = 0
            if (self.direction == 1):
                self.surf = self.up_ani[self.frameOn]
                self.rect.move_ip(0,-7)
            elif (self.direction == 2):
                self.surf = self.right_ani[self.frameOn]
                self.rect.move_ip(7,0)
            elif (self.direction == 3):
                self.surf = self.down_ani[self.frameOn]
                self.rect.move_ip(0,7)
            elif (self.direction == 4):
                self.surf = self.left_ani[self.frameOn]
                self.rect.move_ip(-7,0)
        if (self.castingTime >=60):
            #player.firecountingCooldown = False
            self.isActive = False
            player.spawnFireball = False
            self.castingTime = 0
            self.rect.move_ip(10000,1000)


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
    wallTop1 = Wall(0,0,570,90)
    wallTop2 = Wall(720,0,560,90)
    wallBottom1 = Wall(0,600,1280,60)
    wallBottom2 = Wall(0,0,0,0)
    wallMiddle = Wall(300,0,180,370)
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
    wallTop1 = Wall(0,0,1280,90)
    wallTop2 = Wall(0,0,0,0)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(310,300,160,170)
    wallMiddle2 = Wall(790,300,160,170)
    wallMiddle3 = Wall(0,0,0,0)
    wallMiddle4 = Wall(0,0,0,0)
    topDoor = Wall(0,0,0,0)
    bottomDoor = Wall(570,620,150,40)
    rightDoor = Wall(1200,240,100,180)
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
    wallTop1 = Wall(0,0,570,90)
    wallTop2 = Wall(720,0,560,90)
    wallBottom1 = Wall(0,600,1280,60)
    wallBottom2 = Wall(0,0,0,0)
    wallMiddle = Wall(100,50,350,190)
    wallMiddle2 = Wall(100,430,350,340)
    wallMiddle3 = Wall(820,50,200,390)
    wallMiddle4 = Wall(900,50,500,200)
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
    wallTop1 = Wall(0,0,570,90)
    wallTop2 = Wall(720,0,560,90)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(500,50,70,140)
    wallMiddle2 = Wall(700,50,65,135)
    wallMiddle3 = Wall(990,400,60,80)
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
    wallTop1 = Wall(0,0,1280,90)
    wallTop2 = Wall(0,0,0,0)
    wallBottom1 = Wall(0,600,570,50)
    wallBottom2 = Wall(720,600,560,50)
    wallMiddle = Wall(0,200,480,170)
    wallMiddle2 = Wall(800,200,500,170)
    wallMiddle3 = Wall(460,100,400,170)
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
    #pygame.draw.rect(screen,(0,0,0), blackScreenFade, alpha = 0)
    #blackFadeScreen.set_alpha(0)
    #screen.blit(blackFadeScreen,(0,0))
    #while timer < 2550:
        #timer+=1
        #blackFadeScreen.set_alpha(timer%10)
        #blackFadeScreen.set_alpha(100)
        #screen.blit(blackFadeScreen,(0,0))


#fadeAlpha = 1

def checkCollision(self, sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    return(col)

fireball = Fireball()
icenova = IceNova()
slime1 = Slime(800,400)
slime2 = Slime(200,400)
player = Player()
firstroom = room1()
bosskey = Key(key_room,key_slime)
secondroom = Room2('graphics/room4.png')
thirdroom = Room3('graphics/room5b.png')
fourthroom = Room4('graphics/room6.png')
bossroom = Bossroom('graphics/bossroom3.png')
currentroom = firstroom
sprites_alive = pygame.sprite.Group()
sprites_walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

## add monster sprites to this group to draw them to the screen
#sprites_alive.add(player)
sprites_alive.add(slime1)
sprites_alive.add(slime2)

#sprites_alive.add(icenova)


sprites_walls.add(firstroom.wallLeft1)
all_sprites.add(sprites_alive,sprites_walls)

fade = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #pygame.draw.rect(screen,(255,0,0), (player.rect),0)
        pressed_keys = pygame.key.get_pressed()


        #print(slime1.isDying)
        #print(slime1.current_frame)
        #print(slime1.dyingtime)

        screen.blit(currentroom.roomimage,(0,0))

        if (player.castingIceNova == True):
            icenova.update()
            screen.blit(icenova.surf,icenova.rect)


####### drawing spell icons #################################
        if (player.mana >=5 and player.fireCountingCooldown == False):
            screen.blit(fireballicon,(800,10))
        else :
            screen.blit(fireballicongrey,(800,10))

        if (player.mana >=20):
            screen.blit(lightningicon,(900,10))
        else :
            screen.blit(lightningicongrey,(900,10))
        if (player.startCountingCooldown == False and player.mana >=10):
            screen.blit(icenovaicon,(1000,10))
        else :
            screen.blit(icenovaicongrey,(1000,10))

########### Key stuff here ##################

        if (currentroom == fourthroom and player.hasKey == False and bosskey.room == 4):
            if (bosskey.slimenum == 1):
                bosskey.update(slime1.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime1.isAlive == False):
                    player.hasKey = True
            elif (bosskey.slimenum == 2):
                bosskey.update(slime2.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime2.isAlive == False):
                    player.hasKey = True
        elif (currentroom == firstroom and player.hasKey == False and bosskey.room == 1):
            if (bosskey.slimenum == 1):
                bosskey.update(slime1.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime1.isAlive == False):
                    player.hasKey = True
            elif (bosskey.slimenum == 2):
                bosskey.update(slime2.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime2.isAlive == False):
                    player.hasKey = True
        elif (currentroom == thirdroom and player.hasKey == False and bosskey.room == 3):
            if (bosskey.slimenum == 1):
                bosskey.update(slime1.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime1.isAlive == False):
                    player.hasKey = True
            elif (bosskey.slimenum == 2):
                bosskey.update(slime2.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime2.isAlive == False):
                    player.hasKey = True
        elif (currentroom == secondroom and player.hasKey == False and bosskey.room == 2):
            if (bosskey.slimenum == 1):
                bosskey.update(slime1.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime1.isAlive == False):
                    player.hasKey = True
            elif (bosskey.slimenum == 2):
                bosskey.update(slime2.rect)
                screen.blit(bosskey.surf,bosskey.rect)
                if(pygame.Rect.colliderect(player.hitbox, bosskey.rect) and slime2.isAlive == False):
                    player.hasKey = True


        for entity in sprites_alive: #this draws the sprites in the sprites_alive group (player and monsters)
            screen.blit(entity.surf, entity.rect)

        screen.blit(player.surf, player.rect)
        if (player.spawnFireball == True):
            fireball.update()
            screen.blit(fireball.surf,fireball.rect)


        #else :
            #bosskey.rect.x = -100
            #bosskey.rect.y = -100

    #self.room = roomnum
    #self.slimenum = slimenum

        pygame.draw.rect(screen,(255,0,0), (102,25,player.health*5,30),0) #draws the health bar
        pygame.draw.rect(screen,(0,0,255), (102,68,player.mana*5,30),0) #draws the mana bar
        screen.blit (ui,(10,10))#draws the ui to the screen
        #pygame.draw.rect(screen,(0,0,255),(slime1.hitbox),0)
       # pygame.draw.rect(screen,(255,0,0),(player.rect), 0)
        #pygame.draw.rect(screen,(255,0,0),(slime1.rect), 0)
        #pygame.draw.rect(screen,(0,0,255),player.hitbox,0)
###############These if statements check for collision with player and walls and if true sets the players speed to 0###############


        if (pygame.Rect.colliderect(player.hitbox, currentroom.wallLeft1) or pygame.Rect.colliderect(player.hitbox, currentroom.wallLeft2)):
            player.leftspeed =0
        if (pygame.Rect.colliderect(player.hitbox, currentroom.wallRight1) or pygame.Rect.colliderect(player.hitbox, currentroom.wallRight2)):
            player.rightspeed =0
        if (pygame.Rect.colliderect(player.hitbox, currentroom.wallTop1) or pygame.Rect.colliderect(player.hitbox, currentroom.wallTop2)):
            player.upspeed = 0
        if (pygame.Rect.colliderect(player.hitbox, currentroom.wallBottom1) or pygame.Rect.colliderect(player.hitbox, currentroom.wallBottom2)):
            player.downspeed = 0
        if (pygame.Rect.colliderect(player.hitbox, currentroom.wallMiddle) or pygame.Rect.colliderect(player.hitbox, currentroom.wallMiddle2) or pygame.Rect.colliderect(player.hitbox, currentroom.wallMiddle3) or
        pygame.Rect.colliderect(player.hitbox, currentroom.wallMiddle4)):
            if (player.direction == 1):
                player.upspeed =0
                player.rect.move_ip(0, 1)
                player.hitbox.move_ip(0, 1)
            if (player.direction==2):
                player.rightspeed = 0
                player.rect.move_ip(-1, 0)
                player.hitbox.move_ip(-1, 0)
            if (player.direction==3):
                player.downspeed = 0
                player.rect.move_ip(0, -1)
                player.hitbox.move_ip(0, -1)
            if (player.direction ==4):
                player.leftspeed =0
                player.rect.move_ip(1, 0)
                player.hitbox.move_ip(1, 0)
            if (currentroom == thirdroom and player.direction == 1):
                player.upspeed = 0
                player.rect.move_ip(0,-2)
                player.hitbox.move_ip(0,-2)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.hitbox.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.upspeed = 4
            if (currentroom == thirdroom and player.direction == 4):
                player.upspeed = 0
                player.rect.move_ip(-2,0)
                player.hitbox.move_ip(-2,0)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.hitbox.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.leftspeed = 4
            if (currentroom == thirdroom and player.direction == 2):
                player.upspeed = 0
                player.rect.move_ip(2,0)
                player.hitbox.move_ip(2,0)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.hitbox.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.rightspeed = 4
            if (currentroom == thirdroom and player.direction == 3):
                player.upspeed = 0
                player.rect.move_ip(0,2)
                player.hitbox.move_ip(0,2)
                player.falling = True
                player.fallingTime +=1
                if (player.fallingTime % 30 == 0):
                    #player.surf = pygame.transform.scale(player.surf,(63,93))
                    #thirdroom.leftDoor.rect.x
                    xdistance = thirdroom.leftDoor.rect.x - player.rect.x + 100
                    ydistance = thirdroom.leftDoor.rect.y - player.rect.y + 30
                    player.rect.move_ip(xdistance, ydistance)
                    player.hitbox.move_ip(xdistance, ydistance)
                    player.surf = player.walk_right_ani[0]
                    player.downspeed = 4

###############These check for collision with the doors and loads new rooms and moves player#####################
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.topDoor)):
            slime1.newInstruction = True
            slime2.newInstruction = True
            if (currentroom == firstroom):
                changeRooms(secondroom)
                slime1.isSpawning = True
                slime1.spawn(100,100)
                slime2.isSpawning = True
                slime2.spawn(900,500)
                player.rect.move_ip(0,500)
                player.hitbox.move_ip(0,500)
            elif (currentroom == thirdroom):
                changeRooms(fourthroom)
                slime1.isSpawning = True
                slime1.spawn(300,400)
                slime2.isSpawning = True
                slime2.spawn(900,200)
                player.rect.move_ip(0,500)
                player.hitbox.move_ip(0,500)
            elif (currentroom == fourthroom and player.hasKey == True):
                changeRooms(bossroom)
                slime1.isAlive = False
                slime2.isAlive = False
                player.rect.move_ip(0,500)
                player.hitbox.move_ip(0,500)
                slime1.rect.move_ip(10000,1000)
                slime1.hitbox.move_ip(10000,1000)
                slime2.rect.move_ip(10000,1000)
                slime2.hitbox.move_ip(10000,1000)
            elif (currentroom == fourthroom and player.hasKey == False):
                player.upspeed = 0
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.bottomDoor)):
            slime1.newInstruction = True
            slime2.newInstruction = True
            if (currentroom == secondroom):
                changeRooms(firstroom)
                slime1.isSpawning = True
                slime1.spawn(800,400)
                slime2.isSpawning = True
                slime2.spawn(200,400)
                player.rect.move_ip(0,-500)
                player.hitbox.move_ip(0,-500)
            elif (currentroom == fourthroom):
                changeRooms(thirdroom)
                slime1.isSpawning = True
                slime1.spawn(500,300)
                slime2.isSpawning = True
                slime2.spawn(900,500)
                player.rect.move_ip(0,-500)
                player.hitbox.move_ip(0,-500)
            elif (currentroom == bossroom):
                player.downspeed = 0
                #changeRooms(fourthroom)
                #slime1.isSpawning = True
                #slime1.spawn(300,400)
                #slime2.isSpawning = True
                #slime2.spawn(900,200)

        if (checkCollision(pygame.sprite.Sprite, player, currentroom.rightDoor)):
            slime1.newInstruction = True
            slime2.newInstruction = True
            if (currentroom == firstroom):
                changeRooms(thirdroom)
                slime1.isSpawning = True
                slime1.spawn(500,300)
                slime2.isSpawning = True
                slime2.spawn(900,500)
            elif (currentroom == secondroom):
                changeRooms(fourthroom)
                slime1.isSpawning = True
                slime1.spawn(300,400)
                slime2.isSpawning = True
                slime2.spawn(900,200)
            player.rect.move_ip(-1030,0)
            player.hitbox.move_ip(-1030,0)
        if (checkCollision(pygame.sprite.Sprite, player, currentroom.leftDoor)):
            slime1.newInstruction = True
            slime2.newInstruction = True
            if (currentroom == thirdroom):
                changeRooms(firstroom)
                slime1.isSpawning = True
                slime1.spawn(800,400)
                slime2.isSpawning = True
                slime2.spawn(200,400)
            elif (currentroom == fourthroom):
                changeRooms(secondroom)
                slime1.isSpawning = True
                slime1.spawn(100,100)
                slime2.isSpawning = True
                slime2.spawn(900,500)
                #player.rect.move_ip(0,500)
            player.rect.move_ip(1020,0)
            player.hitbox.move_ip(1020,0)


################ Fireball stuff #######################
        #if (player.spawnFireball == True):
            #fireball.isActive = True
            #player.spawnFireball = False


################Spell collision with slime ###########################
        if (checkCollision(pygame.sprite.Sprite, icenova, slime1)):
            if (icenova.canFreeze == True and slime1.isAlive == True):
                slime1.frozen = True
                slime1.speed = 0
        if (checkCollision(pygame.sprite.Sprite, icenova, slime2)):
            if (icenova.canFreeze == True and slime2.isAlive == True):
                slime2.frozen = True
                slime2.speed = 0
        if (pygame.Rect.colliderect(slime1.hitbox, fireball.rect)):
            if (slime1.isAlive == True and fireball.isActive == True):
                slime1.isDying = True
                slime1.current_frame = 0
                slime1.isAlive = False
        if (pygame.Rect.colliderect(slime2.hitbox, fireball.rect)):
            if (slime2.isAlive == True and fireball.isActive == True):
                slime2.isDying = True
                slime2.current_frame = 0
                slime2.isAlive = False
                #slime1.die()

############### Slime on Slime collision######################
        if (pygame.Rect.colliderect(slime1.hitbox, slime2.hitbox)):
            if (slime1.direction == 1 and slime1.isAlive == True and slime2.isAlive == True):
                slime1.direction = 0
                slime2.direction = 1
            elif (slime1.direction==0 and slime1.isAlive == True and slime2.isAlive == True):
                slime1.direction = 1
                slime2.direction = 0
            elif (slime1.direction==2 and slime1.isAlive == True and slime2.isAlive == True):
                slime1.direction = 3
                slime2.direction = 2
            elif (slime1.direction ==3 and slime1.isAlive == True and slime2.isAlive == True):
                slime1.direction = 2
                slime2.direction = 3

############### Player Collision with slime ##########################
        #if (checkCollision(pygame.sprite.Sprite, player,slime1)):
        if (pygame.Rect.colliderect(player.hitbox, slime1.hitbox)):
            if (slime1.frozen == True and slime1.isAlive == True):
                if (player.direction == 1):
                    player.upspeed =0
                    player.rect.move_ip(0, 1)
                    player.hitbox.move_ip(0, 1)
                if (player.direction==2):
                    player.rightspeed = 0
                    player.rect.move_ip(-1, 0)
                    player.hitbox.move_ip(-1, 0)
                if (player.direction==3):
                    player.downspeed = 0
                    player.rect.move_ip(0, -1)
                    player.hitbox.move_ip(0, -1)
                if (player.direction ==4):
                    player.leftspeed =0
                    player.rect.move_ip(1, 0)
                    player.hitbox.move_ip(1, 0)

        if (pygame.Rect.colliderect(player.hitbox, slime2.hitbox)):
            if (slime2.frozen == True and slime2.isAlive == True):
                if (player.direction == 1):
                    player.upspeed =0
                    player.rect.move_ip(0, 1)
                    player.hitbox.move_ip(0, 1)
                if (player.direction==2):
                    player.rightspeed = 0
                    player.rect.move_ip(-1, 0)
                    player.hitbox.move_ip(-1, 0)
                if (player.direction==3):
                    player.downspeed = 0
                    player.rect.move_ip(0, -1)
                    player.hitbox.move_ip(0, -1)
                if (player.direction ==4):
                    player.leftspeed =0
                    player.rect.move_ip(1, 0)
                    player.hitbox.move_ip(1, 0)
        
        slime1.update()
        slime2.update()
        player.update(pressed_keys) ###this calls the update method in player which checks for keypresses and handles movement/attacks

        #use the following for collision detection between player and enemies
        #if pygame.sprite.spritecollideany(player, enemies):
            #player takes damage and is pushed back?

        ##(102, 25) for health bar
        ##(102, 68) for mana bar


        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
