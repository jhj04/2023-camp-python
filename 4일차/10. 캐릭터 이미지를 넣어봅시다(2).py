import random

# 장애물 불러오기

enemy = pygame.image.load("[파일 위치]")
enemy_size = enemy.get_rect().size       #이미지 크기 구하기
enemy_width = enemy_size[0]               #가로 크기
enemy_height = enemy_size[1]              # 세로 크기
enemy_x_pos = random.randint(0,screen_width - enemy_width)     
# 화면 가로의 절반에 위치
enemy_y_pos = 0
enemy_speed = [직접 지정하기]               # 이동 속도
...
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos ))  
