#Main engine
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 700))
done = False
x=640
y=350
theChar = pygame.image.load('graphics/character.png')
theChar = pygame.transform.scale(theChar,(76,112))
room1 = pygame.image.load('graphics/room1.png')
room1 = room1.convert()
room1 = pygame.transform.scale(room1,(1280,720))
framerate = pygame.time.Clock()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        ##basic controls
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 4
        if pressed[pygame.K_DOWN]: y+= 4
        if pressed[pygame.K_LEFT]: x -= 4
        if pressed[pygame.K_RIGHT]: x+= 4

        screen.fill((0,0,0))
        screen.blit(room1,(0,0))

        screen.blit(theChar,(x,y))

        #surface = pygame.image.load('graphics/character.png')
        pygame.display.flip()
        framerate.tick(60) #sets the framerate to 60 fps
