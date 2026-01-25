pip install pygame

import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("dashing Bird")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 32)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
gravity = 0.5
bird_velocity = 0
jump_strength = -8

# Pipe settings
pipe_width = 60
pipe_gap = 150
pipe_speed = 3

pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Score
score = 0

def draw_bird(x, y):
    pygame.draw.circle(screen, WHITE, (x, int(y)), bird_radius)

def draw_pipes(x, height):
    top_pipe = pygame.Rect(x, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(x, height + pipe_gap, pipe_width, HEIGHT)
    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.rect(screen, GREEN, bottom_pipe)
    return top_pipe, bottom_pipe

def show_score(score):
    text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = FONT.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 20))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    # Removed sys.exit()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False   # Removed sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipe movement
    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Draw objects
    draw_bird(bird_x, bird_y)
    top_pipe, bottom_pipe = draw_pipes(pipe_x, pipe_height)
    show_score(score)

    # Collision detection
    bird_rect = pygame.Rect(
        bird_x - bird_radius,
        bird_y - bird_radius,
        bird_radius * 2,
        bird_radius * 2
    )

def game_over():
    text = FONT.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 20))
    pygame.display.update()
    pygame.time.delay(2000)
    # Instead of quitting here, just signal the loop to stop
    return True

# In the loop:
if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
    running = not game_over()

if bird_y < 0 or bird_y > HEIGHT:
    running = not game_over()

if not running:

    pygame.quit()   
