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

l = pygame.image.load("ers.png")#start menu logo and buttons
s = pygame.image.load("start.png")
ws = pygame.image.load("istart.png")
b = pygame.image.load("bonus.png")
ib = pygame.image.load("ibonus.png")
l1 = pygame.image.load("lock1.png") #each frame of lock animation
l2 = pygame.image.load("lock2.png")
l3 = pygame.image.load("lock3.png")


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

#global variables
key_got = 0 # lvl1 key
door_click = 0 #lvl 1 door
intro = True
disp = 1 #executes display window unless start or bonus is clicked
lvl1 = True
sec = 0 #film countdown animator
play = 0
cbonus = 0
countdown = 1
logo = 1 #padlock animator
done = False
pkey_got = 0 #piano key picked up
m_got = 0 #match got
key_placed = 0 #piano key placed in piano
boot_up = 0 #power start up
power = 0 #if power is on
fire = 0 #if fire is lit
light_on = 0 #if light switch is flicked
rpress = 0
gpress = 0
ypress = 0
bpress = 0
counter = 0
y_bpress = 0 #if blue is pressed after yellow
y_b_gpress = 0 #if green is pressed after previous
granted = 0 #if code it correct
player_exit = 0 #if player beats level 2
Outro2 = True

while intro:
#intro loop
    if disp == 1:
        gameDisplay = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption('Welcome to ERS')#caption of display window
                
        gameDisplay.fill(white) #background
        gameDisplay.blit(l,(55,0)) #ers
        gameDisplay.blit(s,(95,175)) #start
        start = button(141, 293, 205, 63) #creates button over top of start
        gameDisplay.blit(b,(95,250)) #bonus
        bonus = button(141, 355, 204, 67) #creates button over top of bonus
        text = GAME_FONT.render("@2019 Brenner De Vos", False, black)
        gameDisplay.blit(text, (1010, 760))
        text2 = GAME_FONT.render("Press space to quit...", False, black)
        gameDisplay.blit(text2, (20, 760))
    
        if logo == 1:
            gameDisplay.blit(l1,(0,50)) #lock frame
            pygame.time.wait(500)
            logo = 2
        elif logo == 2:
            gameDisplay.blit(l2,(0,50)) #lock frame 2
            pygame.time.wait(500)
            logo = 3
        elif logo == 3:
            gameDisplay.blit(l3,(0,50)) #lock frame 3
            pygame.time.wait(500)
            logo = 1

    #below is each slide of the coundown clip
    three = pygame.image.load("three.png")
    two = pygame.image.load("two.png")
    one = pygame.image.load("one.png")
    zero = pygame.image.load("zero.png")
    #sound files for the countdown
    sb1 = pygame.mixer.Sound('beep1.wav')
    sb2 = pygame.mixer.Sound('beep2.wav')
    n = pygame.mixer.Sound('but.wav')


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
        text4 = GAME_FONT.render("royalty free meaning they are fair use. They are all from these sites:", False, (255, 255, 255))
        gameDisplay.blit(text4, (20,170))
        text5 = GAME_FONT.render("https://www.fesliyanstudios.com/royalty-free-sound-effects-download", False, (255, 255, 255))
        gameDisplay.blit(text5, (20,220))
        text6 = GAME_FONT.render("https://www.freesoundeffects.com/free-sounds", False, (255, 255, 255))
        gameDisplay.blit(text6, (20,270))
        text7 = GAME_FONT.render("http://www.orangefreesounds.com/wrong-buzzer/", False, (255, 255, 255))
        gameDisplay.blit(text7, (20,320))
        text8 = GAME_FONT.render("Press space to return to the menu", False, (255, 255, 255))
        gameDisplay.blit(text8, (830,750))
        text9 = GAME_FONT.render("P.S. Did you find any hidden secrets?", False, (255, 255, 255))
        gameDisplay.blit(text9, (20,500))
        
        pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.isOver(pos):
                disp = 0
                play = 1
            if bonus.isOver(pos):
                disp = 0
                cbonus = 1
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if cbonus == 1:
                disp = 1
                cbonus = 0
            elif cbonus != 1:
                pygame.quit()
                quit()
            
        if event.type == pygame.MOUSEMOTION:
            if play != 1 and cbonus != 1:
                if start.isOver(pos):
                    n.play()#plays noise signalling over button
                    gameDisplay.blit(ws,(95,175)) #inverse start
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                elif start.isOver(pos) != True:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)  

                if bonus.isOver(pos):
                    n.play()#plays noise signalling over button
                    gameDisplay.blit(ib,(95,250)) #inverse bonus
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                elif bonus.isOver(pos) != True:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow) 

    pygame.display.flip()
    clock.tick(60)


press_dict = {'bed': {'mx_min': 850, 'mx_max': 1270, 'my_min': 570, 'my_max': 680,
                      'text': GAME_FONT.render("You cannot sleep while there are mosters nearby.", False, (255, 255, 255))},
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

disp = 1
while not done:
        ra = pygame.image.load("rarrow.png") #arrows
        lab = button(30,675,140,125)
        la = pygame.image.load("larrow.png")
        rab = button(1230,665,140,125)
        
        e = pygame.image.load("exit.png") #reg versions
        pad_button = button(0,0,0,0) #placeholder for button
        door_button = button(0,0,0,0) #placeholder for button
        er = pygame.image.load('exitr.png') #exit with green pad
        c = pygame.image.load("chim.png")
        lightswitch = button(0,0,0,0)
        fc = pygame.image.load("fchim.png")
        log_button = button(0,0,0,0)
        b = pygame.image.load("book.png")
        matchbook_button = button(0,0,0,0) #placeholder for button
        mb = pygame.image.load("mbook.png") #matchbook buttons
        mbutton = button(0,0,0,0) #placeholder
        emb = pygame.image.load("embook.png")
        book1 = button(0,0,0,0) #placeholder for button
        b1 = pygame.image.load("book1.png")
        got_button = button(0,0,0,0) #placeholder for button
        got = pygame.image.load("got.png")
        bookbook = pygame.image.load("book2.png")
        book2 = button(0,0,0,0) #placeholder for button
        book3333 = button(0,0,0,0) #book book button
        black_button = button(0,0,0,0) #black book button
        ac = pygame.image.load("acbook.png")
        hp_button = button(0,0,0,0) #hp book button
        hp = pygame.image.load("hp.png")
        we_know = button(0,0,0,0) #skyrim book button
        wk = pygame.image.load("weknow.png")
        b3 = pygame.image.load("book3333.png")#3333 book
        p = pygame.image.load("piano.png")
        key_button = button(0,0,0,0) #placeholder for button
        piano_button = button(0,0,0,0) #placeholder for button
        
        dc = pygame.image.load("dchim.png")#dark versions
        lc1 = pygame.image.load("lightandlogoff.png")#lightswitch hit
        lc2 = pygame.image.load("lightoff.png")#lightswtich hit + logs on fire
        db = pygame.image.load("dbook.png")
        dp = pygame.image.load("dpiano.png")
        dwk = pygame.image.load("key_miss.png")#piano key picked up but not placed
        dcp = pygame.image.load("dcpiano.png")#dark complete piano
        de = pygame.image.load("dexit.png")
        pad = pygame.image.load("pad.png")
        padw = pygame.image.load("pad_w.png")#wrong pad
        padr = pygame.image.load("pad_r.png")#right pad
        rpad = button(0,0,0,0)#red button
        gpad = button(0,0,0,0)#green button
        ypad = button(0,0,0,0)#yellow button
        bpad = button(0,0,0,0)#blue button
        
        s3 = pygame.mixer.Sound('doorh.wav')
        mg = pygame.mixer.Sound('medgears.wav')
        fg = pygame.mixer.Sound('fastgears.wav')
        su = pygame.mixer.Sound('startup.wav')
        melo = pygame.mixer.Sound('melo.wav')#piano melody
        click = pygame.mixer.Sound('click.wav')
        buzz = pygame.mixer.Sound('buzz.wav')
        switch = pygame.mixer.Sound('switch.wav')

        if disp == 1:#exit
                press_dict = {'door': {'mx_min': 468, 'mx_max': 803, 'my_min': 175, 'my_max': 785,
                        'text': GAME_FONT.render("Looks like the doors locked again", False, (255, 255, 255))}
                }

                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This is the background of the first wall"""
                if power == 1 and granted == 1:
                        screen.blit(er,(0,0)) #green pad
                        if player_exit == 1:
                            done = True
                elif power == 1:
                        screen.blit(e,(0,0)) #exit with lights on
                elif power != 1:
                        screen.blit(de,(0,0))
                screen.blit(ra,(1225,650))#blit arrows in
                screen.blit(la,(20,650))
                pad_button = button(850, 433, 54, 77)
                door_button = button(468, 175, 335, 610)

        elif disp == 2:#chimney
                press_dict = {'antlers': {'mx_min': 475, 'mx_max': 875, 'my_min': 20, 'my_max': 100,
                      'text': GAME_FONT.render("What a nice rack!", False, (255, 255, 255))},
                'switch': {'mx_min': 1340, 'mx_max': 1390, 'my_min': 310, 'my_max': 390,
                      'text': GAME_FONT.render("Let there be light!", False, (255, 255, 255))},
                'fireplace': {'mx_min': 330, 'mx_max': 950, 'my_min': 290, 'my_max': 630,
                      'text': GAME_FONT.render("Hhmmm, Fancy.", False, (255, 255, 255))},
                'logs': {'mx_min': 400, 'mx_max': 850, 'my_min': 640, 'my_max': 740,
                      'text': GAME_FONT.render("Wonder if there is any matches anywhere.", False, (255, 255, 255))}
                }

                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This is the background of the chimney wall"""
                if power == 1:
                    lightswitch = button(1345, 320, 40, 75)
                    if light_on == 1:
                        screen.blit(lc1,(0,0))#chimney wlight switch changed
                    if light_on != 1:
                        screen.blit(c,(0,0)) #chimney with lights on but light switch inverted
                elif power != 1:
                        screen.blit(dc,(0,0))
                log_button = button(400, 640, 450, 100)
                if fire == 1:
                    lightswitch = button(1345, 320, 40, 75)
                    if light_on == 1:
                            screen.blit(lc2,(0,0))
                    elif light_on != 1:
                            screen.blit(fc,(0,0))
                screen.blit(ra,(1225,650))#blit arrows in
                screen.blit(la,(20,650))
        
        elif disp == 3:#bookcase
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This is the background of the book wall"""
                if power == 1:
                        screen.blit(b,(0,0)) #bookcase with lights on
                        matchbook_button = button(215, 80, 30, 125) #book needed to solve button
                        book1 = button(1150, 360, 15, 100) #green book button
                        book2 = button(440,75,50,100) #book book button
                        book3333 = button(120,345,40,115) #3333 book button
                        got_button = button(925, 90, 40, 115) #GOT book button
                        black_button = button(460, 365, 30, 100) #black book button
                        hp_button = button(1040, 340, 40, 120) #hp book button
                        we_know = button(1000, 90, 30, 115) #hp book button
                elif power != 1: 
                        screen.blit(db,(0,0))
                screen.blit(ra,(1225,650))#blit arrows in
                screen.blit(la,(20,650))
        
        elif disp == 4:#piano wall
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This is the background of the piano wall"""
                key_button = button(355, 550, 40, 10)
                piano_button = button(335, 580, 640, 50)
                
                if pkey_got == 1:
                        screen.blit(dwk,(0,0)) #piano with key_got
                
                if key_placed == 1:
                        screen.blit(dcp,(0,0))#complete piano without power
                
                if power == 1:
                        screen.blit(p,(0,0)) #complete piano
                        if boot_up == 1:
                                melo.play(maxtime = 22000)#plays medium gears noise
                                pygame.time.wait(22000)
                                su.play()#plays boot up noise
                                mg.play(maxtime = 2500)#plays medium gears noise
                                pygame.time.wait(2000)
                                fg.play(maxtime = 2500)#plays fast gears noise
                                pygame.mixer.fadeout(2000) 
                                boot_up = 2
                elif power != 1 and pkey_got != 1 and key_placed != 1: 
                        screen.blit(dp,(0,0))
                screen.blit(ra,(1225,650))#blit arrows in
                screen.blit(la,(20,650))
        
        elif disp == 5:#pad
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                if power == 1:
                        screen.blit(padw,(0,0)) #pad with red light on
                        rpad = button(600, 200, 100, 150)#red button
                        gpad = button(750, 200, 100, 150)#green button
                        ypad = button(600, 380, 100, 150)#yellow button
                        bpad = button(750, 380, 100, 150)#blue button
                        if granted == 1:
                                screen.blit(padr,(0,0)) #green pad

                                

                elif power != 1:
                        screen.blit(pad,(0,0)) #dead pad
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 6:#matchbook
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(mb,(0,0))
                mbutton = button(805, 150, 70, 260)#match button
                if m_got ==  1:
                        screen.blit(emb,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 7:#3333book
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(b3,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 8:#book1
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(b1,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 9:#Game of T
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(got,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 10:#book book
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(bookbook,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 11:#black book
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(ac,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 12:#hp
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(hp,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        elif disp == 13:#we know
                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This view of the colour pad on the wall"""
                screen.blit(wk,(0,0))
                rab = button(0,0,0,0)#erases rigth arrow button
                screen.blit(la,(20,650))

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        print(pos)
                        # check mouse click against all registered coordinates
                        button_press(mx,my,text_render_queue)
                        if pad_button.isOver(pos):
                                disp = 5
                        if door_button.isOver(pos) and granted == 1:
                                player_exit = 1
                                s4.play()#plays door unlock
                                s2.play()#plays door open      
                        elif door_button.isOver(pos):
                                s3.play(maxtime = 1690)#plays handle noise
                        if key_button.isOver(pos):
                                pkey_got = 1
                        if matchbook_button.isOver(pos):
                                disp = 6
                        if book3333.isOver(pos):
                                disp = 7
                        if book1.isOver(pos):
                                disp = 8
                        if got_button.isOver(pos):
                                disp = 9
                        if book2.isOver(pos):
                                disp = 10
                        if black_button.isOver(pos):
                                disp = 11
                        if hp_button.isOver(pos):
                                disp = 12
                        if we_know.isOver(pos):
                                disp = 13
                        if mbutton.isOver(pos):#if match is clicked
                                m_got = 1
                        if log_button.isOver(pos) and m_got == 1:#if logs clicked with match
                                fire = 1
                        if lightswitch.isOver(pos) and power == 1:#if light switch is clicked
                                switch.play(maxtime = 1500)
                                if light_on == 0:
                                        light_on = 1
                                elif light_on == 1:
                                        light_on = 0


                        if piano_button.isOver(pos):
                                if key_placed == 1: #if piano is clicked after key is placed back in 
                                        power = 1
                                        boot_up += 1
                                elif pkey_got == 1: 
                                        key_placed = 1 #places key in piano

                        if disp == 5:
                                if bpad.isOver(pos) and ypress == 1:
                                        y_bpress = 1
                                elif gpad.isOver(pos) and y_bpress == 1:
                                        y_b_gpress = 1
                                elif rpad.isOver(pos) and y_b_gpress == 1:
                                        granted = 1
                                
                                if rpad.isOver(pos):
                                        rpress = 1
                                        click.play()#plays click noise
                                        counter += 1
                                elif gpad.isOver(pos):
                                        gpress = 1
                                        click.play()#plays click noise
                                        counter += 1
                                elif ypad.isOver(pos):
                                        ypress = 1
                                        click.play()#plays click noise
                                        counter += 1
                                elif bpad.isOver(pos):
                                        bpress = 1
                                        click.play()#plays click noise
                                        counter += 1
                                if counter == 4:
                                        screen.blit(pad,(0,0)) #dead pad
                                        buzz.play()#plays buzz noise
                                        counter = 0

                        #if Right arrow is clicked, changes to appropiate wall
                        if rab.isOver(pos) and disp == 1:
                                disp = 2
                        elif rab.isOver(pos) and disp == 2:
                                disp = 3
                        elif rab.isOver(pos) and disp == 3:
                                disp = 4
                        elif rab.isOver(pos) and disp == 4:
                                disp = 1

                        #if Left arrow is clicked, changes to appropiate wall
                        if lab.isOver(pos) and disp == 1:
                                disp = 4
                        elif lab.isOver(pos) and disp == 4:
                                disp = 3
                        elif lab.isOver(pos) and disp == 3:
                                disp = 2
                        elif lab.isOver(pos) and disp == 2:
                                disp = 1
                        elif lab.isOver(pos) and disp == 5: #for colorpad
                                disp = 1
                        elif lab.isOver(pos) and disp == 6: #for matchbook
                                disp = 3
                        elif lab.isOver(pos) and disp == 7: #3333 book
                                disp = 3
                        elif lab.isOver(pos) and disp == 8: #book1
                                disp = 3
                        elif lab.isOver(pos) and disp == 9: #got
                                disp = 3
                        elif lab.isOver(pos) and disp == 10: #book2 or book book
                                disp = 3
                        elif lab.isOver(pos) and disp == 11: #black book
                                disp = 3
                        elif lab.isOver(pos) and disp == 12: #hp
                                disp = 3
                        elif lab.isOver(pos) and disp == 13: #hp
                                disp = 3

                if event.type == pygame.MOUSEMOTION:
                        #if cursor is over any clickable objects changes cursor
                        if rab.isOver(pos) or lab.isOver(pos) or door_button.isOver(pos) or pad_button.isOver(pos) or key_button.isOver(pos) or piano_button.isOver(pos) or matchbook_button.isOver(pos) or mbutton.isOver(pos) or rpad.isOver(pos) or gpad.isOver(pos) or ypad.isOver(pos) or bpad.isOver(pos) or lightswitch.isOver(pos) or book3333.isOver(pos) or book1.isOver(pos) or got_button.isOver(pos) or book2.isOver(pos) or black_button.isOver(pos) or hp_button.isOver(pos) or we_know.isOver(pos):
                                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        elif rab.isOver(pos) != True or lab.isOver(pos) != True or door_button.isOver(pos) != True or pad_button.isOver(pos) != True or key_button.isOver(pos) != True or piano_button.isOver(pos) != True or matchbook_button.isOver(pos) != True or mbutton.isOver(pos) != True or rpad.isOver(pos) != True or gpad.isOver(pos) != True or ypad.isOver(pos) != True or bpad.isOver(pos) != True or lightswitch.isOver(pos) != True or book3333.isOver(pos) != True or book1.isOver(pos) != True or got_button.isOver(pos) != True or book2.isOver(pos) != True or black_button.isOver(pos) != True or hp_button.isOver(pos) != True or we_know.isOver(pos) != True:
                                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        
        pygame.display.flip()
        clock.tick(60)

while Outro2 and done == True:
#second outro loop
    gameDisplay = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('ERS')#caption of display window
                
    gameDisplay.fill(black) #background
    text = GAME_FONT.render("Congrats, you made it through the second level!", False, (255, 255, 255))
    gameDisplay.blit(text, (355,390))
    t2 = GAME_FONT.render("Press space to quit.", False, (255, 255, 255))
    gameDisplay.blit(t2, (1060,750))
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.quit()
            quit()
             

    pygame.display.flip()
    clock.tick(60)
