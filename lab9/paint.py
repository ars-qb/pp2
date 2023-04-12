import sys

import pygame
pygame.init()

# set the size of the screen
WIDTH, HEIGHT = 1000, 800

# set the frames per second
FPS = 60

# initialize some variables
draw = False
lastPos = (0, 0)

# define some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 100, 10)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

# define tools
BRUSH = 0x1
CLEANER = 0x2
ERASER = 0x3
RECTANGLE = 0x4
CIRCLE = 0x5
SQUARE = 0x6
RIGHT_TRIANGLE = 0x7
EQUILATERAL_TRIANGLE = 0x8
RHOMBUS = 0x9

NOTHING = 0x10

# set the initial mode, color, and radius
mode = BRUSH
color = BLACK
radius = 15

# create the screen and set its caption
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')

# set the clock
clock = pygame.time.Clock()

# fill the screen with white
screen.fill(WHITE)

# set up some fonts and images
font_66 = pygame.font.SysFont('Arial', 66)
font_45 = pygame.font.SysFont('Arial', 45)
plus = font_45.render("+", True, BLACK)
font = pygame.font.SysFont('Arial', 50)
minus = font_45.render("-", True, BLACK)

IMG_ERASER = pygame.transform.scale(pygame.image.load("source/paint/eraser.png"), (40, 40))
IMG_CLEANER = pygame.transform.scale(pygame.image.load("source/paint/cleaner.png"), (40, 40))
IMG_BRUSH = pygame.transform.scale(pygame.image.load("source/paint/brush.png"), (40, 40))
IMG_RIGHT_TRIANGLE = pygame.transform.scale(pygame.image.load("source/paint/right_triangle.png"), (50, 50))
IMG_EQUILATERAL_TRIANGLE = pygame.transform.scale(pygame.image.load("source/paint/equilateral_triangle.png"), (50, 60))
IMG_SQUARE = pygame.transform.scale(pygame.image.load("source/paint/square.png"), (50, 50))
IMG_RHOMBUS = pygame.transform.scale(pygame.image.load("source/paint/rhombus.png"), (50, 50))


# function for draw line
def drawLine(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

# function for draw circle
def drawCircle(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, color, (x, y), radius, tickness)

# function for draw rectangle
def drawRectangle(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, width, height), tickness)
    elif y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, color, (x2, y1, width, height), tickness)
    elif x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, width, height), tickness)
    elif x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, width, height), tickness)

# function for draw square
def drawSquare(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, color, (x1, y1, mn, mn), tickness)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, color, (x2, y1, mn, mn), tickness)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, color, (x2, y2, mn, mn), tickness)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, color, (x1, y2, mn, mn), tickness)


# function for draw right triangle
def drawRightTriangle(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), tickness)
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), tickness)
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), tickness)
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), tickness)

# function for draw equilateral triangle
def drawEquilateralTriangle(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width = abs(x2 - x1)
    height = (3 ** 0.5) * width / 2

    if y2 > y1:
        pygame.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), tickness)
    else:
        pygame.draw.polygon(screen, color, ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), tickness)

# function for draw rhombus
def drawRhombus(screen, start, end, tickness, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, color, True,
                      (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), tickness)

while True:

    # set Tools area
    TOOLS = pygame.draw.rect(screen, WHITE, (WIDTH-81, 22, 70, HEIGHT-170))

    # set Font size area
    BAR = pygame.draw.rect(screen, WHITE, (5, 5, 115, 75))


    # set tools button
    BUTTON_CLEANER = screen.blit(IMG_CLEANER, (WIDTH-70, HEIGHT-760))
    BUTTON_BRUSH = screen.blit(IMG_BRUSH, (WIDTH-70, HEIGHT-700))
    BUTTON_ERASER = screen.blit(IMG_ERASER, (WIDTH-70, HEIGHT-640))

    BUTTON_RECT = pygame.draw.rect(screen, BLACK, (WIDTH-70, HEIGHT-570, 50, 30), 2)
    BUTTON_CIRCLE = pygame.draw.circle(screen, BLACK, (WIDTH-40, HEIGHT-510), 18, 2)
    BUTTON_RIGHT_TRIANGLE = screen.blit(IMG_RIGHT_TRIANGLE, (WIDTH-70, HEIGHT-480))
    BUTTON_EQUILATERAL_TRIANGLE = screen.blit(IMG_EQUILATERAL_TRIANGLE, (WIDTH-70, HEIGHT-420))
    BUTTON_SQUARE = screen.blit(IMG_SQUARE, (WIDTH - 70, HEIGHT - 340))
    BUTTON_RHOMBUS = screen.blit(IMG_RHOMBUS, (WIDTH - 70, HEIGHT - 270))

    BUTTON_BLUE = pygame.draw.rect(screen, BLUE, (WIDTH-75, HEIGHT-360+160, 25, 25))
    BUTTON_RED = pygame.draw.rect(screen, RED, (WIDTH-45, HEIGHT-360+160, 25, 25))
    BUTTON_GREEN = pygame.draw.rect(screen, GREEN, (WIDTH-75, HEIGHT-320+160, 25, 25))
    BUTTON_BLACK = pygame.draw.rect(screen, BLACK, (WIDTH-45, HEIGHT-320+160, 25, 25))
    BUTTON_BROWN = pygame.draw.rect(screen, BROWN, (WIDTH-75, HEIGHT-280+160, 25, 25))
    BUTTON_ORANGE = pygame.draw.rect(screen, ORANGE, (WIDTH-45, HEIGHT-280+160, 25, 25))
    BUTTON_GREY = pygame.draw.rect(screen, GREY, (WIDTH-75, HEIGHT-240+160, 25, 25))
    BUTTON_YELLOW = pygame.draw.rect(screen, YELLOW, (WIDTH-45, HEIGHT-240+160, 25, 25))
    BUTTON_PURPLE = pygame.draw.rect(screen, PURPLE, (WIDTH-75, HEIGHT-200+160, 25, 25))
    BUTTON_PINK = pygame.draw.rect(screen, PINK, (WIDTH-45, HEIGHT-200+160, 25, 25))

    BUTTON_PLUS = screen.blit(plus, (85, 5))
    BUTTON_MINUS = screen.blit(minus, (90, 35))


    # get mouse pos
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            pos = event.pos

            # check if mouse pos collide with tools button pos
            # if collide set tool
            if TOOLS.collidepoint(pos) or BAR.collidepoint(pos):
                prevMode = mode
                mode = NOTHING

            if mode == BRUSH:
                pygame.draw.circle(screen, color, event.pos, radius)

            if BUTTON_RECT.collidepoint(pos):
                mode = RECTANGLE

            elif BUTTON_CIRCLE.collidepoint(pos):
                mode = CIRCLE

            elif BUTTON_RIGHT_TRIANGLE.collidepoint(pos):
                mode = RIGHT_TRIANGLE

            elif BUTTON_EQUILATERAL_TRIANGLE.collidepoint(pos):
                mode = EQUILATERAL_TRIANGLE

            elif BUTTON_SQUARE.collidepoint(pos):
                mode = SQUARE


            elif BUTTON_RHOMBUS.collidepoint(pos):
                mode = RHOMBUS

            if BUTTON_PLUS.collidepoint(pos):
                radius = min(99, radius + 1) # max size is  99

            elif BUTTON_MINUS.collidepoint(pos):
                radius = max(1, radius - 1) # min size is 1

            # check if mouse pos collide with colors button pos
            # if collide set color
            if BUTTON_BLUE.collidepoint(pos):
                color = BLUE

            elif BUTTON_RED.collidepoint(pos):
                color = RED

            elif BUTTON_GREEN.collidepoint(pos):
                color = GREEN

            elif BUTTON_BLACK.collidepoint(pos):
                color = BLACK

            elif BUTTON_BROWN.collidepoint(pos):
                color = BROWN

            elif BUTTON_ORANGE.collidepoint(pos):
                color = ORANGE

            elif BUTTON_GREY.collidepoint(pos):
                color = GREY

            elif BUTTON_YELLOW.collidepoint(pos):
                color = YELLOW

            elif BUTTON_PURPLE.collidepoint(pos):
                color = PURPLE

            elif BUTTON_PINK.collidepoint(pos):
                color = PINK

            elif BUTTON_BRUSH.collidepoint(pos):
                mode = BRUSH

            elif BUTTON_CLEANER.collidepoint(pos):
                mode = CLEANER

            elif BUTTON_ERASER.collidepoint(pos):
                mode = ERASER

        if event.type == pygame.MOUSEBUTTONUP:

            # check current mode
            if mode == NOTHING and (not TOOLS.collidepoint(event.pos) or not BAR.collidepoint(event.pos)):
                mode = prevMode
            if mode == RECTANGLE:
                drawRectangle(screen, pos, event.pos, radius, color)
            elif mode == CIRCLE:
                drawCircle(screen, pos, event.pos, radius, color)
            elif mode == SQUARE:
                drawSquare(screen, pos, event.pos, radius, color)
            elif mode == RHOMBUS:
                drawRhombus(screen, pos, event.pos, radius, color)
            elif mode == RIGHT_TRIANGLE:
                drawRightTriangle(screen, pos, event.pos, radius, color)
            elif mode == EQUILATERAL_TRIANGLE:
                drawEquilateralTriangle(screen, pos, event.pos, radius, color)
            elif mode == RHOMBUS:
                drawRhombus(screen, pos, event.pos, radius, color)
            elif mode == CLEANER:
                screen.fill(WHITE) # clean screen
                mode = BRUSH # change mode to BRUSH
            draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw and mode == BRUSH:
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == ERASER:
                drawLine(screen, lastPos, event.pos, radius, WHITE)

            lastPos = event.pos

    screen.blit(font_66.render(str(radius), True, color), (5, 5))
    pygame.display.flip()
    clock.tick(FPS)