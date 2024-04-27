import pygame
import random

# Инициализация библиотеки pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размер окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Размер ракетки
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Размер мяча
BALL_SIZE = 10

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def move(self, dy):
        self.y += dy

class Ball:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_SIZE)

    def move(self):
        self.x += self.dx
        self.y += self.dy

class PongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.player_paddle = Paddle(20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.computer_paddle = Paddle(WINDOW_WIDTH - 30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, random.choice([-1, 1]), random.choice([-1, 1]))

    def run(self):
        while not self.game_over:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player_paddle.move(-5)
            if keys[pygame.K_DOWN]:
                self.player_paddle.move(5)

            if self.ball.y <= 0 or self.ball.y >= WINDOW_HEIGHT:
                self.ball.dy *= -1

            if self.ball.x <= 0:
                self.game_over = True

            if self.ball.x >= WINDOW_WIDTH:
                self.ball.dx *= -1

            if self.ball.x <= self.player_paddle.x + PADDLE_WIDTH and self.player_paddle.y <= self.ball.y <= self.player_paddle.y + PADDLE_HEIGHT:
                self.ball.dx *= -1

            if self.ball.x >= self.computer_paddle.x - BALL_SIZE and self.computer_paddle.y <= self.ball.y <= self.computer_paddle.y + PADDLE_HEIGHT:
                self.ball.dx *= -1

            if self.ball.y < self.computer_paddle.y + PADDLE_HEIGHT // 2:
                self.computer_paddle.move(-3)
            if self.ball.y > self.computer_paddle.y + PADDLE_HEIGHT // 2:
                self.computer_paddle.move(3)

            self.ball.move()

            self.player_paddle.draw(self.screen)
            self.computer_paddle.draw(self.screen)
            self.ball.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = PongGame()
    game.run()