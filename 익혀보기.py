import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Input Example")

# 색상 정의
WHITE = (255, 255, 225)
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)

# 객체 초기 위치 (시작 좌표)
x_coordinate = WIDTH // 2
y_coordinate = HEIGHT // 2
object_width = 20
object_height = 20

# 게임 루프 (이벤트 처리)
running = True
while running:
    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 키보드 누름 이벤트 감지
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # 왼쪽 화살표 키: x 좌표를 -1 만큼 이동
                x_coordinate -= 10
                print(f"왼쪽 키 감지: 현재 x 좌표 = {x_coordinate}")
            elif event.key == pygame.K_RIGHT:
                # 오른쪽 화살표 키: x 좌표를 +1 만큼 이동
                x_coordinate += 10
                print(f"오른쪽 키 감지: 현재 x 좌표 = {x_coordinate}")
            elif event.key == pygame.K_UP:
                # 오른쪽 화살표 키: x 좌표를 +1 만큼 이동
                y_coordinate -= 10
                print(f"위 키 감지: 현재 y 좌표 = {y_coordinate}")
            elif event.key == pygame.K_DOWN:
                # 오른쪽 화살표 키: x 좌표를 +1 만큼 이동
                y_coordinate += 10
                print(f"아래 키 감지: 현재 y 좌표 = {y_coordinate}")

    # 2. 화면 그리기
    screen.fill(WHITE)  # 배경을 흰색으로 채우기
    
    # 현재 x, y 좌표에 사각형 그리기
    pygame.draw.rect(screen, GREEN, (x_coordinate, y_coordinate, object_width, object_height))
    
    # 3. 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
