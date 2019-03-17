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

press_dict = {'bed': {'mx_min': 850, 'mx_max': 1270, 'my_min': 570, 'my_max': 680,
                      'text': GAME_FONT.render("This bed reminds me of something, but I can't quite put my finger on it.", False, (255, 255, 255))},
                'door': {'mx_min': 400, 'mx_max': 550, 'my_min': 310, 'my_max': 610,
                      'text': GAME_FONT.render("This door is locked.", False, (255, 255, 255))},
                'key': {'mx_min': 610, 'mx_max': 640, 'my_min': 350, 'my_max': 410,
                      'text': GAME_FONT.render("FRREEEEEDDOOOM!!!!", False, (255, 255, 255))},
                'ceiling': {'mx_min': 0, 'mx_max': 1400, 'my_min': 0, 'my_max': 115,
                      'text': GAME_FONT.render("That's weird, there are no lights in this room.", False, (255, 255, 255))}
}
             

# This text render queue will hold a dict with the text object to be displayed
# as well as the number of game ticks it will be displayed
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

# This contains the actions and locations for all interaction related to clicking
# Will likely need better key names, or unique keys. This might also all be
# better done using object, but I will let you decide.
# press_dict contains dictionaires of the expected format:
# {'mx_min': ,
#  'mx_max': ,
#  'my_min': ,
#  'my_max': ,
#  'text': ,
#  #'ticks':200, # this could also be specified specifically for each interaction
# }


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
        ## cleanup
        # Use list comprehension to loop fast
        [text_render_queue.pop(key) for key in del_list]

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
                        button_press(mx,my,text_render_queue)
                        
        
        # render text in the queue
        render_text(text_render_queue)
        print('text_render_queue:',text_render_queue)
        
        pygame.display.flip()
        clock.tick(60)
