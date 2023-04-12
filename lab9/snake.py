import pygame
import random
from time import sleep

pygame.init()

# Game Constants
FPS = 5
WIDTH = 600
HEIGHT = 600
BIGFRUIT_RATE = 10

# Board Constants
board_size = WIDTH * 0.8, HEIGHT * 0.8
window_pos = ((WIDTH-board_size[0])//2, (HEIGHT-board_size[1])//2)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Set up fonts
pygame.font.init()
font = pygame.font.SysFont(None, 72)
game_over_text = font.render('Game Over.', False, (153, 21, 0))

# Fruit class
class Fruit():
    def __init__(self, window, window_pos):
        self.window_pos = window_pos
        self.window = window
        self.item_size = 20
        self.surface = pygame.image.load('source/snake/apple.png')
        self.randomize()

    def draw(self):
        # Draw fruit on screen
        rect = pygame.Rect(self.x, self.y, self.item_size, self.item_size)
        surface = pygame.transform.scale(self.surface, (self.item_size, self.item_size))
        screen.blit(surface, rect)

    def randomize(self):
        # Place fruit in a random position on the board
        x = random.randrange(0, board_size[0])
        y = random.randrange(0, board_size[1])
        x += self.window_pos[0]
        y += self.window_pos[1]

        self.x = x - x % self.item_size
        self.y = y-y % self.item_size

# BigFruit class
class bigFruit():
    def __init__(self, window, window_pos):
        self.window_pos = window_pos
        self.window = window
        self.item_size = 30
        self.surface = pygame.image.load('source/snake/goldapple.png')
        self.randomize()

    def draw(self):
        # Draw big fruit on screen
        rect = pygame.Rect(self.x, self.y, 30, 30)
        surface = pygame.transform.scale(self.surface, (30, 30))
        screen.blit(surface, rect)

    def randomize(self):
        # Place big fruit in a random position on the board
        x = random.randrange(0, board_size[0])
        y = random.randrange(0, board_size[1])
        x += self.window_pos[0]
        y += self.window_pos[1]

        self.x = x - x % self.item_size
        self.y = y-y % self.item_size

# Snake class
class Snake():
    def __init__(self, window, window_size, window_pos, item_size):
        # Initialize snake object with required parameters
        self.window = window
        self.window_size = window_size
        self.window_pos = window_pos

        self.item_size = item_size
        self.color = 66, 133, 244
        self.head_color = 70, 100, 232
        self.reset()

    def reset(self):
        # Reset snake to initial state
        x = self.window_size[0]//2+self.window_pos[0]
        y = self.window_size[1]//2+self.window_pos[1]
        self.snake = [
            {
                'x': x,
                'y': y
            }
        ]
        self.future_item = None
        self.dx = 1
        self.dy = 0

    def move(self):
        # Move the snake in the current direction
        head = self.snake[0]
        self.future_item = self.snake.pop()
        self.snake.insert(0, {
            'x': (head['x'] - self.window_pos[0] + self.dx*self.item_size) % (self.window_size[0]) + self.window_pos[0],
            'y': (head['y'] - self.window_pos[1] + self.dy*self.item_size) % (self.window_size[1]) + self.window_pos[1]
        })

    def draw(self):
        # Draw the snake on the screen
        for i, item in enumerate(self.snake):
            color = self.color
            if i == 0:
                color = self.head_color

            pygame.draw.rect(
                self.window, color, (item['x'], item['y'], self.item_size, self.item_size))

    def eat(self, fruit):
        # Check if the snake has eaten the fruit
        head = self.snake[0]
        return abs(head['x']-fruit.x) < 20 and abs(head['y']-fruit.y) < 20

    def overlap(self):
        # Check if the snake has collided with itself
        return self.snake.count(self.snake[0]) > 1

    def grow(self, s):
        # Make the snake grow by s segments
        for _ in range(s):
            self.snake.append(self.future_item)


# Initialize game variables
score = 0
level = 1
score_next_level = 5
game_started = False

# Initialize snake and fruit objects
snake = Snake(screen, window_size=board_size,
              window_pos=((WIDTH - board_size[0]) // 2,
                          (HEIGHT - board_size[1]) // 2),
              item_size=20)
fruit = Fruit(screen, window_pos)
bigFruit = bigFruit(snake, window_pos)

# Load images for apple and trophy icons
apple_image = {
    'pos': {
        'x': (window_pos[0] - 40) // 2,
        'y': (window_pos[1] - 40) // 2,
        },
    'image': pygame.transform.scale(pygame.image.load('source/snake/apple.png'), (40, 40))
}

trophy_image = {
    'pos': {
        'x': (WIDTH-80),
        'y': (window_pos[1] - 40) // 2,
            },
    'image': pygame.transform.scale(pygame.image.load('source/snake/trophy.png'), (40, 40))
}

# Set up game clock and initial game state
clock = pygame.time.Clock()
game_over = False

# Set up message to display at end of game
press_spacebar_to_play_again = {
    "text": pygame.font.SysFont(None, 24).render('Press SPACEBAR to play again.', False, (153, 21, 0)),
    "hidden": True
}

# Initialize big fruit counter
BigCounter = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx <= 0:
                snake.dx = -1
                snake.dy = 0
                continue
            elif event.key == pygame.K_RIGHT and snake.dx >= 0:
                snake.dx = 1
                snake.dy = 0
                continue
            elif event.key == pygame.K_UP and snake.dy <= 0:
                snake.dx = 0
                snake.dy = -1
                continue
            elif event.key == pygame.K_DOWN and snake.dy >= 0:
                snake.dx = 0
                snake.dy = 1
                continue
            elif event.key == pygame.K_SPACE:
                if game_over:
                    snake.reset()
                    score = 0
                    game_over = False

    if game_over:
        # Fill the screen with a red color
        screen.fill((232, 92, 70))

        # Display the "game over" text at the center of the screen
        screen.blit(
            game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height() - game_over_text.get_height()) // 2))

        # Render the player's score and display it below the "game over" text
        score_text = font.render('Score: %i' % score, False, (153, 21, 0))
        screen.blit(
            score_text, ((WIDTH - score_text.get_width()) // 2, (HEIGHT - score_text.get_height() - score_text.get_height()) // 2 + 45))

        pygame.display.update()
        clock.tick(1)
    else:
        # Render the score and level text
        score_text = pygame.font.SysFont(None, 20).render(
            str(score), False, (200, 200, 200))
        level_text = pygame.font.SysFont(None, 20).render(
            str(level), False, (200, 200, 200))

        # Fill the screen with a green color
        screen.fill((86, 138, 52))

        # Draw a rectangle to represent the game board
        pygame.draw.rect(screen, (170, 215, 81),
                         (window_pos[0], window_pos[1], board_size[0], board_size[1]))

        # Draw a rectangle to represent the score and level section
        pygame.draw.rect(screen, (74, 117, 44),
                         (0, 0, WIDTH, window_pos[1]))

        # Move the snake and draw the fruit
        snake.move()
        fruit.draw()

        # Draw the big fruit if the conditions are met
        if BigCounter > BIGFRUIT_RATE and BigCounter < BIGFRUIT_RATE * 3:
            bigFruit.draw()

        if BigCounter > BIGFRUIT_RATE * 3 and BigCounter < BIGFRUIT_RATE * 5:
            if BigCounter % 3 == 0:
                bigFruit.draw()

        if BigCounter > BIGFRUIT_RATE * 5:
            BigCounter = 0

        # Increment the big fruit counter
        BigCounter += 1

        # Check if the snake has eaten the fruit
        if snake.eat(fruit):
            # Increase the snake's length, score, and level if necessary
            snake.grow(1)
            score += 1
            if score >= score_next_level:
                level += 1
                score_next_level += 5
                FPS += 1

            # Randomize the fruit's position
            fruit.randomize()

        # Check if the snake has eaten the big fruit
        if snake.eat(bigFruit):
            # Increase the snake's length, score, and level if necessary
            snake.grow(2)
            score += 3
            if score >= score_next_level:
                level += 1
                score_next_level += 5
                FPS += 1
            BigCounter = 0
            bigFruit.randomize()

        # Check if the snake has collided with itself
        if snake.overlap():
            # Set the game over flag and wait for a second
            game_over = True
            sleep(1)

        # Draw the snake, apple image, score text, trophy image, and level text
        snake.draw()
        screen.blit(
            apple_image['image'], (apple_image['pos']['x'], apple_image['pos']['y']))
        screen.blit(
            score_text, (apple_image['pos']['x'] + 40, apple_image['pos']['y'] + 10))
        screen.blit(
            trophy_image['image'], (trophy_image['pos']['x'], trophy_image['pos']['y']))
        screen.blit(
            level_text, (trophy_image['pos']['x'] - 10, trophy_image['pos']['y'] + 10))

        # Update the display and wait for the specified number of frames
        pygame.display.flip()
        clock.tick(FPS)
