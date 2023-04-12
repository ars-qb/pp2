import random
import pygame
import sys
pygame.init()

WIDTH = 540
HEIGHT = 800
FPS = 60
MOVE_RATE = 5
ADD_RATE = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')
clock = pygame.time.Clock()

road = pygame.transform.scale(pygame.image.load('source/racer/road.png'), (540, 800))
coin = pygame.transform.scale(pygame.image.load('source/racer/coin.png'), (20, 20))
player = pygame.transform.scale(pygame.image.load('source/racer/player.png'), (50, 100))
car1 = pygame.transform.scale(pygame.image.load('source/racer/L.png'), (50, 100))
car2 = pygame.transform.scale(pygame.image.load('source/racer/R.png'), (50, 100))
score_img = pygame.transform.scale(pygame.image.load('source/racer/score.png'), (50, 50))
running = True
game_over = False


playerRect = player.get_rect()
moveLeft = moveRight = moveUp = moveDown = False
playerRect.topleft = (WIDTH // 1.7, HEIGHT - 50)

leftWall = pygame.Rect(0, 0, 50, HEIGHT)
rightWall = pygame.Rect(WIDTH-50, 0, 50, HEIGHT)
cars = []
coins = []

font = pygame.font.SysFont(None, 72)
game_over_text = font.render('Game Over', False, (153, 21, 0))

score = 0
carAddCounter = 0
speed = 5

pygame.mixer.music.load('source/racer/car.wav')

def playerHasHitWall(playerRect):

    if playerRect.collidelistall([leftWall, rightWall]):
        return True

    return

def playerHasHitCars(playerRect, cars):

    for c in cars:
        if playerRect.colliderect(c['rect']):
            return True

    return

def playerHasHitCoins(playerRect, coins):

    for c in coins:
        if playerRect.colliderect(c['rect']):
            coins.remove(c)
            pygame.mixer.music.load('source/racer/coin.mp3')
            pygame.mixer.music.play(0, 0)
            pygame.mixer.music.load('source/racer/car.wav')
            pygame.mixer.music.play(-1, 0.0, 500)
            return True
    return


pygame.mixer.music.play(-1, 0.0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveRight = False
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                moveLeft = False
                moveRight = True
            elif event.key == pygame.K_UP:
                moveDown = False
                moveUp = True
            elif event.key == pygame.K_DOWN:
                moveUp = False
                moveDown = True

            elif event.key == pygame.K_SPACE:
                if game_over:
                    cars = []
                    coins = []
                    score = 0
                    playerRect.topleft = (WIDTH // 1.7, HEIGHT - 50)
                    moveLeft = moveRight = moveUp = moveDown = False
                    carAddCounter = 0
                    game_over = False
                    pygame.mixer.music.load('source/racer/car.wav')
                    pygame.mixer.music.play(-1, 0.0)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                moveLeft = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False
            elif event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_DOWN:
                moveDown = False


    if game_over:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('source/racer/crash.wav')
        screen.fill((232, 92, 70))
        screen.blit(
            game_over_text, ((WIDTH - game_over_text.get_width()) // 2,
                             (HEIGHT - game_over_text.get_height() - game_over_text.get_height()) // 2))
        score_text = font.render('Score: %i' % score, False, (153, 21, 0))
        screen.blit(
            score_text, ((WIDTH - score_text.get_width()) // 2,
                         (HEIGHT - score_text.get_height() - score_text.get_height()) // 2 + 45))

    else:

        carAddCounter += 1

        if carAddCounter == ADD_RATE:
            carAddCounter = 0
            randomL = random.choice([80, 90, 180, 200])
            randomR = random.choice([290, 310, 410, 420])
            rectL = pygame.Rect(randomL, -50, 50, 100)
            rectR = pygame.Rect(randomR, HEIGHT+50, 50, 100)
            newCarL = {
                            'rect': rectL,
                            'speed': speed,
                            'surface': car1,
                            'type': 1
            }

            newCarR = {
                            'rect': rectR,
                            'speed': -speed,
                            'surface': car2,
                            'type': 0
            }
            randomCL = random.choice([80, 90, 180, 200])
            rectCL = pygame.Rect(randomCL, -50, 20, 20)
            randomCR = random.choice([290, 310, 410, 420])
            rectCR = pygame.Rect(randomCR, HEIGHT+50, 20, 20)
            cars.append(newCarR)
            cars.append(newCarL)
            if not rectCL.colliderect(rectL):
                newCoinL = {
                    'rect': rectCL,
                    'speed': speed,
                    'surface': coin,
                    'type': 1

                }
                coins.append(newCoinL)

            if not rectCR.colliderect(rectR):
                newCoinR = {
                    'rect': rectCR,
                    'speed': -speed,
                    'surface': coin,
                    'type': 0

                }
                coins.append(newCoinR)



        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * MOVE_RATE, 0)
        if moveRight and playerRect.right < WIDTH:
            playerRect.move_ip(MOVE_RATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * MOVE_RATE)
        if moveDown and playerRect.bottom < HEIGHT:
            playerRect.move_ip(0, MOVE_RATE)

        for c in cars:
            c['rect'].move_ip(0, c['speed'])

        for c in coins:
            c['rect'].move_ip(0, c['speed'])

        for c in cars[:]:
            if c['type']:
                if c['rect'].top > HEIGHT:
                    cars.remove(c)
            else:
                if c['rect'].top < -100:
                    cars.remove(c)

        for c in coins[:]:
            if c['type']:
                if c['rect'].top > HEIGHT:
                    coins.remove(c)
            else:
                if c['rect'].top < -100:
                    coins.remove(c)

        if playerHasHitWall(playerRect):
            game_over = True

        screen.blit(road, pygame.Rect(0,0,1080,1916))

        screen.blit(player, playerRect)
        for c in cars:
            screen.blit(c['surface'], c['rect'])

        for c in coins:
            screen.blit(c['surface'], c['rect'])

        if playerHasHitCars(playerRect, cars):
            game_over = True

        if playerHasHitCoins(playerRect, coins):
            score += 1


        score_text = pygame.font.SysFont(None, 50).render(
            str(score), False, (0, 0, 0))

        h, w = score_text.get_height(), score_text.get_width()
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 50  - w, 15, 45 + w, 50))
        screen.blit(score_img, (WIDTH - 50, 20))

        screen.blit(score_text, (WIDTH - 45 - w, 30))

    pygame.display.update()
    clock.tick(FPS)


