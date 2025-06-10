import pygame
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏁 Reach the Goal Challenge")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Player and goal
player = pygame.Rect(250, 550, 30, 30)
goal = pygame.Rect(250, 50, 40, 40)
player_speed = 5

# Obstacles (add more as needed)
obstacles = [
    pygame.Rect(150, 200, 250, 20),
    pygame.Rect(100, 350, 300, 20),
    pygame.Rect(0, 100, 180, 20),
    pygame.Rect(360, 100, 180, 20)
]

# Font
font = pygame.font.SysFont(None, 36)

# Timer
time_limit = 20  # seconds
start_ticks = pygame.time.get_ticks()

# Game loop
running = True
won = False
while running:
    screen.fill(WHITE)

    # Time countdown
    seconds = time_limit - (pygame.time.get_ticks() - start_ticks) // 1000
    if seconds <= 0:
        text = font.render("⏱ Time's up! You lost.", True, BLACK)
        screen.blit(text, (120, 280))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Collision with walls
    for wall in obstacles:
        if player.colliderect(wall):
            text = font.render("💥 Hit an obstacle!", True, BLACK)
            screen.blit(text, (140, 280))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
            break

    # Win condition
    if player.colliderect(goal):
        text = font.render("🎉 You Win!", True, BLACK)
        screen.blit(text, (180, 280))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    # Draw everything
    pygame.draw.rect(screen, GREEN, goal)
    pygame.draw.rect(screen, RED, player)
    for wall in obstacles:
        pygame.draw.rect(screen, BLUE, wall)

    # Show timer
    timer_text = font.render(f"⏱ Time left: {seconds}s", True, BLACK)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()