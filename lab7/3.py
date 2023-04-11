import pygame


WIDTH = 800
HEIGHT = 600
FPS = 60
RED = (255, 0, 0)
WHITE = (255, 255, 255)
RADIUS = 25
SPEED = 10

direction = [0, 0]
pos = [WIDTH//2, HEIGHT//2]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_ball():
    pygame.draw.circle(screen, RED, pos, RADIUS)

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction[1] = -1
            elif event.key == pygame.K_DOWN:
                direction[1] = 1
            elif event.key == pygame.K_LEFT:
                direction[0] = -1
            elif event.key == pygame.K_RIGHT:
                direction[0] = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                direction[1] = 0
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                direction[0] = 0

    new_pos = [pos[0] + SPEED * direction[0], pos[1] + SPEED * direction[1]]
    if RADIUS <= new_pos[0] <= WIDTH - RADIUS:
        pos[0] = new_pos[0]
    if RADIUS <= new_pos[1] <= HEIGHT - RADIUS:
        pos[1] = new_pos[1]

    screen.fill(WHITE)

    draw_ball()
    pygame.display.update()

pygame.quit()
