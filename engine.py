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

#room1 = pygame.image.load('graphics/room1.png')
#room1 = room1.convert()
#room1 = pygame.transform.scale(room1,(1280,720))
framerate = pygame.time.Clock()

#def createRoom():
    
class Player:
    x = 640
    y = 350
    health = 10

player = Player()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        ##basic controls
        pressed = pygame.key.get_pressed()
        
        
        if pressed[pygame.K_UP]: 
            if player.y >= 400:player.y -= 4
        if pressed[pygame.K_DOWN]: player.y+= 4
        if pressed[pygame.K_LEFT]: player.x -= 4
        if pressed[pygame.K_RIGHT]: player.x+= 4

            
        screen.fill((0,0,0))
        #screen.blit(room1,(0,0))
        screen.blit(floortile,(100,100)) 
        screen.blit(floortile,(200,200))
        screen.blit(theChar,(player.x,player.y))

        #surface = pygame.image.load('graphics/character.png')
        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
