import pygame


pygame.init()
done = False

#mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.diamond)

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

l = pygame.image.load("ers.png")
s = pygame.image.load("start.png")
ws = pygame.image.load("istart.png")
b = pygame.image.load("bonus.png")
ib = pygame.image.load("ibonus.png")


class button(): 
    """This class creates a invisible clickable box (or button)"""
    def __init__(self, x, y, width, height):  
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        
    def isOver(self, pos): #Pos is the mouse position [(x,y) coordinates] 
        if self.x < pos[0] < self.x + self.width: 
            if self.y < pos[1] < self.y + self.height: 
                return True 
        return False


intro = True
lvl1 = True

while intro:
#intro loop
    gameDisplay = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Welcome to ERS')#caption of display window
                
    gameDisplay.fill(white) #background
    gameDisplay.blit(l,(55,0)) #ers
    gameDisplay.blit(s,(95,175)) #start
    start = button(141, 293, 205, 63) #creates button over top of start
    gameDisplay.blit(b,(95,250)) #bonus
    bonus = button(141, 355, 204, 67) #creates button over top of bonus

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.isOver(pos):
                intro = False
            if bonus.isOver(pos):
                intro = False
            
        if event.type == pygame.MOUSEMOTION:
            if start.isOver(pos):
                gameDisplay.blit(ws,(95,175)) #inverse start
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            elif start.isOver(pos) != True:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)  

            if bonus.isOver(pos):
                gameDisplay.blit(ib,(95,250)) #inverse bonus
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            elif bonus.isOver(pos) != True:
                pygame.mouse.set_cursor(*pygame.cursors.arrow) 

    pygame.display.flip()
    clock.tick(60)

press_dict = {'bed': {'mx_min': 850, 'mx_max': 1270, 'my_min': 570, 'my_max': 680,
                      'text': GAME_FONT.render("This bed reminds me of something, but I can't quite put my finger on it.", False, (255, 255, 255))},
                'door': {'mx_min': 400, 'mx_max': 550, 'my_min': 310, 'my_max': 610,
                      'text': GAME_FONT.render("This door is locked.", False, (255, 255, 255))},
                'key': {'mx_min': 600, 'mx_max': 640, 'my_min': 350, 'my_max': 410,
                      'text': GAME_FONT.render("FRREEEEEDDOOOM!!!!", False, (255, 255, 255))},
                'ceiling': {'mx_min': 0, 'mx_max': 1400, 'my_min': 0, 'my_max': 115,
                      'text': GAME_FONT.render("That's weird, there are no lights in this room.", False, (255, 255, 255))}
}
             
text_render_queue = {}

def button_press(mx,my,text_render_queue,press_dict=press_dict):
        """Function that checks coords of mouse click against dictionary
        of known events and then adds them to the render queue modifies press_dict"""

        for key in press_dict:
                # This contains the actions and locations for all interaction related to clicking
                if press_dict[key]['mx_min']<=mx<=press_dict[key]['mx_max'] and press_dict[key]['my_min']<=my<=press_dict[key]['my_max']:
                        #print('caught the button press {}'.format(key))
                        text_render_queue[key] = {'text':press_dict[key]['text'],'ticks':50,}



def render_text(text_render_queue):
        del_list = []
        for key in text_render_queue:
                if text_render_queue[key]['ticks'] >= 0:
                        # render text to screen
                        screen.blit(text_render_queue[key]['text'], (110,10))
                        # decrease the number of ticks left
                        text_render_queue[key]['ticks'] -= 1
                        pygame.display.update() 
                else:
                        del_list.append(key)
        
        # cleanup
        [text_render_queue.pop(key) for key in del_list]
                        


while lvl1: 
#level1 game loop
        screen = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption('ERS')#caption of display window


        screen.fill((0, 0, 0))
        """This is the background of the first room"""
        pygame.draw.rect(screen, green, pygame.Rect(200, 110, 1000, 500))
        pygame.draw.rect(screen, black, pygame.Rect(210, 120, 980, 480))
        #corner lines
        pygame.draw.line(screen, green, (0,0), (205,114), 10)
        pygame.draw.line(screen, green, (1400,0), (1190,114), 10)
        pygame.draw.line(screen, green, (0,800), (205,600), 10)
        pygame.draw.line(screen, green, (1400,800), (1190,600), 10)
        #ceiling button
        roof = button(0, 0, 1400, 115)
        #door
        pygame.draw.rect(screen, green, pygame.Rect(400, 310, 150, 300))
        pygame.draw.rect(screen, black, pygame.Rect(410, 320, 130, 280))
        pygame.draw.circle(screen, green, (520, 460), 10, 10)
        pygame.draw.circle(screen, black, (520, 460), 7, 7)
        #door button
        door = button(400, 310, 150, 290)
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
        #bed button
        bed = button(840, 565, 400, 110)

        #key sprite
        k = pygame.image.load("key.png")
        screen.blit(k,(590,350))
        key = button(600, 350, 25, 50)
        ik = pygame.image.load("bkey.png") #loads in missing key

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                        lvl1 = False
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        #print (pygame.mouse.get_pos())
                        # check mouse click against all registered coordinates
                        button_press(mx,my,text_render_queue)
                        if key.isOver(pos):
                                screen.blit(ik,(590,350)) #inverse key
                                pygame.display.update()
                
                if event.type == pygame.MOUSEMOTION:
                        #if cursor is over any clickable objects changes cursor
                        if key.isOver(pos) or bed.isOver(pos) or door.isOver(pos) or roof.isOver(pos):
                                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        elif key.isOver(pos) != True or bed.isOver(pos) != True or door.isOver(pos) != True or roof.isOver(pos) != True:
                                pygame.mouse.set_cursor(*pygame.cursors.arrow)


        # render text in the queue
        render_text(text_render_queue)
        
        pygame.display.flip()
        clock.tick(60)
