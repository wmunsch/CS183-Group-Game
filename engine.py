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
        
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
    x = 640
    y = 350
    health = 10
    
    

    
    
class Goblin:
    x = 0
    y = 0
    health = 3
    
class room1:
    roomimage = pygame.image.load('graphics/room2.png')
    roomimage = roomimage.convert()
    roomimage = pygame.transform.scale(roomimage,(1280,720))
    wallLeft = pygame.Rect(0,0,100,1280)
    
    wallup = 60
    walldown = 500
    wallleft = 100
    wallright = 1100
    

player = Player()
firstroom = room1()

sprites = pygame.sprite.Group()
## add sprites to this group to draw them to the screen
sprites.add(player)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        ##basic controls
        #pressed = pygame.key.get_pressed()
        
        
        #if pressed[pygame.K_UP]: 
        #    if player.y >= firstroom.wallup:player.y -= 4
        #if pressed[pygame.K_DOWN]: 
        #    if player.y <= firstroom.walldown:player.y+= 4
        #if pressed[pygame.K_LEFT]: 
       #     if player.x >= firstroom.wallleft:player.x -= 4
       # if pressed[pygame.K_RIGHT]:
        #    if player.x <= firstroom.wallright:player.x+= 4

        pressed_keys = pygame.key.get_pressed()
        currentMap = firstroom
        if (player.rect.left < currentMap.wallLeft.right):
            player.update(pressed_keys)
        
        #screen.fill((0,0,0)) dont use anymore
        screen.blit(firstroom.roomimage,(0,0))
       
        for entity in sprites:
            screen.blit(entity.surf, entity.rect)
           
        #use the following for collision detection between player and enemies
        #if pygame.sprite.spritecollideany(player, enemies):
            #player.kill()
        

        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
