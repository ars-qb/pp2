# Import necessary modules
import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Set constants for the game
WIDTH = 540
HEIGHT = 800
FPS = 60
MOVE_RATE = 5
ADD_RATE = 100

# Create the game screen and set its caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

# Set the clock
clock = pygame.time.Clock()

# Load the images for the game
road = pygame.transform.scale(pygame.image.load('source/racer/road.png'), (540, 800))
coin = pygame.transform.scale(pygame.image.load('source/racer/coin.png'), (30, 30))
bigcoin = pygame.transform.scale(pygame.image.load('source/racer/bigcoin.png'), (30, 30))
player = pygame.transform.scale(pygame.image.load('source/racer/player.png'), (50, 100))
car1 = pygame.transform.scale(pygame.image.load('source/racer/L.png'), (50, 100))
car2 = pygame.transform.scale(pygame.image.load('source/racer/R.png'), (50, 100))
score_img = pygame.transform.scale(pygame.image.load('source/racer/score.png'), (50, 50))

# Set variables for the game
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
next_level = 5
pygame.mixer.music.load('source/racer/car.wav')

# Define a function to check if the player has hit a wall
def playerHasHitWall(playerRect):
    if playerRect.collidelistall([leftWall, rightWall]):
        return True
    return

# Define a function to check if the player has hit a car
def playerHasHitCars(playerRect, cars):
    for c in cars:
        if playerRect.colliderect(c['rect']):
            return True
    return

# Define a function to check if the player has hit a coin
def playerHasHitCoins(playerRect, coins):
    for c in coins:
        if playerRect.colliderect(c['rect']):
            coins.remove(c)
            pygame.mixer.music.load('source/racer/coin.mp3')
            pygame.mixer.music.play(0, 0)
            pygame.mixer.music.load('source/racer/car.wav')
            pygame.mixer.music.play(-1, 0.0, 500)
            return c['score']
    return 0

# Play the background music
pygame.mixer.music.play(-1, 0.0)

# Main game loop
while running:

    # loop through all events in the queue
    for event in pygame.event.get():

        # if the event type is QUIT (window close button is clicked)
        if event.type == pygame.QUIT:
            # quit pygame
            pygame.quit()
            # exit the program
            sys.exit()

        # if the event type is KEYDOWN (a key on the keyboard is pressed down)
        if event.type == pygame.KEYDOWN:

            # check which key was pressed down
            if event.key == pygame.K_LEFT:
                # if left arrow key is pressed, set moveRight to False and moveLeft to True
                moveRight = False
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                # if right arrow key is pressed, set moveLeft to False and moveRight to True
                moveLeft = False
                moveRight = True
            elif event.key == pygame.K_UP:
                # if up arrow key is pressed, set moveDown to False and moveUp to True
                moveDown = False
                moveUp = True
            elif event.key == pygame.K_DOWN:
                # if down arrow key is pressed, set moveUp to False and moveDown to True
                moveUp = False
                moveDown = True
            elif event.key == pygame.K_SPACE:
                # if spacebar is pressed and the game is over, reset the game
                if game_over:
                    cars = []
                    coins = []
                    score = 0
                    playerRect.topleft = (WIDTH // 1.7, HEIGHT - 50)
                    moveLeft = moveRight = moveUp = moveDown = False
                    carAddCounter = 0
                    MOVE_RATE = 5
                    next_level = 5
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

        # Load the crash sound effect
        pygame.mixer.music.load('source/racer/crash.wav')

        # Fill the screen with a red color
        screen.fill((232, 92, 70))

        # Display the "game over" text at the center of the screen
        screen.blit(
            game_over_text, ((WIDTH - game_over_text.get_width()) // 2,
                             (HEIGHT - game_over_text.get_height() - game_over_text.get_height()) // 2))

        # Render the player's score and display it below the "game over" text
        score_text = font.render('Score: %i' % score, False, (153, 21, 0))
        screen.blit(
            score_text, ((WIDTH - score_text.get_width()) // 2,
                         (HEIGHT - score_text.get_height() - score_text.get_height()) // 2 + 45))


    else:

        carAddCounter += 1

        if carAddCounter == ADD_RATE:
            carAddCounter = 0
            # Choose random positions for cars on the left and right side of the screen
            randomL = random.choice([80, 90, 180, 200])
            randomR = random.choice([290, 310, 410, 420])
            # Create rectangles to represent the cars
            rectL = pygame.Rect(randomL, -50, 50, 100)
            rectR = pygame.Rect(randomR, HEIGHT + 50, 50, 100)
            # Create new car dictionaries with their respective properties
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
            # Choose random positions for coins on the left and right side of the screen
            randomCL = random.choice([80, 90, 180, 200])
            rectCL = pygame.Rect(randomCL, -50, 30, 30)
            randomCR = random.choice([290, 310, 410, 420])
            rectCR = pygame.Rect(randomCR, HEIGHT + 50, 30, 30)
            # Add the new cars to the cars list
            cars.append(newCarR)
            cars.append(newCarL)
            # Choose random type of coin
            coinType = random.randint(0, 1)
            # If the coin doesn't collide with the car, create a new coin on the left side of the screen
            if not rectCL.colliderect(rectL):
                newCoinL = {
                    'rect': rectCL,
                    'speed': speed,
                    'surface': (coin if coinType else bigcoin),
                    'type': 1,
                    'score': (1 if coinType else 3)
                }
                coins.append(newCoinL)
            coinType = random.randint(0, 1)
            ## If the coin doesn't collide with the car, create a new coin on the right side of the screen
            if not rectCR.colliderect(rectR):
                newCoinR = {
                    'rect': rectCR,
                    'speed': -speed,
                    'surface': (coin if coinType else bigcoin),
                    'type': 0,
                    'score': (1 if coinType else 3)
                }
                coins.append(newCoinR)
        # Move the player's rectangle left if the 'moveLeft' variable is True and the player's left edge is not at the left edge of the screen
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * MOVE_RATE, 0)

        # Move the player's rectangle right if the 'moveRight' variable is True and the player's right edge is not at the right edge of the screen
        if moveRight and playerRect.right < WIDTH:
            playerRect.move_ip(MOVE_RATE, 0)

        # Move the player's rectangle up if the 'moveUp' variable is True and the player's top edge is not at the top edge of the screen
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * MOVE_RATE)

        # Move the player's rectangle down if the 'moveDown' variable is True and the player's bottom edge is not at the bottom edge of the screen
        if moveDown and playerRect.bottom < HEIGHT:
            playerRect.move_ip(0, MOVE_RATE)

        # Move all cars and coins downwards based on their speed
        for c in cars:
            c['rect'].move_ip(0, c['speed'])

        for c in coins:
            c['rect'].move_ip(0, c['speed'])

        # Remove cars that have gone off the bottom of the screen or coins that have gone off the top of the screen
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

        # Check if the player has hit the wall and set the game_over variable to True if so
        if playerHasHitWall(playerRect):
            game_over = True

        # Draw the road at the top of the screen
        screen.blit(road, pygame.Rect(0, 0, 1080, 1916))

        # Draw the player's rectangle and all the cars and coins on the screen
        screen.blit(player, playerRect)
        for c in cars:
            screen.blit(c['surface'], c['rect'])

        for c in coins:
            screen.blit(c['surface'], c['rect'])

        # Check if the player has hit any of the cars and set the game_over variable to True if so
        if playerHasHitCars(playerRect, cars):
            game_over = True

        # Update the score based on whether the player has hit any coins
        score += playerHasHitCoins(playerRect, coins)

        # Render the score as text and draw it on the screen in the top right corner
        score_text = pygame.font.SysFont(None, 50).render(str(score), False, (0, 0, 0))
        h, w = score_text.get_height(), score_text.get_width()
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 50 - w, 15, 45 + w, 50))
        screen.blit(score_img, (WIDTH - 50, 20))
        screen.blit(score_text, (WIDTH - 45 - w, 30))

        # Check if the player has reached the score required for the next level and increase the speed and MOVE_RATE variables if so
        if score >= next_level:
            next_level = next_level + 5
            speed += 1
            MOVE_RATE += 0.3

    pygame.display.update()
    clock.tick(FPS)


