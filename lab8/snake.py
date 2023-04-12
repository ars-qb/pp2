import pygame
import random
import time
pygame.init()
FPS = 10
WIDTH = 800
HEIGHT = 800
board_size = WIDTH * 0.8, HEIGHT * 0.8
window_pos = ((WIDTH-board_size[0])//2, (HEIGHT-board_size[1])//2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
pygame.font.init()
font = pygame.font.SysFont(None, 72)

class Fruit():
    def __init__(self, window, window_pos, item_size):
        self.window_pos = window_pos
        self.window = window
        self.item_size = item_size
        self.color = 221, 75, 57
        self.surface = pygame.image.load('source/snake/apple.png')
        self.randomize()

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.item_size, self.item_size)
        surface = pygame.transform.scale(self.surface, (self.item_size, self.item_size))
        screen.blit(surface, rect)

    def randomize(self):
        x = random.randrange(0, board_size[0])
        y = random.randrange(0, board_size[1])
        x += self.window_pos[0]
        y += self.window_pos[1]

        self.x = x-x % self.item_size
        self.y = y-y % self.item_size


class Snake():
    def __init__(self, window, window_size, window_pos, item_size):
        self.window = window
        self.window_size = window_size
        self.window_pos = window_pos

        self.item_size = item_size
        self.color = 66, 133, 244
        self.head_color = 70, 100, 232
        self.reset()

    def reset(self):
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
        head = self.snake[0]
        self.future_item = self.snake.pop()
        self.snake.insert(0, {
            'x': (head['x'] - self.window_pos[0] + self.dx*self.item_size)  + self.window_pos[0],
            'y': (head['y'] - self.window_pos[1] + self.dy*self.item_size)  + self.window_pos[1]
        })

    def draw(self):
        for i, item in enumerate(self.snake):
            color = self.color
            if i == 0:
                color = self.head_color

            self.rect = pygame.draw.rect(
                self.window, color, (item['x'], item['y'], self.item_size, self.item_size))

    def eat(self, fruit):
        head = self.snake[0]
        return abs(head['x']-fruit.x) < 20 and abs(head['y']-fruit.y) < 20

    def overlap(self):
        return self.snake.count(self.snake[0]) > 1

    def grow(self):
        self.snake.append(self.future_item)

    def hasHitWall(self):
        head = self.snake[0]
        if head['x'] < self.window_pos[0] or head['x'] >= self.window_pos[0] + self.window_size[0]:
            return True
        if head['y'] < self.window_pos[1] or head['y'] >= self.window_pos[1] + self.window_size[1]:
            return True
        return False


score = 0
level = 1
score_next_level = 5
game_started = False


snake = Snake(screen, window_size=board_size,
              window_pos=((WIDTH - board_size[0]) // 2,
                          (HEIGHT - board_size[1]) // 2),
              item_size=20)
fruit = Fruit(screen, window_pos, item_size=20)

apple_image = {
    'size': {
        'width': 40,
        'height': 40
    }
}

apple_image['pos'] = {
    'x': (window_pos[0] - apple_image['size']['width']) // 2,
    'y': (window_pos[1] - apple_image['size']['height']) // 2,
}
apple_image['image'] = pygame.transform.scale(
    pygame.image.load('source/snake/apple.png'), (apple_image['size']['width'], apple_image['size']['height']))


trophy_image = {
    'size': {
        'width': 40,
        'height': 40
    }
}

trophy_image['pos'] = {
    'x': (WIDTH-apple_image['pos']['x']-trophy_image['size']['width']),
    'y': (window_pos[1] - apple_image['size']['height']) // 2,
}
trophy_image['image'] = pygame.transform.scale(
    pygame.image.load('source/snake/trophy.png'), (trophy_image['size']['width'], trophy_image['size']['height']))


clock = pygame.time.Clock()
game_over = False


game_over_text = font.render('Game Over.', False, (153, 21, 0))

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

        screen.fill((232, 92, 70))

        screen.blit(
            game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height() - game_over_text.get_height()) // 2))
        score_text = font.render('Score: %i' % score, False, (153, 21, 0))
        screen.blit(
            score_text, ((WIDTH - score_text.get_width()) // 2, (HEIGHT - score_text.get_height() - score_text.get_height()) // 2 + 45))

        pygame.display.update()
        clock.tick(1)
    else:
        score_text = pygame.font.SysFont(None, 20).render(
            str(score), False, (200, 200, 200))
        level_text = pygame.font.SysFont(None, 20).render(
            str(level), False, (200, 200, 200))

        screen.fill((86, 138, 52))
        pygame.draw.rect(screen, (170, 215, 81),
                         (window_pos[0], window_pos[1], board_size[0], board_size[1]))

        pygame.draw.rect(screen, (74, 117, 44),
                         (0, 0, WIDTH, window_pos[1]))

        snake.move()

        fruit.draw()
        if snake.eat(fruit):
            snake.grow()
            score += 1
            if score >= score_next_level:
                level += 1
                score_next_level += 5
                FPS += 3
            fruit.randomize()
        if snake.overlap():
            # game over
            game_over = True
            time.sleep(1)

        if not snake.hasHitWall():
            snake.draw()
        else:
            game_over = True



        screen.blit(
            apple_image['image'], (apple_image['pos']['x'], apple_image['pos']['y']))
        screen.blit(
            score_text, (apple_image['pos']['x']+apple_image['size']['width'], apple_image['pos']['y']+10))
        screen.blit(
            trophy_image['image'], (trophy_image['pos']['x'], trophy_image['pos']['y']))
        screen.blit(
            level_text, (trophy_image['pos']['x']-10, trophy_image['pos']['y']+10))

        pygame.display.update()

        clock.tick(FPS)