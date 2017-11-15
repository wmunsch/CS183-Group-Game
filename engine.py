#Main engine
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 700))
done = False
x=640
y=350



theChar = pygame.image.load('desktop/graphics/character.png')
theChar = pygame.transform.scale(theChar,(76,112))
floortile = pygame.image.load('desktop/graphics/floortile.png')
floortile = pygame.transform.scale(floortile,(100,100))

#room1 = pygame.image.load('desktop/graphics/room1.png')
#room1 = room1.convert()
#room1 = pygame.transform.scale(room1,(1280,720))
framerate = pygame.time.Clock()

#def createRoom():
    
class Player:
    x = 640
    y = 350
    health = 10
    
class Goblin:
    x = 0
    y = 0
    health = 3
    
class room1:
    roomimage = pygame.image.load('desktop/graphics/room1.png')
    roomimage = roomimage.convert()
    roomimage = pygame.transform.scale(roomimage,(1280,720))
    wallup = 60
    walldown = 500
    wallleft = 100
    wallright = 1100
    

player = Player()
firstroom = room1()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        ##basic controls
        pressed = pygame.key.get_pressed()
        
        
        if pressed[pygame.K_UP]: 
            if player.y >= firstroom.wallup:player.y -= 4
        if pressed[pygame.K_DOWN]: 
            if player.y <= firstroom.walldown:player.y+= 4
        if pressed[pygame.K_LEFT]: 
            if player.x >= firstroom.wallleft:player.x -= 4
        if pressed[pygame.K_RIGHT]:
            if player.x <= firstroom.wallright:player.x+= 4

            
        screen.fill((0,0,0))
        screen.blit(firstroom.roomimage,(0,0))
        screen.blit(floortile,(100,100)) 
        screen.blit(floortile,(200,200))
        screen.blit(theChar,(player.x,player.y))

        #surface = pygame.image.load('graphics/character.png')
        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
