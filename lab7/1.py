import pygame
import datetime

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
CENTER_X, CENTER_Y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

mickey = pygame.image.load("sprites/main-clock.png")
left_hand = pygame.image.load("sprites/left-hand.png")
right_hand = pygame.image.load("sprites/right-hand.png")
mickey_rect = mickey.get_rect()
current_time = datetime.datetime.now()
second = 78 - current_time.second * 6
minute = 78 - current_time.minute * 6
def blit_rotate_center(surface, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surface.blit(rotated_image, new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    second -= 0.099
    minute -= 0.00165

    screen.fill(WHITE)
    screen.blit(mickey, (CENTER_X, CENTER_Y))
    screen.blit(mickey, mickey_rect)

    blit_rotate_center(screen, left_hand, (CENTER_X, CENTER_Y), second)
    blit_rotate_center(screen, right_hand, (CENTER_X, CENTER_Y), minute)

    pygame.display.update()
