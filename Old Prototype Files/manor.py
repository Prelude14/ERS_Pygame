import pygame
import time


pygame.init()
done = False
disp = 1
key_got = 0
m_got = 0
key_placed = 0
boot_up = 0
power = 0
fire = 0
rpress = 0
gpress = 0
ypress = 0
bpress = 0
counter = 0
y_bpress = 0
y_b_gpress = 0

#mouse cursor and mouse coordinates
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
GAME_FONT = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()


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


press_dict = {}
text_render_queue = {}

def button_press(mx,my,text_render_queue,press_dict=press_dict):
        """Function that checks coords of mouse click against dictionary
        of known events and then adds them to the render queue
        
        modifies press_dict"""

        for key in press_dict:
                if press_dict[key]['mx_min']<=mx<=press_dict[key]['mx_max'] and press_dict[key]['my_min']<=my<=press_dict[key]['my_max']:
                        #print('caught the button press {}'.format(key))
                        text_render_queue[key] = {'text':press_dict[key]['text'],
                                                  'ticks':50,
                                                  # we could add more properties either constant
                                                  # or specific to interaction
                                                  }

def render_text(text_render_queue):
        del_list = []
        for key in text_render_queue:
                if text_render_queue[key]['ticks'] >= 0:
                        # render text to screen
                        screen.blit(text_render_queue[key]['text'],
                                    (110,10) )
                        # decrease the number of ticks left
                        text_render_queue[key]['ticks'] -= 1
                        # This seems redundant, I suspect we can
                        # move it outside the for-loop
                        pygame.display.update() 
                else:
                        # Remove that entry from the queue
                        # text_render_queue.pop(key)
                        # This doesn't actually work, Error:
                        # RuntimeError: dictionary changed size during iteration
                        del_list.append(key)

        [text_render_queue.pop(key) for key in del_list]

while not done:
        ra = pygame.image.load("rarrow.png")#arrows
        lab = button(30,675,140,125)
        la = pygame.image.load("larrow.png")
        rab = button(1230,665,140,125)
        
        e = pygame.image.load("exit.png")#reg versions
        pad_button = button(0,0,0,0) #placeholder for button
        door_button = button(0,0,0,0) #placeholder for button
        c = pygame.image.load("chim.png")
        fc = pygame.image.load("fchim.png")
        log_button = button(0,0,0,0)
        b = pygame.image.load("book.png")
        matchbook_button = button(0,0,0,0) #placeholder for button
        mb = pygame.image.load("mbook.png") #matchbook buttons
        mbutton = button(0,0,0,0) #placeholder
        emb = pygame.image.load("embook.png")
        book1_button = button(0,0,0,0) #placeholder for button
        book2_button = button(0,0,0,0) #placeholder for button
        p = pygame.image.load("piano.png")
        key_button = button(0,0,0,0) #placeholder for button
        piano_button = button(0,0,0,0) #placeholder for button
        
        dc = pygame.image.load("dchim.png")#dark versions
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
        click = pygame.mixer.Sound('click.wav')
        buzz = pygame.mixer.Sound('buzz.wav')

        if disp == 1:#exit
                press_dict = {'door': {'mx_min': 468, 'mx_max': 803, 'my_min': 175, 'my_max': 785,
                        'text': GAME_FONT.render("Looks like the doors locked again", False, (255, 255, 255))}
                }

                screen = pygame.display.set_mode((1400, 800))
                pygame.display.set_caption('ERS')#caption of display window
                """This is the background of the first wall"""
                if power == 1:
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
                        screen.blit(c,(0,0)) #chimney with lights on
                elif power != 1:
                        screen.blit(dc,(0,0))
                log_button = button(400, 640, 450, 100)
                if fire == 1:
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
                        book1_button = button(1150, 360, 15, 100) #green book button
                        book2_button = button(440,75,50,30) #book book button
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
                if key_got == 1:
                        screen.blit(dwk,(0,0)) #piano with key_got
                
                if key_placed == 1:
                        screen.blit(dcp,(0,0))#complete piano without power
                
                if power == 1:
                        screen.blit(p,(0,0)) #complete piano
                        if boot_up == 1:
                                su.play()#plays boot up noise
                                mg.play(maxtime = 2500)#plays medium gears noise
                                pygame.time.wait(2000)
                                fg.play(maxtime = 2500)#plays fast gears noise
                                pygame.mixer.fadeout(2000) 
                                boot_up = 2
                elif power != 1: 
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

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        print(pos)
                        # check mouse click against all registered coordinates
                        button_press(mx,my,text_render_queue)
                        if pad_button.isOver(pos):
                                disp = 5
                        if door_button.isOver(pos):
                                s3.play(maxtime = 1690)#plays handle noise
                        if key_button.isOver(pos):
                                key_got = 1
                        if matchbook_button.isOver(pos):
                                disp = 6
                        if mbutton.isOver(pos):#if match is clicked
                                m_got = 1
                        if log_button.isOver(pos) and m_got == 1:#if logs clicked with match
                                fire = 1

                        if piano_button.isOver(pos):
                                if key_placed == 1: #if piano is clicked after key is placed back in 
                                        power = 1
                                        boot_up += 1
                                        #ps.play() #plays piano clip
                                elif key_got == 1: 
                                        key_placed = 1 #places key in piano

                        if disp == 5:
                                if bpad.isOver(pos) and ypress == 1:
                                        y_bpress = 1
                                elif gpad.isOver(pos) and y_bpress == 1:
                                        y_b_gpress = 1
                                elif rpad.isOver(pos) and y_b_gpress == 1:
                                        done = True
                                        Outro = True
                                
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

                if event.type == pygame.MOUSEMOTION:
                        #if cursor is over any clickable objects changes cursor
                        if rab.isOver(pos) or lab.isOver(pos) or door_button.isOver(pos) or pad_button.isOver(pos) or key_button.isOver(pos) or piano_button.isOver(pos) or matchbook_button.isOver(pos) or mbutton.isOver(pos) or rpad.isOver(pos) or gpad.isOver(pos) or ypad.isOver(pos) or bpad.isOver(pos):
                                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        elif rab.isOver(pos) != True or lab.isOver(pos) != True or door_button.isOver(pos) != True or pad_button.isOver(pos) != True or key_button.isOver(pos) != True or piano_button.isOver(pos) != True or matchbook_button.isOver(pos) != True or mbutton.isOver(pos) != True or rpad.isOver(pos) != True or gpad.isOver(pos) != True or ypad.isOver(pos) != True or bpad.isOver(pos) != True:
                                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        # render text in the queue
        render_text(text_render_queue)
        
        pygame.display.flip()
        clock.tick(60)

while Outro:
#outro loop
    gameDisplay = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('ERS')#caption of display window
                
    gameDisplay.fill(black) #background
    text = GAME_FONT.render("Oh look, you made it through the second level!", False, (255, 255, 255))
    gameDisplay.blit(text, (355,390))
    t2 = GAME_FONT.render("Press space to quit.", False, (255, 255, 255))
    gameDisplay.blit(t2, (980,750))
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            Outro = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Outro = False
            

    pygame.display.flip()
    clock.tick(60)
