import pygame


pygame.init()
screen = pygame.display.set_mode((1400, 800))
done = False
is_blue = True
#x = 30
#y = 30

#mouse cursor
pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))

#colours
red = (255,0,0)
dred = (153,0,0)
green = (50,205,50)
blue = (0,128,255)
darkBlue = (0,0,128)
white = (255,255,255)
dwhite = (192,192,192)
black = (0,0,0)
pink = (255,200,200)

#font
GAME_FONT = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

while not done:

        screen.fill((0, 0, 0))
        """This is the background of the first room"""
        pygame.draw.rect(screen, green, pygame.Rect(200, 110, 1000, 500))
        pygame.draw.rect(screen, black, pygame.Rect(210, 120, 980, 480))
        #corner lines
        pygame.draw.line(screen, green, (0,0), (205,114), 10)
        pygame.draw.line(screen, green, (1400,0), (1190,114), 10)
        pygame.draw.line(screen, green, (0,800), (205,600), 10)
        pygame.draw.line(screen, green, (1400,800), (1190,600), 10)
        #door
        pygame.draw.rect(screen, green, pygame.Rect(400, 310, 150, 300))
        pygame.draw.rect(screen, black, pygame.Rect(410, 320, 130, 280))
        pygame.draw.circle(screen, green, (520, 460), 10, 10)
        pygame.draw.circle(screen, black, (520, 460), 7, 7)
        #bed
        #solid colour
        pygame.draw.rect(screen, red, pygame.Rect(900, 640, 290, 40))
        #red blanket
        pygame.draw.polygon(screen, red, [(850,570), (1110,570), (900,640), (1190,640)])
        pygame.draw.polygon(screen, red, [(850,570), (900,640), (1110,570), (1190,640)])
        pygame.draw.polygon(screen, red, [(850,570), (850,610), (900,640), (900,680)])
        pygame.draw.polygon(screen, red, [(850,570), (900,640), (850,610), (900,680)]) 
        #white sheets
        pygame.draw.polygon(screen, white, [(1110,570), (1190,570), (1190,640), (1270,640)])
        pygame.draw.polygon(screen, white, [(1110,570), (1190,640), (1190,570), (1270,640)])
        pygame.draw.rect(screen, white, pygame.Rect(1190, 640, 80, 40))
        pygame.draw.line(screen, dred, (850,570), (1110,570), 5)
        pygame.draw.line(screen, dwhite, (1110,570), (1190,570), 5)
        pygame.draw.line(screen, dred, (900,640), (1190,640), 5)
        pygame.draw.line(screen, dwhite, (1190,640), (1270,640), 5)
        #angles
        pygame.draw.line(screen, dred, (850,570), (900,640), 5)
        pygame.draw.line(screen, dwhite, (1190,570), (1270,640), 5)
        pygame.draw.line(screen, dred, (850,610), (900,680), 5)
        #corners
        pygame.draw.line(screen, dred, (850,570), (850,610), 5)
        pygame.draw.line(screen, dred, (900,640), (900,680), 5)
        pygame.draw.line(screen, dwhite, (1270,640), (1270,680), 5)
        pygame.draw.line(screen, dred, (900,680), (1190,680), 5)
        pygame.draw.line(screen, dwhite, (1190,680), (1270,680), 5)
        pygame.draw.line(screen, dred, (900,640), (900,680), 5)
        #blanket
        pygame.draw.line(screen, dred, (1110,570), (1190,640), 5)
        pygame.draw.line(screen, dred, (1190,640), (1190,682), 5)

        #pygame.font.Font.render("Welcome to the first level", white)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if 400<=mx<=550 and 310<=my<=610:
                                text_surface = GAME_FONT.render("Hello", False, (255, 255, 255))
                                screen.blit(text_surface, (50, 50))
                        else: pass
        
        pygame.display.flip()
        clock.tick(60)