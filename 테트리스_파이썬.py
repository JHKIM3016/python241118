import pygame
import random

# 초기화
pygame.init()

# 색상 정의
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'GRAY': (128, 128, 128),
    'BLUE': (0, 0, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0),
    'PURPLE': (255, 0, 255),
    'CYAN': (0, 255, 255),
    'ORANGE': (255, 165, 0)
}

# 게임 설정
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (BOARD_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 테트리미노 모양
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'L': [[1, 0],
          [1, 0],
          [1, 1]],
    'J': [[0, 1],
          [0, 1],
          [1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]]
}

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('테트리스')
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.current_pos = {'x': 0, 'y': 0}
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)

    def new_piece(self):
        # 새로운 테트리미노 생성
        shape = random.choice(list(SHAPES.keys()))
        self.current_piece = SHAPES[shape]
        self.current_pos = {
            'x': BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2,
            'y': 0
        }
        
        # 게임 오버 체크
        if self.check_collision():
            self.game_over = True

    def check_collision(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_pos['x'] + x
                    new_y = self.current_pos['y'] + y
                    if (new_x < 0 or new_x >= BOARD_WIDTH or 
                        new_y >= BOARD_HEIGHT or 
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_pos['y'] + y][self.current_pos['x'] + x] = 1

    def clear_lines(self):
        lines_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(self.board[y]):
                lines_cleared += 1
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
            else:
                y -= 1
        self.score += lines_cleared * 100

    def draw(self):
        self.screen.fill(COLORS['BLACK'])
        
        # 보드 그리기
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS['BLUE'],
                                   [x * BLOCK_SIZE, y * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 현재 조각 그리기
        if self.current_piece:
            for y, row in enumerate(self.current_piece):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, COLORS['RED'],
                                       [(self.current_pos['x'] + x) * BLOCK_SIZE,
                                        (self.current_pos['y'] + y) * BLOCK_SIZE,
                                        BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 점수 표시
        score_text = self.font.render(f'Score: {self.score}', True, COLORS['WHITE'])
        self.screen.blit(score_text, (BOARD_WIDTH * BLOCK_SIZE + 10, 10))

        pygame.display.flip()

    def run(self):
        self.new_piece()
        fall_time = 0
        fall_speed = 1000  # 1초

        while not self.game_over:
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_pos['x'] -= 1
                        if self.check_collision():
                            self.current_pos['x'] += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_pos['x'] += 1
                        if self.check_collision():
                            self.current_pos['x'] -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_pos['y'] += 1
                        if self.check_collision():
                            self.current_pos['y'] -= 1
                            self.merge_piece()
                            self.clear_lines()
                            self.new_piece()
                    elif event.key == pygame.K_UP:
                        # 회전 구현
                        pass

            if fall_time >= fall_speed:
                self.current_pos['y'] += 1
                if self.check_collision():
                    self.current_pos['y'] -= 1
                    self.merge_piece()
                    self.clear_lines()
                    self.new_piece()
                fall_time = 0

            self.draw()

        # 게임 오버 화면
        game_over_text = self.font.render('Game Over!', True, COLORS['WHITE'])
        self.screen.blit(game_over_text, 
                        (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                         SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

if __name__ == '__main__':
    game = Tetris()
    game.run()
    pygame.quit()