#Discipuli 1.9.3 Home Design

import pygame
import time
import random
import pygame as pg


pygame.init()

display_height = 600
display_width = 1000

pygame.display.set_caption('Discipuli 1.9.3 - Demo Version')
screen = pygame.display.set_mode((display_width,display_height))

img = pygame.image.load('brain.jpg')
pygame.display.set_icon(img)

Aqua = (0,255,255)
Black = (0, 0, 0)
Blue = (0, 0, 150)
light_blue = ( 0, 0, 255)
Fuchsia = ( 255, 0, 255)
Gray = ( 128, 128, 128)
Lime = (  0, 255,   0)
Maroon = (128,  64,   64)
light_maroon = (185,  122,   87)
Navy_Blue = (  0,  0, 128)
Olive = (128, 128,   0)
Purple = (128,  0, 128)
light_purple = (255,  0, 255)
Silver = (192, 192, 192)
bright_silver = (200,200, 200)
Teal = (  0, 128, 128)
bright_teal = (  0, 200, 200)
White = (255, 255, 255)
bright_yellow = (255, 255,   0)
Yellow = (120, 120,   0)
Red = (150, 0, 10)
Green = (0, 150, 10)
bright_green =(0, 250, 0)
bright_red = (250, 0, 0)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def gosign():
    pygame.draw.circle(screen, White, (327, 225), 10, 3)
    pygame.draw.line(screen, White, (322, 220), (335, 224), 3)
    pygame.draw.line(screen, White, (322, 230), (335, 224), 3)

    
clock = pygame.time.Clock()

def starter():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Black)

        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects('Introducing Discipuli 1.9.3', largeText)
        TextRect.center = ((display_width/2),(450))
        screen.blit(TextSurf, TextRect)
        message_display('WELCOME USER')
        
        pygame.display.update()
        clock.tick(65)

def powered():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Black)

        largeText = pygame.font.SysFont('Callibri',50)
        TextSurf, TextRect = text_objects('...Expanding & Exploring Horizons', largeText)
        TextRect.center = ((display_width/2),(450))
        screen.blit(TextSurf, TextRect)
        message_display2('POWERED BY MEDITATI')
        
        pygame.display.update()
        clock.tick(65)
        
def HomeWindow():
    SignedIn  = True
    start = True

    gobutts = pygame.draw.rect(screen, Green,(900,550,100,50))
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gobutts.collidepoint(event.pos):
                    NextWindow()
                else:
                    Daniel = 'Boss'

        screen.fill(Black)
        
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects3('DASHBOARD', largeText)
        TextRect.center = ((display_width/2),(50))
        screen.blit(TextSurf, TextRect)
        
        def button_edit(msg1,msg2,x,y,w,h,ic,ac, action = None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(screen, ac,(x,y,w,h))
                try:
                    if click[0] == 1 and action != None:
                        if action == 'biology':
                            biology()
                        elif action == 'chemistry':
                            chemistry()
                        elif action == 'physics':
                            physics()
                        elif action == 'economics':
                            economics()
                        elif action == 'geography':
                            geography()
                        elif action == 'mathematics':
                            mathematics()
                        else:
                            quit()
                except:
                     pygame.draw.rect(screen, Black, (0, 100, 1000,500))
                     message_display_alternative('This Feature Is Not Yet Available')
            else:
                pygame.draw.rect(screen, ic,(x,y,w,h))
                    
                        
            smallText = pygame.font.Font("freesansbold.ttf",60)
            textSurf, textRect = text_objects3(msg1, smallText)
            textRect.center = ( (x+(w/2)), ((y+(h/2)) - 40) )
            screen.blit(textSurf, textRect)

            smallText = pygame.font.Font("freesansbold.ttf",25)
            textSurf, textRect = text_objects3(msg2, smallText)
            textRect.center = ( (x+(w/2)), ((y+(h/2)) + 50) )
            screen.blit(textSurf, textRect)

        button_edit('0610','Biology',93,100,140,150,Green,bright_green, 'biology')
        button_edit('0620','Chemistry',426,100,140,150,Red,bright_red, 'chemistry')
        button_edit('0625','Physics',759,100,140,150,Blue,light_blue, 'physics')
        button_edit('0455','Economics',93,350,140,150,Purple,light_purple, 'economics')
        button_edit('0460','Geography',426,350,140,150,Yellow,bright_yellow, 'geography')
        button_edit('0580','Math',759,350,140,150,Maroon,light_maroon, 'mathematics')

        pygame.draw.rect(screen, Green,(900,550,100,50))
        
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurf, textRect = text_objects3('...', smallText)
        textRect.center = ( (900+(100/2)), ((550+(50/2))) )
        screen.blit(textSurf, textRect)

        pygame.draw.line(screen, White, (0, 200), (1000, 200), 3)
        pygame.draw.line(screen, Black, (0, 200), (93, 200), 3)
        pygame.draw.line(screen, Black, (233, 200), (426, 200), 3)
        pygame.draw.line(screen, Black, (566, 200), (759, 200), 3)
        pygame.draw.line(screen, Black, (899, 200), (1000, 200), 3)

        pygame.draw.line(screen, White, (0, 450), (1000, 450), 3)
        pygame.draw.line(screen, Black, (0, 450), (93, 450), 3)
        pygame.draw.line(screen, Black, (233, 450), (426, 450), 3)
        pygame.draw.line(screen, Black, (566, 450), (759, 450), 3)
        pygame.draw.line(screen, Black, (899, 450), (1000, 450), 3)

        avatar = pygame.image.load('avatar.png')
        avatar = pygame.transform.scale(avatar, (55, 35))      
        screen.blit(avatar, (930, 10))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 930+55 > mouse[0] > 930 and 10+35 > mouse[1] > 10:
            if click[0] == 1:
                print('Daniel')
                SignedIn = not SignedIn
                if SignedIn == True:                   
                    message_displayz('Activated')
                elif SignedIn == False:
                    pygame.draw.rect(screen, Black, (0, 100, 1000,500))
                    message_displayz('De-Activated (5s)')
                else:
                    Dave = 'Boss'
        else:
            Daniel = 'Boss'
        
        pygame.display.update()
        clock.tick(65)

def NextWindow():
    SignedIn  = True
    start = True

    backbutts = pygame.draw.rect(screen, Red,(0,550,100,50))

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutts.collidepoint(event.pos):
                    HomeWindow()
                else:
                    Daniel = 'Boss'

        screen.fill(Black)

        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects3('DASHBOARD', largeText)
        TextRect.center = ((display_width/2),(50))
        screen.blit(TextSurf, TextRect)

        def button(msg1,msg2,x,y,w,h,ic,ac, action = None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(screen, ac,(x,y,w,h))
                if click[0] == 1 and action != None:
                    if action == 'ict':
                        ict()
                    elif action == 'addmath':
                        addmath()
            else:
                pygame.draw.rect(screen, ic,(x,y,w,h))
                    
                        
            smallText = pygame.font.Font("freesansbold.ttf",60)
            textSurf, textRect = text_objects3(msg1, smallText)
            textRect.center = ( (x+(w/2)), ((y+(h/2)) - 40) )
            screen.blit(textSurf, textRect)

            smallText = pygame.font.Font("freesansbold.ttf",25)
            textSurf, textRect = text_objects3(msg2, smallText)
            textRect.center = ( (x+(w/2)), ((y+(h/2)) + 50) )
            screen.blit(textSurf, textRect)

        button('0417','ICT',93,100,140,150,Silver,bright_silver, 'ict')
        button('0606','Add. Math',426,100,140,150,Teal,bright_teal, 'addmath')

        pygame.draw.line(screen, White, (0, 200), (1000, 200), 3)
        pygame.draw.line(screen, Black, (0, 200), (93, 200), 3)
        pygame.draw.line(screen, Black, (233, 200), (426, 200), 3)
        pygame.draw.line(screen, Black, (566, 200), (1000, 200), 3)
        pygame.draw.line(screen, Black, (899, 200), (1000, 200), 3)

        pygame.draw.rect(screen, Red,(0,550,100,50))
        
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurf, textRect = text_objects3('...', smallText)
        textRect.center = ( (0+(100/2)), ((550+(50/2))) )
        screen.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(65)

def text_objects(text, font):
    textSurface = font.render(text, True, Aqua)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def text_objects3(text, font):
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

    powered()

def message_displayz(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(10)

def message_display2(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

    HomeWindow()

def message_display_alternative(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

def geography():
    #Cross-Platform Testing Here#
    #Fix Bugs.
    #Source: C:\Users\User\Desktop\stuff\Daniel Eta\The Discipuli Project\Source Codes\G0460 - Ch1
    #Going to make a pretty neat function
    img = pygame.image.load('brain.jpg')
    pygame.display.set_icon(img)

    frcarImg = pygame.image.load('brain-exercise.png')
    carImg = pygame.transform.scale(frcarImg, (80, 60))

    bulb = pygame.image.load('bulb.png')
    bulbtrans = pygame.transform.scale(bulb, (40, 30))

    car_width = 73
    car_height = 73

    def car(x,y):
        screen.blit(carImg,(x,y))

    def bulbdsp(thingx, thingy, thingw, thingh):
        screen.blit(bulbtrans, [thingx, thingy, thingw, thingh])

    Aqua = (0,255,255)
    Black = (0, 0, 0)
    Blue = ( 0, 0, 255)
    Fuchsia = ( 255, 0, 255)
    Gray = ( 128, 128, 128)
    Lime = (  0, 255,   0)
    Maroon = (128,  0,   0)
    Navy_Blue = (  0,  0, 128)
    Olive = (128, 128,   0)
    Purple = (128,  0, 128)
    Silver = (192, 192, 192)
    Teal = (  0, 128, 128)
    White = (255, 255, 255)
    Yellow = (255, 255,   0)
    Red = (150, 0, 10)
    Green = (0, 150, 10)
    bright_green =(0, 250, 0)
    bright_red = (250, 0, 0)

    clock = pygame.time.Clock()

    #Going to make a pretty neat function
    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            
    def g_win1_ch1():

        start = True

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)
            font2 = pygame.font.SysFont('Cooper Black', 25)
            largeText = pygame.font.Font('freesansbold.ttf',40)
            TextSurf, TextRect = text_objects('Population Dynamics - Introduction', largeText)
            TextRect.center = ((display_width/2),(30))
            screen.blit(TextSurf, TextRect)

            someimg = pygame.image.load('verybusystreet.jpg')
            someimg_2 = pygame.transform.scale(someimg, (500, 200))
            screen.blit(someimg_2, (0, 75))

            stxt = 'Population is a term used to describe the number inhabitants in a particular region/area. The picture to your left shows a very busy street in Hong Kong. Suppose, the number of people in Hong Kong was 7 million, then it could be said that the population of Hong Kong was 7 million. In a nutshell, population is the number of people in a city or town, region, country or world; population is usually determined by a process called census (a process of collecting, analyzing, compiling and publishing data).'
            blit_text(screen, stxt, (505, 75), font, color=pygame.Color('black'))

            stxt2 = 'Population is a big deal in many countries as it plays a huge role in indicating the development and progress in that country. In the upcoming lessons, we would learn how to analyse the population trends in various countries. We would also learn various factors that affect population growth. We would also study different methods of population control to develop an optimum population.'
            stxt3 = 'The world population is growing at about 88 million people each year. However, the population growth in various countries differ significantly. The rapid growth of population in some countries is referred to as POPULATION EXPLOSION. However, in some IGCSE questions, you may be asked to calculate the natural population change as well as the overall population change. In those scenarios, you may use these formulae: '

            calca = 'Natural Population Change = Birth Rate - Death Rate'
            calcb = 'Overall Population Change = Birth Rate - Death Rate +/- Migration'

            blit_text(screen, calca, ((20),(350)), font2, color=pygame.Color('blue'))
            blit_text(screen, calcb, ((20),(390)), font2, color=pygame.Color('blue'))
            
            blit_text(screen, stxt3, (20, 280), font, color=pygame.Color('black'))
            blit_text(screen, stxt2, (20, 430), font, color=pygame.Color('black'))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_qwindow1_ch1()
                        elif action == 'Quit':
                            g_intro_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_intro_ch1():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects('Geography(0460)', largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRect)

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win1_ch1()
                        elif action == 'Quit':
                            pygame.quit()
                            quit()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('START', 650, 450, 100, 50, Green, bright_green, 'Play')
            button('QUIT', 250, 450, 100, 50, Red, bright_red, 'Quit')

            smalltext = pygame.font.Font('freesansbold.ttf', 50)
            smallsurf, smallrect = text_objects('Population: Structure & Interpretation', smalltext)
            smallrect.center = ((display_width/2),(display_height/1.5))
            screen.blit(smallsurf, smallrect)

            pygame.display.update()
            clock.tick(15)

    def g_qwindow1_ch1():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Which Sentence Correctly Defines Population?', largeText)
            TextRect.center = ((display_width/2),(50))
            screen.blit(TextSurf, TextRect)

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'ans1':
                            correct = True
                            message_display_cr('Correct')
                            g_win2_ch1()
                        elif action == 'ans2':
                            correct = False
                            message_display_ir('Wrong')
                            g_win2_ch1()
                        elif action == 'ans3':
                            correct = False
                            message_display_ir('Wrong')
                            g_win2_ch1()
                        elif action == 'Play':
                            g_win2_ch1()
                        elif action == 'Back':
                            g_win1_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('The number of people in a city or town, region, country or world',100,100,800,75,Silver,Teal, 'ans1')       
            button('The method used to organize data on the inhabitants of a country',100,400,800,75,Silver,Teal, 'ans2')       
            button('The different races of people in a particular region',100,250,800,75,Silver,Teal, 'ans3')


            pygame.display.update()
            clock.tick(15)

    def text_objects(text, font):
        textSurface = font.render(text, True, Black)
        return textSurface, textSurface.get_rect()

    def text_objects_white(text, font):
        textSurface = font.render(text, True, White)
        return textSurface, textSurface.get_rect()

    def text_objects_green(text, font):
        textSurface = font.render(text, True, Green)
        return textSurface, textSurface.get_rect()

    def text_objects_red(text, font):
        textSurface = font.render(text, True, Red)
        return textSurface, textSurface.get_rect()

    #cr = Correct
    #ir = Incorrect

    def message_display_cr(text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects_green(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

    def message_display_cr_edit(text):
        largeText = pygame.font.Font('freesansbold.ttf',35)
        TextSurf, TextRect = text_objects_green(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

        

    def message_display_ir(text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects_red(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

    def message_display_ir_edit(text):
        largeText = pygame.font.Font('freesansbold.ttf',35)
        TextSurf, TextRect = text_objects_red(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

    def message_display_ir_edit_edit(text):
        largeText = pygame.font.Font('freesansbold.ttf',35)
        TextSurf, TextRect = text_objects_red(text, largeText)
        TextRect.center = ((display_width/2),(350))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

    def message_display_ir_edit_edit_edit(text):
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects_red(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(5)

    def g_win2_ch1():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Population Dynamics - Patterns', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            someimg = pygame.image.load('World_population_percentage.png')
            someimg_2 = pygame.transform.scale(someimg, (1000, 600))
            screen.blit(someimg_2, (0, 0))
            
            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win3_ch1()
                        elif action == 'Quit':
                            g_qwindow1_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_win3_ch1():
        
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            stxt = 'Physical Factors: Physical factors that affect population distribution include altitude and latitude, relief, climate, soils, vegetation, water and location of mineral and energy resources. It is important to note that most of the physical factors influence population distribution only indirectly through climatic conditions. Favourable Climates that help with crop production, and weather usually attract people.'
            stxt2 = 'Economic Factors: The population may be drastically affected by the economic performance. If there is constant recession and inflation, people tend to migrate, thus having a negative effect on the population.'
            stxt3 = 'Available Resources: If a country has a wide range of resources and minerals, the population there would inevitably increase. This is because there are now new oppurtunities to gain income and livelihood.'
            stxt4 = 'Political Factors: The government and politics may also play a pivotal role in a country\'s population. Some individuals prefer some sort of political strategy over the other. This can and may influence their living area. For example, some capitalist governments gain a higher population because most people favour that government type.'

            blit_text(screen, stxt, (20, 20), font, color=pygame.Color('black'))
            blit_text(screen, stxt2, (20, 100), font, color=pygame.Color('black'))
            blit_text(screen, stxt3, (20, 150), font, color=pygame.Color('black'))
            blit_text(screen, stxt, (20, 200), font, color=pygame.Color('black'))

            someimg = pygame.image.load('pdistribution.gif')
            someimg2 = pygame.transform.scale(someimg, (450, 250))
            screen.blit(someimg2, (0, 290))

            stxtalt = 'As you saw in this diagram, the population density of countries may vary greatly due to some of the above factors. These factors, however may be controlled to achieve an optimum population.'
            blit_text(screen, stxtalt, (450, 290), font, color=pygame.Color('black'))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win4_ch1()
                        elif action == 'Quit':
                            g_win2_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 700, 400, 100, 50, Green, bright_green, 'Play')
            button('BACK', 600, 400, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_win4_ch1():
        
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)
            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('UNDERPOPULATION & OVERPOPULATION', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'For somewhere to be referred to as underpopulated, it means that there a country has declined so much that it can’t support its economic system. On the other hand, a country can be overpopulated when there are too little resources to meet the population\'s needs. An overpopulated area may also be extremely crowded. If a country is declared under/overpopulated, there may be some consequences...'
            blit_text(screen, txt, (20, 50), font, color=pygame.Color('black'))

            sip = pygame.image.load('someimportedpic.png')
            #sip2 = pygame.transform.scale(sip, (1000, 250))
            #Edit
            screen.blit(sip, (100, 130))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win5_ch1()
                        elif action == 'Quit':
                            g_win3_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_win5_ch1():
        font = pygame.font.SysFont('comicsansms', 25)
        input_box = pg.Rect(380, 120, 70, 40)
        input_box2 = pg.Rect(150, 200, 70, 40)
        input_box3 = pg.Rect(550, 250, 70, 40)
        input_box4 = pg.Rect(150, 330, 70, 40)
        color_inactive = pg.Color('lightskyblue3')
        color_inactive2 = pg.Color('lightskyblue3')
        color_inactive3 = pg.Color('lightskyblue3')
        color_inactive4 = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color_active2 = pg.Color('dodgerblue2')
        color_active3 = pg.Color('dodgerblue2')
        color_active4 = pg.Color('dodgerblue2')
        color = color_inactive
        color2 = color_inactive
        color3 = color_inactive
        color4 = color_inactive
        active = False
        active2 = False
        active3 = False
        active4 = False
        text = ''
        text2 = ''
        text3 = ''
        text4 = ''
        check = pygame.draw.rect(screen, Green,(950, 550, 50, 50)) 

        #Question Window
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
    ###             
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active                
                    elif input_box2.collidepoint(event.pos):
                        # Toggle the active variable.
                        active2 = not active2
                    elif input_box3.collidepoint(event.pos):
                        # Toggle the active variable.
                        active3 = not active3
                    elif input_box4.collidepoint(event.pos):
                        # Toggle the active variable.
                        active4 = not active4
    ###
    ###
                    elif input_box.collidepoint(event.pos) != True:
                        active = False
                    # Change the current color of the input box.
                    elif input_box2.collidepoint(event.pos) != True:
                        active2 = False
                    # Change the current color of the input box.
                    elif input_box3.collidepoint(event.pos) != True:
                        active3 = False
                    # Change the current color of the input box.
                    elif input_box4.collidepoint(event.pos) != True:
                        active4 = False
                    # Change the current color of the input box.
    ###
                    else:
                        print('Daniel is a boss!!!')

                    color4 = color_active4 if active4 else color_inactive4
                    color3 = color_active3 if active3 else color_inactive3
                    color2 = color_active2 if active2 else color_inactive2
                    color = color_active if active else color_inactive
                                      
                elif event.type == pygame.KEYDOWN:
                    if active2:
                        if event.key == pygame.K_RETURN:
                            print(text2)
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode###
                    elif active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode###
                    elif active3:
                        if event.key == pygame.K_RETURN:
                            print(text3)
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode###
                    elif active4:
                        if event.key == pygame.K_RETURN:
                            print(text4)
                        elif event.key == pygame.K_BACKSPACE:
                            text4 = text4[:-1]
                        else:
                            text4 += event.unicode###

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check.collidepoint(event.pos):

                        texta = text.lower()
                        textb = text2.lower()
                        textc = text3.lower()
                        textd = text4.lower()

                        pointa = 0
                        pointb = 0
                        pointc = 0
                        pointd = 0

                        if texta == 'decrease':
                            pointa += 1
                        if textb == 'shortage':
                            pointb += 1
                        if textc == 'low':
                            pointc += 1
                        if textd == 'inflation':
                            pointd += 1

                        tpoints = pointa + pointb + pointc + pointd
                        if tpoints > 2:
                            together = 'You got ', str(tpoints), ' out of 4'
                            togetheragain = ''.join(together)
                            message_display_cr(togetheragain)
                            g_win6_ch1()
                        else:
                            together = 'You got ', str(tpoints), ' out of 4'
                            togetheragain = ''.join(together)
                            message_display_ir(togetheragain)
                            g_win6_ch1()
                     

            screen.fill(White)
            font2 = pygame.font.SysFont('comicsansms', 30)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Complete the gaps', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            stxt = 'When a country is overpopulated the \n number of jobs \n However, in an underpopulated region there will be a                                  of workers. \n The GDP is also likely to be \n Finally, in an overpopulated region, there may be\n                      due to excess demand.'
            blit_text(screen, stxt, (150, 70), font2, color=pygame.Color('black'))

            pygame.draw.rect(screen, Silver, (150, 400, 700, 100))

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('WORD BANK', largeText)
            TextRect.center = ((display_width/2),(420))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('inflation, low, shortage, decrease', largeText)
            TextRect.center = ((display_width/2),(475))
            screen.blit(TextSurf, TextRect)
    #Box1
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)
    #Box1<END>
    #Box2
            # Render the current text.
            txt_surface2 = font.render(text2, True, color2)
            # Resize the box if the text is too long.
            width2 = max(200, txt_surface2.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box2.w = width2
            # Blit the text.
            screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color2, input_box2, 2)
    #Box2<END>
    #Box3
            # Render the current text.
            txt_surface3 = font.render(text3, True, color3)
            # Resize the box if the text is too long.
            width3 = max(200, txt_surface3.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box3.w = width3
            # Blit the text.
            screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color3, input_box3, 2)
    #Box3<END>
    #Box4
            # Render the current text.
            txt_surface4 = font.render(text4, True, color4)
            # Resize the box if the text is too long.
            width4 = max(200, txt_surface4.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box4.w = width4
            # Blit the text.
            screen.blit(txt_surface4, (input_box4.x+5, input_box4.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color4, input_box4, 2)
    #Box4<END>
            
            #Cover box blemishes
            pygame.draw.line(screen, White, (380, 120), (380, 160), 5)
            pygame.draw.line(screen, White, (380, 120), (580, 120), 5)
            pygame.draw.line(screen, White, (580, 160), (580, 120), 5)

            pygame.draw.line(screen, White, (150, 200), (150, 240), 5)
            pygame.draw.line(screen, White, (150, 200), (350, 200), 5)
            pygame.draw.line(screen, White, (350, 240), (350, 200), 5)

            pygame.draw.line(screen, White, (550, 250), (550, 290), 5)
            pygame.draw.line(screen, White, (550, 250), (750, 250), 5)
            pygame.draw.line(screen, White, (750, 290), (750, 250), 5)

            pygame.draw.line(screen, White, (150, 330), (150, 370), 5)
            pygame.draw.line(screen, White, (150, 330), (350, 330), 5)
            pygame.draw.line(screen, White, (350, 370), (350, 330), 5)

            pygame.draw.rect(screen, Green, (950, 550, 100, 50))

            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects('GO', smallText)
            textRect.center = ( (950+(50/2)), (550+(50/2)) )
            screen.blit(textSurf, textRect)

            pygame.display.update()

            clock.tick(60)

    def g_win6_ch1():
        
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Why might poplation explosion occur?', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'Over the centuries, we may have discovered different areas and countries that have experienced a very rapid population growth. Through research and study, we may have discovered why the population may increase significantly in such a short time frame.'
            blit_text(screen, txt, (20, 50), font, color=pygame.Color('black'))
            txt2 = 'This is a huge concern and most governments tend to pinpoint these reasons so that a remedy is reached.Press next to see some reasons why...  '
            
            blit_text(screen, txt2, (20, 500), font, color=pygame.Color('black'))       

            sip = pygame.image.load('rpg.jpg')
            sip2 = pygame.transform.scale(sip, (1000, 400))
            screen.blit(sip2, (0, 100))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win7_ch1()
                        elif action == 'Quit':
                            g_win5_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 500, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 400, 550, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)

    def g_win7_ch1():

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            sip = pygame.image.load('mypicit.png')
            screen.blit(sip, (200, 75))
            
            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win8_ch1()
                        elif action == 'Quit':
                            g_win6_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)

    def g_win8_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(Black)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects_white('Some Key Terms', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            kt1 = pygame.image.load('keyterms1.png')
            screen.blit(kt1, (200, 50))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win9_ch1()
                        elif action == 'Quit':
                            g_win7_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('...', 900, 0, 100, 50, Green, bright_green, 'Play')
            button('...', 0, 0, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)

    def g_win9_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(Black)

            kt1 = pygame.image.load('keyterms2.png')
            screen.blit(kt1, (200, 50))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win10_ch1()
                        elif action == 'Quit':
                            g_win8_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('...', 500, 550, 100, 50, Green, bright_green, 'Play')
            button('...', 400, 550, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)


    def g_win10_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Why are there high death rates in LEDCs?', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            img = pygame.image.load('poorafrica.jpg')
            img2 = pygame.transform.scale(img, (1000, 300))
            screen.blit(img2, (0, 50))
            txt = 'It is said that, most underdeveloped countries have very high death rates. In geography, we find reasons behind common world events and phenomenom. In this lecture, we would talk about why there are so many deaths in LEDCs.'
            blit_text(screen, txt, (20, 350), font, color=pygame.Color('black'))

            apic = pygame.image.load('anothapic.png')
            screen.blit(apic, (150, 400))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win11_ch1()
                        elif action == 'Quit':
                            g_win9_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)

    def g_win11_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Why are there low birth rates in MEDCs?', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'Another common trend is the fact that there are very low birth rates in MEDCs, of course, like any other trend, there would be reasons...'
            blit_text(screen, txt, (20, 350), font, color=pygame.Color('black'))

            img = pygame.image.load('apic7.jpg')
            img2 = pygame.transform.scale(img, (1000, 300))
            screen.blit(img2, (0, 50))

            imga = pygame.image.load('anothapic2.png')
            screen.blit(imga, (150, 380))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win12_ch1()
                        elif action == 'Quit':
                            g_win10_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 0, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 0, 100, 50, Red, bright_red, 'Quit')

            pygame.display.update()

            clock.tick(60)

    def g_win12_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Migration', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            img = pygame.image.load('migrants.jpg')#
            img2 = pygame.transform.scale(img, (700, 300))
            screen.blit(img2, (0, 40))

            apic = pygame.image.load('migrpic.png')#
            #apica = pygame.transform.scale(apic, (1000, 300))
            screen.blit(apic, (150, 350))

            txt = 'When people move from one region or country to another due to some specific reasons, it is referred to as migration. People migrate for different reasons. These reasons however may classify what type of migrant the person is. Some types of migration are specified below: '
            blit_text(screen, txt, (710, 40), font, color=pygame.Color('black'))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win13_ch1()
                        elif action == 'Quit':
                            g_win11_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_win13_ch1():
            
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('PUSH & PULL FACTORS', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)
            
            font = pygame.font.SysFont('comicsansms', 15)

            img = pygame.image.load('pushpull2.jpg')
            img2 = pygame.transform.scale(img, (500, 200))
            screen.blit(img2, (0, 50))

            apic = pygame.image.load('pullfactor.jpg')
            apic2 = pygame.transform.scale(apic, (500, 200))
            screen.blit(apic2, (500, 50))

            pic = pygame.image.load('mypicitt.png')
            #apic2 = pygame.transform.scale(apic, (500, 200))
            screen.blit(pic, (150, 300))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win14_ch1()
                        elif action == 'Quit':
                            g_win12_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 500, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 400, 550, 100, 50, Red, bright_red, 'Quit')
            
            pygame.display.update()

            clock.tick(60)

    def g_win14_ch1():
    #Run this block later   
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)
            
            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('INVOLUNTARY MIGRATION', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'Sometimes people may migrate without their free will, or are forced out of that country.'
            blit_text(screen, txt, (20, 50), font, color=pygame.Color('black'))

            img = pygame.image.load('isis.jpg')
            img2 = pygame.transform.scale(img, (1000, 300))
            screen.blit(img2, (0, 40))

            img = pygame.image.load('mypicit3.png')
            screen.blit(img, (150, 290))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win15_ch1()
                        elif action == 'Quit':
                            g_win13_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')        

            pygame.display.update()

            clock.tick(60)

    def g_win15_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)
            
            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('VOLUNTARY MIGRATION', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            img = pygame.image.load('money.jpg')
            img2 = pygame.transform.scale(img, (1000, 300))
            screen.blit(img2, (0, 40))

            img = pygame.image.load('vmigr.png')
            screen.blit(img, (150, 300))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win16_ch1()
                        elif action == 'Quit':
                            g_win14_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 0, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 0, 100, 50, Red, bright_red, 'Quit')              

            pygame.display.update()

            clock.tick(60)

    def g_win16_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('EFFECTS OF MIGRATION', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)


            img = pygame.image.load('landg.png')
            screen.blit(img, (150, 50))

            img = pygame.image.load('migrantreason.png')
            screen.blit(img, (150, 400))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win17_ch1()
                        elif action == 'Quit':
                            g_win15_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')   

            pygame.display.update()

            clock.tick(60)

    def g_win17_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Population Structures', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            img = pygame.image.load('dtm.jpg')
            screen.blit(img, (0, 0))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win18_ch1()
                        elif action == 'Quit':
                            g_win16_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 0, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 0, 100, 50, Red, bright_red, 'Quit')   

            pygame.display.update()

            clock.tick(60)


    def g_win18_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Population Structures', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'As you saw in the previous diagram, the growth and development of countries can be shown in the demographic transition model. It has a number of stages, that various countries (MEDC or LEDC) fit into.'
            blit_text(screen, txt, (20, 50), font, color=pygame.Color('black'))

            img = pygame.image.load('dtm2.png')
            screen.blit(img, (200, 100))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_win19_ch1()
                        elif action == 'Quit':
                            g_win17_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 550, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 550, 100, 50, Red, bright_red, 'Quit')   
            
            pygame.display.update()

            clock.tick(60)

    def g_win19_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('Population density and distribution', largeText)
            TextRect.center = ((display_width/2),(20))
            screen.blit(TextSurf, TextRect)

            txt = 'Some areas around the world are extremely sparse. While some are very congested and overpopulated. The table below gives reasons why the population density and ditribution varies between areas.' 
            blit_text(screen, txt, (20, 50), font, color=pygame.Color('black'))

            img = pygame.image.load('why.png')
            screen.blit(img, (200, 100))

            img = pygame.image.load('pdense.png')
            img2 = pygame.transform.scale(img, (1000, 320))
            screen.blit(img2, (0, 290))

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            #g_win20_ch1()
                            pygame.draw.rect(screen, White, (0, 0, 1000, 600))
                            mouse = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()
                            if 500+50 > mouse[0] > 500 and 350+50 > mouse[1] > 350:
                                if click[0] == 1:
                                    HomeWindow()
                                else:
                                    print('')

                            img = pygame.image.load('gohome.jpg')
                            img2 = pygame.transform.scale(img, (50, 50))
                            screen.blit(img2, (500, 350))
                            message_display_ir_edit_edit_edit('Feature Unavailable. Update Available On the 9th May 2018')
                            
                        elif action == 'Quit':
                            g_win18_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('NEXT', 900, 0, 100, 50, Green, bright_green, 'Play')
            button('BACK', 0, 0, 100, 50, Red, bright_red, 'Quit')



            pygame.display.update()

            clock.tick(60)

    def g_quiz_ch1():
       
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(White)

            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Play':
                            g_game_ch1()
                        elif action == 'Quit':
                            g_intro_ch1()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('YES', 650, 450, 100, 50, Green, bright_green, 'Play')
            button('NO', 250, 450, 100, 50, Red, bright_red, 'Quit')

            timg = pygame.image.load('brain-exercise.png')
            timgt = pygame.transform.scale(timg, (1000, 400))
            screen.blit(timgt, (0,0))

            largeText = pygame.font.Font('freesansbold.ttf',100)
            TextSurf, TextRect = text_objects('TAKE A TEST?', largeText)
            TextRect.center = ((display_width/2),(380))
            screen.blit(TextSurf, TextRect)

            pygame.display.update()

            clock.tick(60)

    #The game_loop position

    #Pause Feature
    pause = True
    def paused():

        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        

        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            #gameDisplay.fill(white)
            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'unpause':
                            g_game_ch1()
                        elif action == 'quitgame':
                            quit()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button("Continue",650,450,100,50,Green,bright_green,'unpause')
            button("Quit",259,450,100,50,Red,bright_red,'quitgame')

            pygame.display.update()
            clock.tick(15) 
    #Endpoint

    #Question Windows

    #Make function: help_win1()

    def help_win1():

        start = True

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(Black)

            largeText = pygame.font.Font('freesansbold.ttf',40)
            TextSurf, TextRect = text_objects_white('Instructions', largeText)
            TextRect.center = ((display_width/2),(30))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects_white('In this activity, you would simply fill in the gaps. If you\'re looking for word options', largeText)
            TextRect.center = ((display_width/2),(100))
            screen.blit(TextSurf, TextRect)

             
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects_white('check the Word Bank below', largeText)
            TextRect.center = ((display_width/2),(130))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects_white('WORD BANK', largeText)
            TextRect.center = ((display_width/2),(200))
            screen.blit(TextSurf, TextRect)

            pygame.draw.rect(screen, White, (100, 250, 800, 200))

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('refugee, high, low, food', largeText)
            TextRect.center = ((display_width/2),(270))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('ageing, migration, underpopulated', largeText)
            TextRect.center = ((display_width/2),(320))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',30)
            TextSurf, TextRect = text_objects('dependency ratio, voluntary migration', largeText)
            TextRect.center = ((display_width/2),(370))
            screen.blit(TextSurf, TextRect)

            back = pygame.image.load('gobutt2.png')
            back2 = pygame.transform.scale(back, (50, 50))
            screen.blit(back2, (0, 550))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 0+50 > mouse[0] > 0 and 550+50 > mouse[1] > 550:
                if click[0] == 1:
                    question1()
            else:
                back = pygame.image.load('gobutt2.png')
                back2 = pygame.transform.scale(back, (50, 50))
                screen.blit(back2, (0, 550))

            pygame.display.update()

            clock.tick(30)

            

    def question1():

        #Cover box blemishes
        #pygame.draw.line(screen, white, (x, y), ((x+200), y), width = 5)
        #pygame.draw.line(screen, white, (x, y), (x,(y+h)) , width = 5)
        #pygame.draw.line(screen, white, ((x+200), y), ((x+200),(y+200)) , width = 5)

        qmark = pygame.image.load('qmark.jpg')
        qmark_trans = pygame.transform.scale(qmark, (50, 50))
        input_box = pg.Rect(100, 90, 70, 32)
        input_box2 = pg.Rect(610, 115, 70, 32)
        input_box3 = pg.Rect(610, 170, 70, 32)
        input_box4 = pg.Rect(50, 215, 70, 32)
        input_box5 = pg.Rect(520, 265, 70, 32)
        input_box6 = pg.Rect(550, 320, 70, 32)
        input_box7 = pg.Rect(700, 373, 70, 32)
        input_box8 = pg.Rect(525, 415, 70, 32)
        input_box9 = pg.Rect(425, 475, 70, 32)
        color_inactive = pg.Color('lightskyblue3')
        color_inactive2 = pg.Color('lightskyblue3')
        color_inactive3 = pg.Color('lightskyblue3')
        color_inactive4 = pg.Color('lightskyblue3')
        color_inactive5 = pg.Color('lightskyblue3')
        color_inactive6 = pg.Color('lightskyblue3')
        color_inactive7 = pg.Color('lightskyblue3')
        color_inactive8 = pg.Color('lightskyblue3')
        color_inactive9 = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color_active2 = pg.Color('dodgerblue2')
        color_active3 = pg.Color('dodgerblue2')
        color_active4 = pg.Color('dodgerblue2')
        color_active5 = pg.Color('dodgerblue2')
        color_active6 = pg.Color('dodgerblue2')
        color_active7 = pg.Color('dodgerblue2')
        color_active8 = pg.Color('dodgerblue2')
        color_active9 = pg.Color('dodgerblue2')
        color = color_inactive
        color2 = color_inactive
        color3 = color_inactive
        color4 = color_inactive
        color5 = color_inactive
        color6 = color_inactive
        color7 = color_inactive
        color8 = color_inactive
        color9 = color_inactive
        active = False
        active2 = False
        active3 = False
        active4 = False
        active5 = False
        active6 = False
        active7 = False
        active8 = False
        active9 = False
        text = ''
        text2 = ''
        text3 = ''
        text4 = ''
        text5 = ''
        text6 = ''
        text7 = ''
        text8 = ''
        text9 = ''
        check = pygame.draw.rect(screen, Green,(950, 550, 50, 50))

        mouse = pygame.mouse.get_pos()
        
        start = True

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
    ###     
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active                
                    elif input_box2.collidepoint(event.pos):
                        # Toggle the active variable.
                        active2 = not active2
                    elif input_box3.collidepoint(event.pos):
                        # Toggle the active variable.
                        active3 = not active3
                    elif input_box4.collidepoint(event.pos):
                        # Toggle the active variable.
                        active4 = not active4
                    elif input_box5.collidepoint(event.pos):
                        # Toggle the active variable.
                        active5 = not active5
                    elif input_box6.collidepoint(event.pos):
                        # Toggle the active variable.
                        active6 = not active6
                    elif input_box7.collidepoint(event.pos):
                        # Toggle the active variable.
                        active7 = not active7
                    elif input_box8.collidepoint(event.pos):
                        # Toggle the active variable.
                        active8 = not active8
                    elif input_box9.collidepoint(event.pos):
                        # Toggle the active variable.
                        active9 = not active9
    ###
    ###
                    elif input_box.collidepoint(event.pos) != True:
                        active = False
                    # Change the current color of the input box.
                    elif input_box2.collidepoint(event.pos) != True:
                        active2 = False
                    # Change the current color of the input box.
                    elif input_box3.collidepoint(event.pos) != True:
                        active3 = False
                    # Change the current color of the input box.
                    elif input_box4.collidepoint(event.pos) != True:
                        active4 = False
                    # Change the current color of the input box.
                    elif input_box5.collidepoint(event.pos) != True:
                        active5 = False
                    # Change the current color of the input box.
                    elif input_box6.collidepoint(event.pos) != True:
                        active6 = False
                    # Change the current color of the input box.
                    elif input_box7.collidepoint(event.pos) != True:
                        active7 = False
                    # Change the current color of the input box.
                    elif input_box8.collidepoint(event.pos) != True:
                        active8 = False
                    # Change the current color of the input box.
                    elif input_box9.collidepoint(event.pos) != True:
                        active9 = False
                    # Change the current color of the input box.
    ###
                    else:
                        print('Daniel is a boss!!!')

                    color9 = color_active9 if active9 else color_inactive9
                    color8 = color_active8 if active8 else color_inactive8
                    color7 = color_active7 if active7 else color_inactive7
                    color6 = color_active6 if active6 else color_inactive6
                    color5 = color_active5 if active5 else color_inactive5
                    color4 = color_active4 if active4 else color_inactive4
                    color3 = color_active3 if active3 else color_inactive3
                    color2 = color_active2 if active2 else color_inactive2
                    color = color_active if active else color_inactive
                                      
                elif event.type == pygame.KEYDOWN:
                    if active2:
                        if event.key == pygame.K_RETURN:
                            print(text2)
                        elif event.key == pygame.K_BACKSPACE:
                            text2 = text2[:-1]
                        else:
                            text2 += event.unicode###
                    elif active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode###
                    elif active3:
                        if event.key == pygame.K_RETURN:
                            print(text3)
                        elif event.key == pygame.K_BACKSPACE:
                            text3 = text3[:-1]
                        else:
                            text3 += event.unicode###
                    elif active4:
                        if event.key == pygame.K_RETURN:
                            print(text4)
                        elif event.key == pygame.K_BACKSPACE:
                            text4 = text4[:-1]
                        else:
                            text4 += event.unicode###
                    elif active5:
                        if event.key == pygame.K_RETURN:
                            print(text5)
                        elif event.key == pygame.K_BACKSPACE:
                            text5 = text5[:-1]
                        else:
                            text5 += event.unicode###
                    elif active6:
                        if event.key == pygame.K_RETURN:
                            print(text6)
                        elif event.key == pygame.K_BACKSPACE:
                            text6 = text6[:-1]
                        else:
                            text6 += event.unicode###
                    elif active7:
                        if event.key == pygame.K_RETURN:
                            print(text7)
                        elif event.key == pygame.K_BACKSPACE:
                            text7 = text7[:-1]
                        else:
                            text7 += event.unicode###
                    elif active8:
                        if event.key == pygame.K_RETURN:
                            print(text8)
                        elif event.key == pygame.K_BACKSPACE:
                            text8 = text8[:-1]
                        else:
                            text8 += event.unicode###
                    elif active9:
                        if event.key == pygame.K_RETURN:
                            print(text9)
                        elif event.key == pygame.K_BACKSPACE:
                            text9 = text9[:-1]
                        else:
                            text9 += event.unicode###

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check.collidepoint(event.pos):
                        
                        texta = text.upper()
                        textb = text2.upper()
                        textc = text3.upper()
                        textd = text4.upper()
                        texte = text5.upper()
                        textf = text6.upper()
                        textg = text7.upper()
                        texth = text8.upper()
                        texti = text9.upper()

                        pointa = 0
                        pointb = 0
                        pointc = 0
                        pointd = 0
                        pointe = 0
                        pointf = 0
                        pointg = 0
                        pointh = 0
                        pointi = 0
                        
                        answer = [texta, textb, textc, textd, texte, textf, textg, texth, texti]
                        if texta == 'REFUGEE':
                            pointa += 1
                        if textb == 'MIGRATION':
                            pointb += 1
                        if textc == 'UNDERPOPULATED':
                            pointc += 1
                        if textd == 'DEPENDENCY RATIO':
                            pointd += 1
                        if texte == 'VOLUNTARY MIGRATION':
                            pointe += 1
                        if textf == 'AGEING':
                            pointf += 1
                        if textg == 'LOW':
                            pointg += 1
                        if texth == 'HIGH':
                            pointh += 1
                        if texti == 'FOOD':
                            pointi += 1

                        total = pointa + pointb + pointc + pointd + pointe + pointf + pointg + pointh + pointi
                        results = 'You got', str(total), 'out of 9'
                        modresult = " ".join(results)
                        if total > 4:    
                            message_display_cr(modresult)
                        else:
                            message_display_ir(modresult)

                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if 925+50 > mouse[0] > 925 and 0+50 > mouse[1] > 0:
                        if click[0] == 1:
                            help_win1()
                            pygame.display.update()
                    else:
                        qmark = pygame.image.load('qmark.jpg')
                        qmark_trans = pygame.transform.scale(qmark, (50, 50))
                        screen.blit(qmark_trans, (925, 0))
                            
                    
                         
            screen.fill(White)

            font = pygame.font.SysFont('comicsansms', 15)

            pygame.draw.rect(screen, Green,(950, 550, 50, 50))

            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = text_objects('GO!', smallText)
            textRect.center = ( (950+(50/2)), (550+(50/2)) )
            screen.blit(textSurf, textRect)

            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects('Identify these key terms', largeText)
            TextRect.center = ((display_width/2),((30)))
            screen.blit(TextSurf, TextRect)

            texti = 'A person who has been forced to leave their home and their country, may be due to a natural disaster, war, religious or political persecution is called a'
            textii = 'The movement of people (or animals) from one country or region to another is called '
            textiii = 'When country has declined too much that it can’t support its economic system it is '
            textiv = 'The                                          would increase if there are many Young Dependents'
            textv = 'When people chose to move, usually for economic benefit it is known as'
            textvi = 'When proportion of old dependents is increasing the population is said to be'
            textvii = 'When an area is mountainous with a very harsh climate, the population density there is likely to be'
            textviii = 'However, an area with good resources and a favorable climate will have a                                          population density. '
            textix = 'When migrating, the migrants may have better access to                                              and health care.'
            
            blit_text(screen, texti, ((20),(70)), font, color=pygame.Color('black'))
            blit_text(screen, textii, ((20),(120)), font, color=pygame.Color('black'))
            blit_text(screen, textiii, ((20),(170)), font, color=pygame.Color('black'))
            blit_text(screen, textiv, ((20),(220)), font, color=pygame.Color('black'))
            blit_text(screen, textv, ((20),(270)), font, color=pygame.Color('black'))
            blit_text(screen, textvi, ((20),(320)), font, color=pygame.Color('black'))
            blit_text(screen, textvii, ((20),(360)), font, color=pygame.Color('black'))
            blit_text(screen, textviii, ((20),(420)), font, color=pygame.Color('black'))
            blit_text(screen, textix, ((20),(480)), font, color=pygame.Color('black'))

            

    #Box1
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)
    #Box1<END>
    #Box2
            # Render the current text.
            txt_surface2 = font.render(text2, True, color2)
            # Resize the box if the text is too long.
            width2 = max(200, txt_surface2.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box2.w = width2
            # Blit the text.
            screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color2, input_box2, 2)
    #Box2<END>
    #Box3
            # Render the current text.
            txt_surface3 = font.render(text3, True, color3)
            # Resize the box if the text is too long.
            width3 = max(200, txt_surface3.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box3.w = width3
            # Blit the text.
            screen.blit(txt_surface3, (input_box3.x+5, input_box3.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color3, input_box3, 2)
    #Box3<END>
    #Box4
            # Render the current text.
            txt_surface4 = font.render(text4, True, color4)
            # Resize the box if the text is too long.
            width4 = max(200, txt_surface4.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box4.w = width4
            # Blit the text.
            screen.blit(txt_surface4, (input_box4.x+5, input_box4.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color4, input_box4, 2)
    #Box4<END>
    #Box5
            # Render the current text.
            txt_surface5 = font.render(text5, True, color5)
            # Resize the box if the text is too long.
            width5 = max(200, txt_surface5.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box5.w = width5
            # Blit the text.
            screen.blit(txt_surface5, (input_box5.x+5, input_box5.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color5, input_box5, 2)
    #Box5<END>
    #Box6
            # Render the current text.
            txt_surface6 = font.render(text6, True, color6)
            # Resize the box if the text is too long.
            width6 = max(200, txt_surface6.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box6.w = width6
            # Blit the text.
            screen.blit(txt_surface6, (input_box6.x+5, input_box6.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color6, input_box6, 2)
    #Box6<END>
    #Box7
            # Render the current text.
            txt_surface7 = font.render(text7, True, color7)
            # Resize the box if the text is too long.
            width7 = max(200, txt_surface7.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box7.w = width7
            # Blit the text.
            screen.blit(txt_surface7, (input_box7.x+5, input_box7.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color7, input_box7, 2)
    #Box7<END>
    #Box8
            # Render the current text.
            txt_surface8 = font.render(text8, True, color8)
            # Resize the box if the text is too long.
            width8 = max(200, txt_surface8.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box8.w = width8
            # Blit the text.
            screen.blit(txt_surface8, (input_box8.x+5, input_box8.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color8, input_box8, 2)
    #Box8<END>
    #Box9
            # Render the current text.
            txt_surface9 = font.render(text9, True, color9)
            # Resize the box if the text is too long.
            width9 = max(200, txt_surface9.get_width()+10)
            #I need a function to help go to a new line if the box is too high.
            input_box9.w = width9
            # Blit the text.
            screen.blit(txt_surface9, (input_box9.x+5, input_box9.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color9, input_box9, 2)
    #Box9<END>

            qmark = pygame.image.load('qmark.jpg')
            qmark_trans = pygame.transform.scale(qmark, (50, 50))
            screen.blit(qmark_trans, (925, 0))

            pygame.draw.line(screen, White, (100, 90), ((100+200), 90),5)
            pygame.draw.line(screen, White, (100, 90), (100,(90+32)) , 5)
            pygame.draw.line(screen, White, ((100+200), 90), ((100+200),(90+32)) , 5)

            pygame.draw.line(screen, White, (610, 115), ((610+200), 115),5)
            pygame.draw.line(screen, White, (610, 115), (610,(115+32)) ,5)
            pygame.draw.line(screen, White, ((610+200), 115), ((610+200),(115+32)) ,5)

            pygame.draw.line(screen, White, (610, 170), ((610+200), 170), 5)
            pygame.draw.line(screen, White, (610, 170), (610,(170+32)) ,  5)
            pygame.draw.line(screen, White, ((610+200), 170), ((610+200),(170+200)) , 5)

            pygame.draw.line(screen, White, (50, 215), ((50+200), 215),5)
            pygame.draw.line(screen, White, (50, 215), (50,(215+32)) ,5)
            pygame.draw.line(screen, White, ((50+200), 215), ((50+200),(215+200)) ,5)

            pygame.draw.line(screen, White, (520, 265), ((520+200), 265),5)
            pygame.draw.line(screen, White, (520, 265), (520,(265+32)) ,5)
            pygame.draw.line(screen, White, ((520+200), 265), ((520+200),(265+200)) ,5)

            pygame.draw.line(screen, White, (550, 320), ((550+200), 320),5)
            pygame.draw.line(screen, White, (550, 320), (550,(320+32)) ,5)
            pygame.draw.line(screen, White, ((550+200), 320), ((550+200),(320+200)) ,5)

            pygame.draw.line(screen, White, (700, 373), ((700+200), 373),5)
            pygame.draw.line(screen, White, (700, 373), (700,(373+32)) ,5)
            pygame.draw.line(screen, White, ((700+200), 373), ((700+200),(373+200)) ,5)

            pygame.draw.line(screen, White, (525, 415), ((525+200), 415),5)
            pygame.draw.line(screen, White, (525, 415), (525,(415+32)) ,5)
            pygame.draw.line(screen, White, ((525+200), 415), ((525+200),(415+200)) ,5)

            pygame.draw.line(screen, White, (425, 475), ((425+200), 475),5)
            pygame.draw.line(screen, White, (425, 475), (425,(475+32)) ,5)
            pygame.draw.line(screen, White, ((425+200), 475), ((425+200),(475+200)) ,5)

            blit_text(screen, texti, ((20),(70)), font, color=pygame.Color('black'))
            blit_text(screen, textii, ((20),(120)), font, color=pygame.Color('black'))
            blit_text(screen, textiii, ((20),(170)), font, color=pygame.Color('black'))
            blit_text(screen, textiv, ((20),(220)), font, color=pygame.Color('black'))
            blit_text(screen, textv, ((20),(270)), font, color=pygame.Color('black'))
            blit_text(screen, textvi, ((20),(320)), font, color=pygame.Color('black'))
            blit_text(screen, textvii, ((20),(360)), font, color=pygame.Color('black'))
            blit_text(screen, textviii, ((20),(420)), font, color=pygame.Color('black'))
            blit_text(screen, textix, ((20),(480)), font, color=pygame.Color('black'))
        
            pygame.display.update()
            clock.tick(30)

    #End Point
    def g_game_ch1():
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 7
        thing_width = 40
        thing_height = 30

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change
            screen.fill(White)

            # things(thingx, thingy, thingw, thingh, color)
            bulbdsp(thing_startx, thing_starty, thing_width, thing_height)
            thing_starty += thing_speed
            car(x,y)

            if x > display_width - car_width or x < 0:
                crash()

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,display_width)
            ####
            if y < thing_starty+thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                    option = ['q1', 'q2', 'q3', 'q4', 'q5']
                    def ques():                                 
                        if len(option) > 0:
                            opt = random.choice(option)
                        else:
                            boss = 1
                        x = 0
                        x2 = 0
                        x3 = 0
                        x4 = 0
                        x5 = 0
                        x6 = 0
                        x7 = 0
                        x8 = 0
                        x9 = 0
                        x10 = 0
                        while len(option) > 0:
                            if opt == 'q1':
                                x+=1
                                if x > 1:
                                    ques()
                                else:
                                    message_display_cr_edit('Answer The Following Question(s): ')
                                    option.remove('q1')
                                    question1()
                            if opt == 'q2':
                                x2 += 1
                                if x2 > 1:
                                    ques()
                                else:
                                    #message_display2('Answer The Following Question(s): ')
                                    option.remove('q2')
                                    #question2()
                                    message_display_ir_edit('Question Unavailable. Update available on 9th May 2018')
                                    message_display_ir_edit_edit('You will be taken to the options menu for further revision')
                            if opt == 'q3':
                                x3 +=1
                                if x3 > 1:
                                    ques()
                                else:
                                    #message_display2('Answer The Following Question(s): ')
                                    option.remove('q3')
                                    #question3()
                                    message_display_ir_edit('Question Unavailable. Update available on 9th May 2018')
                                    message_display_ir_edit_edit('You will be taken to the options menu for further revision')
                            if opt == 'q4':
                                x4+=1
                                if x4 > 1:
                                    ques()
                                else:
                                    #message_display2('Answer The Following Question(s): ')
                                    option.remove('q4')
                                    #question4()
                                    message_display_ir_edit('Question Unavailable. Update available on 9th May 2018')
                                    message_display_ir_edit_edit('You will be taken to the options menu for further revision')
                            if opt == 'q5':
                                x5 += 1
                                if x5 > 1:
                                    ques()
                                else:
                                    #message_display2('Answer The Following Question(s): ')
                                    option.remove('q5')
                                    #question5()
                                    message_display_ir_edit('Question Unavailable. Update available on 9th May 2018')
                                    message_display_ir_edit_edit('You will be taken to the options menu for further revision')
                            if opt == 'q6':
                                x6 += 1
                                if x6 > 1:
                                    ques()
                                else:
                                    #message_display2('Answer The Following Question(s): ')
                                    option.remove('q6')
                                    #question6()
                                    message_display_ir_edit('Question Unavailable. Update available on 9th May 2018')
                                    message_display_ir_edit_edit('You will be taken to the options menu for further revision')
                    ques()
                    
            def button(msg,x,y,w,h,ic,ac, action = None):
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if x+w > mouse[0] > x and y+h > mouse[1] > y:
                    pygame.draw.rect(screen, ac,(x,y,w,h))
                    if click[0] == 1 and action != None:
                        if action == 'Pause':
                            pause = True
                            paused()
                        elif action == 'Quit':
                            quit()
                else:
                    pygame.draw.rect(screen, ic,(x,y,w,h))
                
                    
                smallText = pygame.font.Font("freesansbold.ttf",20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                screen.blit(textSurf, textRect)

            button('PAUSE',900,0,100,50,Blue,Aqua, 'Pause')
            #Apply Home and Alt-View 

            ####
            pygame.display.update()
            clock.tick(60)

    #My code endpoint
    g_intro_ch1()
    pygame.quit()
    quit()

starter()
pygame.quit()
quit()
