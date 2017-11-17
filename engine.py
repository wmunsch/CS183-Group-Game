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
        self.rect = self.surf.get_rect()
        self.rect.move_ip(400,0)
        
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            
            
          
    speed = 5
    x = 640
    y = 350
    health = 10
    
    

    
    
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
    wallMiddle = Wall(200,0,200,300)
    
        
    
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
            player.rect.move_ip(5, 0)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallRight2)):
            player.rect.move_ip(-5, 0)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallTop2)):
            player.rect.move_ip(0, 5)
        if (checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom1) or checkCollision(pygame.sprite.Sprite, player,currentroom.wallBottom2)):
            player.rect.move_ip(0, -5)
        
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
