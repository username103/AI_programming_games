import pygame
import sys

# 初始化
pygame.init()

# 设置窗口大小
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# 设置颜色
black = 0, 0, 0
white = 255, 255, 255
background_color = 200, 200, 200

# 初始化棋盘
board = [[0 for _ in range(15)] for _ in range(15)]

# 绘制棋盘
def draw_board():
    pygame.draw.rect(screen, background_color, (20, 20, 560, 560))

    for i in range(15):
        pygame.draw.line(screen, black, (40, 40 + i * 40), (560, 40 + i * 40), 2)
        pygame.draw.line(screen, black, (40 + i * 40, 40), (40 + i * 40, 560), 2)


# 绘制棋子
def draw_piece(x, y, player):
    if player == 1:
        color = black
    else:
        color = white
    pygame.draw.circle(screen, color, (x+20, y+20), 20,0)

# 判断胜负
def check_win(x, y, player):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        # 向一个方向检查
        for i in range(1, 5):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < 15 and 0 <= ny < 15 and board[nx][ny] == player:
                count += 1
            else:
                break
        # 向另一个方向检查
        for i in range(1, 5):
            nx, ny = x - dx * i, y - dy * i
            if 0 <= nx < 15 and 0 <= ny < 15 and board[nx][ny] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# 显示胜利消息
def show_win_message(player):
    try:
        # Try loading the custom font first
        font_path = ".\\simsun.ttc"
        font = pygame.font.Font(font_path, 74)
    except Exception as e:
        print(f"Custom font not found, using system font: {e}")
        # Fallback to a system font that supports Chinese
        font = pygame.font.SysFont("SimSun", 74)

    text = font.render(f"玩家 {player} 获胜！", True, (255, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # 显示消息3秒
    sys.exit()

# 游戏主循环
current_player = 1
draw_board()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x = (x - 20) // 40
            grid_y = (y - 20) // 40
            if 0 <= grid_x < 15 and 0 <= grid_y < 15 and board[grid_x][grid_y] == 0:
                board[grid_x][grid_y] = current_player
                draw_piece(grid_x * 40 + 20, grid_y * 40 + 20, current_player)
                if check_win(grid_x, grid_y, current_player):
                    show_win_message(current_player)
                current_player = 2 if current_player == 1 else 1
    pygame.display.flip()
