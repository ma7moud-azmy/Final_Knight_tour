import pygame
from no_ai import no_ai
from backtracking import backtracking
from genetic import genetic
from simulated_annealing import simulated_annealing
import os

def __main__():
    x = 450
    y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    #game initiolization and window formatting
    pygame.init()
    WIDTH = 820
    HEIGHT = 400
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Knight Tour")
    icon = pygame.image.load('assets/images/black knight.png')
    bg = pygame.image.load('assets/images/bg.jpg')
    bg = pygame.transform.scale(bg, (820, 400))
    pygame.display.set_icon(icon)
    font = pygame.font.Font('freesansbold.ttf', 25)
    med_font = pygame.font.Font('freesansbold.ttf', 30)
    large_font = pygame.font.Font('freesansbold.ttf', 40)
    color = (255,255,255) 
    color_light = (170,170,170) 
    color_dark = (100,100,100) 
    timer = pygame.time.Clock()
    fps = 60

    #global variables
    game_mode = 0



    #drawing buttons in the window
    def draw_buttons(mouse):
        text1 = font.render('No AI' , True , color)
        text2 = font.render('Backtracking' , True , color)
        text3 = font.render('Genetic' , True , color)
        text4 = font.render('Simulated Annealing' , True , color)
        if 500 <= mouse[0] <= 780 and 60 <= mouse[1] <= 100:
            pygame.draw.rect(screen,color_light,[500,60,280,40]) 
        else:
            pygame.draw.rect(screen,color_dark,[500,60,280,40])
        
        if 500 <= mouse[0] <= 780 and 140 <= mouse[1] <= 180:
            pygame.draw.rect(screen,color_light,[500,140,280,40]) 
        else:
            pygame.draw.rect(screen,color_dark,[500,140,280,40])
        
        if 500 <= mouse[0] <= 780 and 220 <= mouse[1] <= 260:
            pygame.draw.rect(screen,color_light,[500,220,280,40]) 
        else:
            pygame.draw.rect(screen,color_dark,[500,220,280,40])
        
        if 500 <= mouse[0] <= 780 and 300 <= mouse[1] <= 340:
            pygame.draw.rect(screen,color_light,[500,300,280,40]) 
        else:
            pygame.draw.rect(screen,color_dark,[500,300,280,40])
        screen.blit(text1 , (515,70))
        screen.blit(text2 , (515,150))
        screen.blit(text3 , (515,230))
        screen.blit(text4 , (515,310))


    #choosing the game mode
    def start_game(mouse):
        if 500 <= mouse[0] <= 750 and 60 <= mouse[1] <= 100:
            flag = no_ai()
            if not flag :
                pygame.quit()
            else :
                __main__()
        if 500 <= mouse[0] <= 750 and 140 <= mouse[1] <= 180:
            flag = backtracking()
            if not flag :
                pygame.quit()
            else : 
                __main__()
        if 500 <= mouse[0] <= 750 and 220 <= mouse[1] <= 260:
            flag = genetic()
            if not flag :
                pygame.quit()
            else : 
                __main__()
        if 500 <= mouse[0] <= 750 and 300 <= mouse[1] <= 340:
            flag = simulated_annealing()
            if not flag :
                pygame.quit()
            else : 
                __main__()

    #main loop
    run = True

    while run:
        
        timer.tick(fps)
        screen.fill('dark gray')
        screen.blit(bg, (0, 0))
        mouse = pygame.mouse.get_pos()
        draw_buttons(mouse)
        x_coords = 0
        y_coords = 0
        click_coords = ()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x_coords = event.pos[0]
                    y_coords = event.pos[1]
                    click_coords = (x_coords, y_coords)
                    start_game(click_coords)
        pygame.display.flip()
    pygame.quit()
__main__()