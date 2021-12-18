import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
size = [600, 600]
screen = pygame.display.set_mode(size)


def is_valid_position(grid, position):
    if grid[position] == ' ':
        return True
    else:
        return False


def is_winner(grid, mark):
    if (grid[0] == mark and grid[1] == mark and grid[2] == mark) or \
            (grid[3] == mark and grid[4] == mark and grid[5] == mark) or \
            (grid[6] == mark and grid[7] == mark and grid[8] == mark) or \
            (grid[0] == mark and grid[3] == mark and grid[6] == mark) or \
            (grid[1] == mark and grid[4] == mark and grid[7] == mark) or \
            (grid[2] == mark and grid[5] == mark and grid[8] == mark) or \
            (grid[0] == mark and grid[4] == mark and grid[8] == mark) or \
            (grid[2] == mark and grid[4] == mark and grid[6] == mark):
        return True
    else:
        return False

def is_grid_full(grid):
    full = True
    for mark in grid:
        if mark == ' ':
            full = False
            break
    return full


turn = 0
grid = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ']

done = False
clock = pygame.time.Clock()


def runGame():
    CELL_SIZE = 60
    COLUMN_COUNT = 3
    ROW_COUNT = 3
    X_WIN = 1
    Y_WIN = 2
    DRAW = 3
    game_over = 0

    global done, turn, grid
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    column_index = event.pos[0] // CELL_SIZE
                    row_index = event.pos[1] // CELL_SIZE
                    position = column_index + 3 * row_index
                    
                    if is_valid_position(grid, position):
                        grid[position] = 'X'
                        
                        if is_winner(grid, position):
                            print('X가 이겼습니다')
                            game_over = X_WIN
                        
                        elif is_grid_full(grid):
                            print('무승부입니다')
                            game_over = DRAW
                        
                        turn += 1
                        turn = turn % 2

        pygame.display.update()


runGame()
pygame.quit()
