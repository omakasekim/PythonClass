import pygame
from datetime import datetime
from datetime import timedelta

pygame.init()  # pygame 초기화

# pygame 에 사용되는 전역 변수 선언
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

block_position = [0, 0]  # (y,x)
last_moved_time = datetime.now()
moving_direction = ''  # North, South, East, West


def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * 20, position[1] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)


def runGame():
    global done, last_moved_time, moving_direction

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block_position[1] -= 1  # 블록의 y 좌표를 1 뺀다
                    moving_direction = 'N'
                    last_moved_time = datetime.now()
                elif event.key == pygame.K_DOWN:
                    block_position[1] += 1  # 블록의 y 좌표를 1 더한다
                    moving_direction = 'S'
                    last_moved_time = datetime.now()
                elif event.key == pygame.K_LEFT:
                    block_position[0] -= 1  # 블록의 x 좌표를 1 뺀다
                    moving_direction = 'W'
                    last_moved_time = datetime.now()
                elif event.key == pygame.K_RIGHT:
                    block_position[0] += 1  # 블록의 x 좌표를 1 더한다
                    moving_direction = 'E'
                    last_moved_time = datetime.now()

    if timedelta(seconds=0.5) <= datetime.now() - last_moved_time:
        if moving_direction == 'N':
            block_position[1] -= 1
        elif moving_direction == 'S':
            block_position[1] == 1
        elif moving_direction == 'W':
            block_position[0] -= 1
        elif moving_direction == 'E':
            block_position[0] += 1

    draw_block(screen, GREEN, block_position)
    pygame.display.update()


runGame()
pygame.quit()
