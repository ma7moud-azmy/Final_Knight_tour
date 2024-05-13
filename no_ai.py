import pygame
import os


def no_ai():
    
    x = 500
    y = 10
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    
    
    pygame.init()
    WIDTH = 640
    HEIGHT = 760
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Knight Tour")
    icon = pygame.image.load('assets/images/black knight.png')
    pygame.display.set_icon(icon)
    font = pygame.font.Font('freesansbold.ttf', 25)
    med_font = pygame.font.Font('freesansbold.ttf', 30)
    large_font = pygame.font.Font('freesansbold.ttf', 40)
    timer = pygame.time.Clock()
    fps = 60

    #colors
    color1 = (49, 46, 43)
    color2 = (115, 149, 82)


    #game variables and images
    valid_moves = []
    board = []
    for i in range(8):
        for j in range(8):
            board.append((i,j))
    game_over = False
    score = 0
    history = []
    location = (1000,1000)

    move = pygame.mixer.Sound('assets/move.mp3')
    #load in game piece image
    black_knight = pygame.image.load('assets/images/icon.png')
    black_knight = pygame.transform.scale(black_knight, (60, 60))


    #draw main game board
    def draw_board():
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, 'white', [480 - (column * 160), row * 80, 80, 80])
                pygame.draw.rect(screen, color2, [560 - (column * 160), row * 80, 80, 80])
            else:
                pygame.draw.rect(screen, 'white', [560 - (column * 160), row * 80, 80, 80])
                pygame.draw.rect(screen, color2, [480 - (column * 160), row * 80, 80, 80])
                
            pygame.draw.rect(screen, color1, [0, 640, WIDTH, 120])



    def draw_knight():
        screen.blit(black_knight, (location[0] * 80 + 15, location[1] * 80 + 15))


    #check valid knight moves
    def check_knight(position):
        move_list = []
        targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                move_list.append(target)
        return move_list


    def check_valid_moves():
        valid_options = []
        for i in options:
            if i not in history:
                valid_options.append(i)
        #valid_options = options
        return valid_options


    #draw valid moves in the screen
    def draw_valid(moves):
        for i in range(len(moves)):
            pygame.draw.circle(screen, 'black', (moves[i][0] * 80 + 40, moves[i][1] * 80 + 40), 6)


    #drawing the visited squares
    def draw_visited():
        visit = 1
        for i in range(len(history)):
            screen.blit(med_font.render(str(visit), True, 'black'), (history[i][0] * 80, history[i][1] * 80))
            visit += 1


    def draw_game_over():
        #pygame.draw.rect(screen, 'black', [130, 655, 380, 70])
        screen.blit(font.render( 'No More Valid Moves!', True, 'white'), (140, 660))
        screen.blit(font.render('Press ENTER To Restart!', True, 'white'), (140, 690))
        screen.blit(font.render('Press SPACE To Go Main Menu!', True, 'white'), (140, 720))


    #main game loop
    run = True

    while run:
        timer.tick(fps)
        screen.fill('dark gray')
        x_coords = 0
        y_coords = 0
        click_coords = ()
        
        draw_board()
        draw_knight()
        options = check_knight(location)
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
        draw_visited()
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coords = event.pos[0] // 80
                y_coords = event.pos[1] // 80
                click_coords = (x_coords, y_coords)
                if click_coords in board:
                    history.append(click_coords)
                    location = click_coords
                    board = []
                    pygame.mixer.Sound.play(move)
                elif click_coords in valid_moves and click_coords not in history:
                    location = click_coords
                    score +=1
                    history.append(click_coords)
                    pygame.mixer.Sound.play(move)
            
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    valid_moves = []
                    for i in range(8):
                        for j in range(8):
                            board.append((i,j))
                    score = 0
                    game_over = False
                    history = []
                    location = (1000,1000)
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    return True
        
        if valid_moves == [] and score > 0:
            game_over = True
            draw_game_over()
        
        pygame.display.flip()
    pygame.quit()
    return False

