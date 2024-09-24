import pygame
import time

pygame.mixer.init(44100, -16, 1, 3072)#initializes sound mixer
pygame.init()
time_left = 2000 #in milliseconds = one second

#mouse cursor and mouse coordinates
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
GAME_FONT = pygame.font.SysFont(None, 50)

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
disp = 1 #executes display window unless start or bonus is clicked
lvl1 = True
sec = 0
play = 0
cbonus = 0
countdown = 1

while intro:
#intro loop
    if disp == 1:
        gameDisplay = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Welcome to ERS')#caption of display window
                
        gameDisplay.fill(white) #background
        gameDisplay.blit(l,(55,0)) #ers
        gameDisplay.blit(s,(95,175)) #start
        start = button(141, 293, 205, 63) #creates button over top of start
        gameDisplay.blit(b,(95,250)) #bonus
        bonus = button(141, 355, 204, 67) #creates button over top of bonus

    #below is each slide of the coundown clip
    three = pygame.image.load("three.png")
    two = pygame.image.load("two.png")
    one = pygame.image.load("one.png")
    zero = pygame.image.load("zero.png")
    #sound files for the countdown
    sb1 = pygame.mixer.Sound('beep1.wav')
    sb2 = pygame.mixer.Sound('beep2.wav')


    if play == 1: #if start is clicked
        #Plays movie intro
        gameDisplay = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Coundown')#caption of display window

        gameDisplay.fill(white) #clears screen
        pygame.display.update()

        if countdown == 1:
            gameDisplay.blit(three,(0,0)) #each slide gets blitted in
            countdown += 1
            pygame.time.wait(750)
        elif countdown == 2:
            sb1.play()#plays beep1 signaling next number
            gameDisplay.blit(two,(0,0)) #each slide gets blitted in
            countdown += 1
            pygame.time.wait(750)
        elif countdown == 3:
            sb1.play()#plays beep1 signaling next number
            gameDisplay.blit(one,(0,0)) #each slide gets blitted in
            pygame.time.wait(750)
            countdown += 1
        elif countdown == 4:
            sb1.play()#plays beep1 signaling next number
            gameDisplay.blit(zero,(0,0)) #each slide gets blitted in
            pygame.time.wait(750)
            countdown += 1
        elif countdown == 5:
            pygame.time.wait(250)
            sb2.play()#plays beep2 signaling end of countdown
            intro = False #quits intro starts lvl1

        pygame.display.update()

    if cbonus == 1: #if bonus is clicked

        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        gameDisplay = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption('Bonus')#caption of display window
        gameDisplay.fill(black) #background
        text = GAME_FONT.render("Welcome to ERS! AKA Escape Room Simulator. This is my final project for", False, (255, 255, 255))
        gameDisplay.blit(text, (20,20))
        text2 = GAME_FONT.render("CPSC 101. It is incredibly basic, but was a lot of fun to make. I hope you", False, (255, 255, 255))
        gameDisplay.blit(text2, (20,70))
        text3 = GAME_FONT.render("enjoy playing it as much as I did making it. All of the sound clips are", False, (255, 255, 255))
        gameDisplay.blit(text3, (20,120))
        text4 = GAME_FONT.render("royalty free meaning they are fair use. They are all from this site:", False, (255, 255, 255))
        gameDisplay.blit(text4, (20,170))
        text5 = GAME_FONT.render("https://www.fesliyanstudios.com/royalty-free-sound-effects-download", False, (255, 255, 255))
        gameDisplay.blit(text5, (20,220))
        text6 = GAME_FONT.render("https://www.freesoundeffects.com/free-sounds", False, (255, 255, 255))
        gameDisplay.blit(text6, (20,270))
        text7 = GAME_FONT.render("Press space to return to the menu", False, (255, 255, 255))
        gameDisplay.blit(text7, (830,750))
        text8 = GAME_FONT.render("P.S. Did you find any hidden secrets?", False, (255, 255, 255))
        gameDisplay.blit(text8, (20,500))
        pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.isOver(pos):
                disp = 2
                play = 1
            if bonus.isOver(pos):
                disp = 2
                cbonus = 1
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if cbonus == 1:
                disp = 1
                cbonus = 0
            
        if event.type == pygame.MOUSEMOTION:
            if play != 1 and cbonus != 1:
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
                # 'key': {'mx_min': 600, 'mx_max': 640, 'my_min': 350, 'my_max': 410,
                #       'text': GAME_FONT.render("FRREEEEEDDOOOM!!!!", False, (255, 255, 255))},
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
                        

key_got = 0 #global variable needed to keep track of the key as well as the door
door_click = 0
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
        bs = button(300, 700, 30, 30)#angles
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
        key = button(600, 350, 25, 50) #makes button around key
        ik = pygame.image.load("bkey.png") #loads in missing key
        s = pygame.image.load("leftover//secret.png")

        s1 = pygame.mixer.Sound('keys.wav')
        s2 = pygame.mixer.Sound('doorc.wav')
        ns = pygame.mixer.Sound('secretn.wav')
        ns2 = pygame.mixer.Sound('secretn2.wav')
        s3 = pygame.mixer.Sound('doorh.wav')
        s4 = pygame.mixer.Sound('unlock.wav')
        
        if sec == 1:
            if countdown == 1:
                screen.blit(s,(250,50)) #each slide gets blitted in
                pygame.display.update()
                pygame.time.wait(2000)
            s3.play(maxtime = 1690)
            ns2.play()
            ns.play(maxtime = 4000)
            countdown += 1
            sec = 2
        if key_got == 1 and door_click == 1:
            lvl1 = False
        elif key_got == 1:
            screen.blit(ik,(590,350)) #inverse key
            pygame.display.update()

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        #print (pygame.mouse.get_pos())
                        # check mouse click against all registered coordinates
                        button_press(mx,my,text_render_queue)
                        if door.isOver(pos):
                                s3.play(maxtime = 1690)#plays handle noise
                        if key.isOver(pos):
                                key_got = 1
                                s1.play(maxtime = 1360)#plays key jingle
                        if bs.isOver(pos):
                                sec += 1
                                countdown = 1
                        if door.isOver(pos) and key_got == 1:
                                door_click = 1
                                s4.play()#plays door unlock
                                s2.play()#plays door open
                
                if event.type == pygame.MOUSEMOTION:
                        #if cursor is over any clickable objects changes cursor
                        if key.isOver(pos) or bed.isOver(pos) or door.isOver(pos) or bs.isOver(pos) or roof.isOver(pos):
                                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        elif key.isOver(pos) != True or bed.isOver(pos) != True or door.isOver(pos) != True or bs.isOver(pos) != True or roof.isOver(pos) != True:
                                pygame.mouse.set_cursor(*pygame.cursors.arrow)


        # render text in the queue
        render_text(text_render_queue)
    
        pygame.display.flip()
        clock.tick(60)

Outro = True

while Outro:
#outro loop
    gameDisplay = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('ERS')#caption of display window
                
    gameDisplay.fill(black) #background
    text = GAME_FONT.render("Oh look, you made it through the first level.", False, (255, 255, 255))
    gameDisplay.blit(text, (355,390))
    t2 = GAME_FONT.render("Press space to continue.", False, (255, 255, 255))
    gameDisplay.blit(t2, (980,750))
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            Outro = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Outro = False
            

    pygame.display.flip()
    clock.tick(60)
