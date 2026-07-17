Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pygame
import random

pygame.init()
enemy_width = 50
enemy_height = 90

enemy_x = random.randint(110, 340)
enemy_y = -100

enemy_speed = 7
player_img = pygame.image.load("playercar.png")
enemy_img = pygame.image.load("enemycar.png")

player_img = pygame.transform.scale(player_img, (50, 90))
enemy_img = pygame.transform.scale(enemy_img, (50, 90))


# Window
WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodger")

clock = pygame.time.Clock()
FPS = 60

car_width = 50
car_height = 90

car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120

car_speed = 6

line_offset = 0
game_over = False
score = 0

font = pygame.font.SysFont(None, 40)
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    score = 0

                    car_x = WIDTH // 2 - car_width // 2
                    car_y = HEIGHT - 120

                    enemy_x = random.choice([125, 225, 325])
                    enemy_y = -100

                    line_offset = 0
        if not game_over:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and car_x > 110:
                car_x -= car_speed

            if keys[pygame.K_RIGHT] and car_x < 340:
                car_x += car_speed

            line_offset += 6

            if line_offset >= 50:
                line_offset = 0

            enemy_y += enemy_speed

            if enemy_y > HEIGHT:
                enemy_y = -100
                enemy_x = random.choice([125, 225, 325])
...                 score += 1
...     player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
...     enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
...     if player_rect.colliderect(enemy_rect):
...         game_over = True
...     # Grass
...     screen.fill((30, 120, 30))
... 
...     # Road
...     pygame.draw.rect(screen, (70, 70, 70), (100, 0, 300, HEIGHT))
... 
...     screen.blit(enemy_img, (enemy_x, enemy_y))
...     # Road Borders
...     pygame.draw.line(screen, (255, 255, 255), (100, 0), (100, HEIGHT), 5)
...     pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, HEIGHT), 5)
... 
...     # Center Lane
...     for y in range(-50, HEIGHT, 50):
...         pygame.draw.rect(screen, (255, 255, 0),
...                          (245, y + line_offset, 10, 30))
...     screen.blit(player_img, (car_x, car_y))
...     score_text = font.render(f"Score: {score}", True, (255, 255, 255))
...     screen.blit(score_text, (20, 20))
...     if game_over:
...         text = font.render("GAME OVER", True, (255, 0, 0))
...         screen.blit(text, (130, 300))
... 
...         restart = font.render("Press R to Restart", True, (255, 255, 255))
...         screen.blit(restart, (120, 350))
...     pygame.display.update()
... 
