import pygame
import sys
import random

pygame.init()

WIDTH = 900
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHT_GREEN = (0, 255, 0)
RED = (255, 80, 80)
BLUE = (80, 120, 255)
YELLOW = (255, 220, 80)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 48)

PADDLE_WIDTH = 120
PADDLE_HEIGHT = 18
PADDLE_SPEED = 8

BALL_SIZE = 16
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

paddle = pygame.Rect(
    WIDTH // 2 - PADDLE_WIDTH // 2,
    HEIGHT - 50,
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

ball = pygame.Rect(
    WIDTH // 2 - BALL_SIZE // 2,
    HEIGHT // 2,
    BALL_SIZE,
    BALL_SIZE
)

ball_dx = BALL_SPEED_X * random.choice([-1, 1])
ball_dy = BALL_SPEED_Y

score = 0
lives = 3


def create_bricks():
    bricks = []
    brick_width = 80
    brick_height = 25
    gap = 8

    rows = 5
    cols = 10

    start_x = 35
    start_y = 60

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (brick_width + gap)
            y = start_y + row * (brick_height + gap)
            brick = pygame.Rect(x, y, brick_width, brick_height)
            bricks.append(brick)

    return bricks


bricks = create_bricks()


def reset_ball():
    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx = BALL_SPEED_X * random.choice([-1, 1])
    ball_dy = -5


def move_paddle(keys):
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED

    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += PADDLE_SPEED


def move_ball():
    global ball_dx, ball_dy, score, lives

    ball.x += ball_dx
    ball.y += ball_dy

    # Bounce off left and right walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1

    # Bounce off top wall
    if ball.top <= 0:
        ball_dy *= -1

    # Bounce off paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball.bottom = paddle.top
        ball_dy *= -1

    # Hit bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            score += 1
            break

    # Ball falls below screen
    if ball.top > HEIGHT:
        lives -= 1
        reset_ball()


def draw():
    screen.fill(BLACK)

    pygame.draw.rect(screen, BRIGHT_GREEN, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    colors = [RED, BLUE, YELLOW, BRIGHT_GREEN]

    for i, brick in enumerate(bricks):
        pygame.draw.rect(screen, colors[i % len(colors)], brick)

    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (WIDTH - 150, 20))

    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if lives <= 0:
        print("Game Over")
        pygame.quit()
        sys.exit()

    if len(bricks) == 0:
        print("You Win")
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    move_paddle(keys)
    move_ball()
    draw()

    clock.tick(FPS)
