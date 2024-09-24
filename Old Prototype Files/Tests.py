import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('ERS')#caption of display window
done = False
is_blue = True

clock = pygame.time.Clock()


white = (255,255,255)
l = pygame.image.load("ers.png")
k = pygame.image.load("start.png")
ik = pygame.image.load("inversestart.png")
b = pygame.image.load("bonus.png")
ib = pygame.image.load("ibonus.png")



intro = True

while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                
    gameDisplay.fill(white)
    gameDisplay.blit(l,(55,0))
    gameDisplay.blit(k,(95,175))
    #gameDisplay.blit(ik,(95,100)) inverse
    gameDisplay.blit(b,(95,250))
    #gameDisplay.blit(ik,(95,200)) inverse
    pygame.display.update()
    clock.tick(15)