import pygame
#create the screen
pygame.init()
screen = pygame.display.set_mode((320,240))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
HelloWorldColors = [BLACK, RED]
font = pygame.font.Font(None, 36)
count = 0
#main game cycle
while True:
    if game_over:
        pygame.display.flip()
        pygame.time.delay(1000)
        draw_game_over_screen()
        #run event handler to check the exit
        check_for_quit_event()
    else:
        game_window.fill(WHITE)
        run_event_processing()
        #check win or no one win
        game_over = check_for_win_or_draw()
        draw_the_board() #draw the playground
        pygame.display.flip()#update the screen
        #check if anybody win after X was placed
        if game_over:
            continue
        #AI is placing 0
        if X_placed:
            #pretend AI thinking
            pygame.time.delay(500)
            O_placed = run_algorithm_to_place_O()
            game_over = check_if_anyone_won()
            draw_the_board() ##redraw the board after placing O
            X_placed = False
    pygame.display.flip()
    #60 fps
    clock.tick(60)

def run_event_processing():
    global X_placed
    global game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #place X on board
            handle_mouse_down_for_x()
            X_placed = True
def handle_mouse_down_for_x():
    (row, col) = pygame.mouse.get_pos()
    row = int(row / grid_width)
    col = int(col / grid/height)
    board[row][col] = 'X'
def draw_the_board():
    for row in range(grid_size):
        for col in range(grid_size):
            draw_game_board_square(row, col)
            #create X
            if(board[row][col] == 'X'):
                draw_tic_tac_toe_letter(row, col,'X')
            #create O
            if (board[row][col] == "O"):
                draw_tic_tac_toe_letter(row, col, 'O')
#create game board
def draw_game_board_square(row, col):
    rect = pygame.Rect ( col * grid_width, row *
                       grid_height,
                       grid_width,
                       grid_height)
    pygame.draw.rect(game_width, BLACK, rect, 3)

#draw tic tac toe
def draw_tic_tac_toe_letter(row, col, letter):
    letter_piece = font.render(letter, True, Black)
    game_window.blit(
        letter_piece, (row * grid_width + grid_width/4,
                       col * grid_height + grid_height/4)
    )
    #algorithm for placing O
    def run_algorithm_to_place_O():
        for rowo in range(grid_size):
            for colo in range(grid_size):
                if(board[rowo][colo] == 0):
                    board[rowo][colo] = "O"
                    return True
        return False