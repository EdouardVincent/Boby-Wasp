import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()
moove = 0
lose = 0
game = 0
game_started = 1

font=pygame.font.Font(None, 50)
font2=pygame.font.Font(None, 150)
trap_image = pygame.image.load('C:\Jeu personnages\OIP (46).png')
trap_upside_down_image = pygame.image.load('C:\Jeu personnages\OIP (47).png')
bg = pygame.image.load('C:\Jeu personnages\OIP (42).png')
bird_image = pygame.image.load('C:\Jeu personnages\OIP (44).png')
bee_image = pygame.image.load('C:\Jeu personnages\OIP (45).png')

window = pygame.display.set_mode((1400,670))

class Trap () :
    def __init__ (self) :
        self.image = trap_image
        self.x = 0
        self.y = 0
        self.velocity = 10

    def display(self) :
        window.blit(self.image,(self.x, self.y))

    def moove(self) :
        self.x -= self.velocity

class Bee () :
    def __init__ (self) :
        self.image = bee_image
        self.x = 300
        self.y = 300
        self.velocity = 10

    def display(self) :
        window.blit(self.image,(self.x, self.y))

    def moove_fall(self) :
        self.y += self.velocity

    def moove_up(self) :
        self.y -= self.velocity

while game_started :

    player = Bee()

    trap1ground = Trap()
    trap2ground = Trap()

    trap1ground.image = trap_upside_down_image
    trap2ground.image = trap_upside_down_image

    trap1ground.x = 2625
    trap1ground.y = random.randint(425,600)

    trap2ground.x = 3375
    trap2ground.y = random.randint(425,600)

    ############

    trap1up = Trap()
    trap2up = Trap()

    trap1up.x = 2400
    trap1up.y = random.randint(-125, 0)

    trap1up.x = 3050
    trap1up.y = random.randint(-125, 0)

    pygame.key.set_repeat(1,20)
    start_ticks=pygame.time.get_ticks()

    game = 1

    while game :
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds >= 30 :
            trap1ground.velocity = 12
            trap2ground.velocity = 12
            trap1up.velocity = 12
            trap2up.velocity = 12

        if seconds >= 50 :
            trap1ground.velocity = 15
            trap2ground.velocity = 15
            trap1up.velocity = 15
            trap2up.velocity = 15

        if seconds >= 100 :
            trap1ground.velocity = 18
            trap2ground.velocity = 18
            trap1up.velocity = 18
            trap2up.velocity = 18
        
        secondes = str(seconds)
        texte2 = font.render(secondes,1,(255,255,0))
    
        moove = 0
        trap1ground_rect = trap_image.get_rect(topleft = (trap1ground.x,trap1ground.y))
        trap2ground_rect = trap_image.get_rect(topleft = (trap2ground.x,trap2ground.y))

        trap1up_rect = trap_image.get_rect(topleft = (trap1up.x,trap1up.y))
        trap2up_rect = trap_image.get_rect(topleft = (trap2up.x,trap2up.y))
    
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN :
                moove = 1
                if (event.key == K_SPACE or event.key == K_UP) and player.y > 0 :
                    player.velocity = 14
                    player.moove_up()

                if event.key == K_DOWN and player.y < 590:
                    player.velocity = 14
                    player.moove_fall()

                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()

        if trap1ground_rect.collidepoint(player.x, player.y) or trap2ground_rect.collidepoint(player.x, player.y) or trap1up_rect.collidepoint(player.x, player.y) or trap2up_rect.collidepoint(player.x, player.y) :
            lose = 1
        

        if moove == 0 and player.y < 590 :
            player.velocity = 7
            player.moove_fall()
            
        if trap1ground.x <= -150 and trap2ground.x <= 1950 :
            trap1ground.x = 1625
            trap1ground.y = random.randint(300,500)
        
        if trap2ground.x <= -150 and trap2ground.x <= 1300 :
            trap2ground.x = trap1ground.x+750 #2275
            trap2ground.y = random.randint(300,500)

        if trap1up.x <= -150 : 
            trap1up.x = trap1ground.x-425 #1300
            trap1up.y = random.randint(-175,-100)
      
        if trap2up.x <= -150 and trap1up.x <= 1625 :
            trap2up.x = trap1ground.x+425 #1950
            trap2up.y = random.randint(-175,-100)

    
        if lose == 1 :
            texte1 = font2.render("STUCK !",1,(255,0,0))
            window.blit(texte1,(700,330))
            pygame.display.flip()
            time.sleep(5)
            lose = 0
            game = 0
            game_started = 1    
        
        window.blit(bg,(0,0))
        trap1ground.moove()
        trap2ground.moove()
        trap1up.moove()
        trap2up.moove()
    
        trap1ground.display()
        trap2ground.display()
        trap1up.display()
        trap2up.display()
        player.display()
        window.blit(texte2,(0,0))
        
        pygame.display.flip()
        FPSCLOCK.tick(FPS)
