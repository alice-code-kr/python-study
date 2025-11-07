
import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("떨어지는 블록 피하기 ")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 70, 70)
BLUE = (70, 130, 255)

# 플레이어 설정
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size * 2
player_speed = 8

# 블록 설정
block_size = 50
block_speed = 4
blocks = []
spawn_rate = 30  # 블록 생성 확률 (낮을수록 자주 생성됨)

# 점수 & 난이도
score = 0
font = pygame.font.SysFont(None, 40)
difficulty_timer = 0

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

def draw_block(block):
    pygame.draw.rect(screen, RED, (block[0], block[1], block_size, block_size))

def show_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # 블록 생성 (확률적으로)
    if random.randint(1, spawn_rate) == 1:
        blocks.append([random.randint(0, WIDTH - block_size), 0])

    # 블록 이동
    for block in blocks[:]:
        block[1] += block_speed
        if block[1] > HEIGHT:
            blocks.remove(block)
            score += 1

    # 충돌 감지
    for block in blocks:
        if (
            player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]
        ):
            show_text("GAME OVER!", 110, HEIGHT // 2 - 20, RED)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # 난이도 조절 (시간이 지날수록 점점 어려워짐)
    difficulty_timer += 1
    if difficulty_timer % 300 == 0:  # 약 5초마다
        if block_speed < 15:
            block_speed += 0.5  # 블록 속도 증가
        if spawn_rate > 10:
            spawn_rate -= 1  # 블록 생성 확률 증가 (더 자주 떨어짐) Test

    # 그리기
    draw_player(player_x, player_y)
    for block in blocks:
        draw_block(block)
    show_text(f"Score: {score}", 10, 10)
    show_text(f"Speed: {block_speed:.1f}", 280, 10)

    pygame.display.flip()
