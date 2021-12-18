import pygame  # 1.Pygame 선언
import random

pygame.init()  # 2 Pygame 초기화
# 3. Pygame 에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
size = (400, 400)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()


# 4. Pygame 무한루프
def runGame():
    global done
    draw_circle = False
    x = 200
    y = 200
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 10

        pygame.draw.circle(screen, (0, 0, 255), (x, y), 5)
        pygame.display.update()


runGame()
pygame.quit()
