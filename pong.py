import pygame
import sys
import random

pygame.init()

WIDTH = 900
HEIGHT = 600
FPS = 60

WHITE = (67, 255, 69)
BLACK = (0,255, 0)
GRAY = (255, 0, 25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spong")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 64)
small_font = pygame.font.Font(None, 32)

PADDLE_WIDTH = 16
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

BALL_SIZE = 16
BALL_SPEED_X = 6
BALL_SPEED_Y = 4

left_paddle = pygame.Rect(40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

left_score = 0
right_score = 0

ball_dx = BALL_SPEED_X * random.choice((-1, 1))
ball_dy = BALL_SPEED_Y * random.choice((-1, 1))


def reset_ball():
    global ball_dx, ball_dy

    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx = BALL_SPEED_X * random.choice((-1, 1))
    ball_dy = BALL_SPEED_Y * random.choice((-1, 1))


def move_paddles(keys):
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED


def move_ball():
    global ball_dx, ball_dy, left_score, right_score

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(left_paddle) and ball_dx < 0:
        ball.left = left_paddle.right
        ball_dx *= -1

    if ball.colliderect(right_paddle) and ball_dx > 0:
        ball.right = right_paddle.left
        ball_dx *= -1

    if ball.right < 0:
        right_score += 1
        reset_ball()

    if ball.left > WIDTH:
        left_score += 1
        reset_ball()


def draw():
    screen.fill(BLACK)

    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 2, y, 4, 18))

    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 30))
    screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width() // 2, 30))

    controls = small_font.render("Left: W/S    Right: Up/Down    Esc: Quit", True, GRAY)
    screen.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 40))

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

    keys = pygame.key.get_pressed()
    move_paddles(keys)
    move_ball()
    draw()

    clock.tick(FPS)
