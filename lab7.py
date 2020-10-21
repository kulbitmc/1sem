class Target:
    def __init__(self, params):
        self.x = params['x']
        self.y = params['y']
        self.r = params['r']
        self.alpha = params['alpha']
        self.v = params['v']
        self.color = params['color']


class Circle(Target):
    def __init__(self, params):
        super().__init__(params)

    def wr(self):
        return self.color, (self.x, self.y), self.r


class Square(Target):
    def __init__(self, params):
        super().__init__(params)

    def wr(self):
        return self.color, (self.x, self.y, self.r, self.r)


import pygame
from pygame import draw
from random import randint
from math import cos, pi, sin, radians
pygame.init()

NUM = 3
MIN_R = 20
MAX_R = 100
WIDTH = 1200
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

f1 = pygame.font.SysFont('serif', 150)
text2 = f1.render("ENTER YOUR NAME", False, (0, 180, 0))
screen.blit(text2, (10, 10))
pygame.display.update()
new_name = input()
pygame.time.delay(2000)
screen.fill(BLACK)
pygame.display.update()

TYPE = ['CIRCLE', 'SQUARE']
circles = []
squares = []

count = 0


def new_target():
    """
    Функция new_target рисует новую мишень.
    """
    params = {
        'x': randint(MAX_R, WIDTH - MAX_R),
        'y': randint(MAX_R, HEIGHT - MAX_R),
        'r': randint(MIN_R, MAX_R),
        'v': float(randint(10, 1000)),
        'alpha': radians(randint(0, 360)),
        'color': COLORS[randint(0, 5)]
    }
    cur_type = TYPE[randint(0, 1)]
    if cur_type == 'CIRCLE':
        new_circle = Circle(params)
        circles.append(new_circle)
        draw.circle(screen, *circles[-1].wr())
    if cur_type == 'SQUARE':
        new_square = Square(params)
        squares.append(new_square)
        draw.rect(screen, *squares[-1].wr())
    pygame.display.update()


def move_targets():
    """
    Функция move_targets отвечает за передвижение мишеней по экрану.
    """
    for circle in circles:
        draw.circle(screen, BLACK, *circle.wr()[1:])
        circle.x += round(circle.v / FPS * cos(circle.alpha))
        circle.y -= round(circle.v / FPS * sin(circle.alpha))
        draw.circle(screen, *circle.wr())
        pygame.display.update()
    for square in squares:
        draw.rect(screen, BLACK, *square.wr()[1:])
        square.v *= randint(90, 110) / 100
        square.alpha += radians(randint(0, 10) - 5)
        square.x += round(square.v / FPS * cos(square.alpha))
        square.y -= round(square.v / FPS * sin(square.alpha))
        draw.rect(screen, *square.wr())
        pygame.display.update()
    check_walls()
    check_collide_circles()
    check_collide_squares()
    check_collide()


def table(points):
    """
    Функция обеспечивает вывод в левый верхний угол экрана таблички с текущим счетом игрока.
    :param points: текущее колличество очков
    """
    draw.rect(screen, YELLOW, (0, 0, 150, 40))
    my_font = pygame.font.Font(None, 30)
    string = "SCORE: " + str(points)
    if points < 0:
        text_color = GREEN
    else:
        text_color = BLACK
    text = my_font.render(string, True, text_color)
    screen.blit(text, (3, 3))


def check_collide_circles():
    """
    Функция проверяет столкновение кругов и реализует отскок
     """
    for i1 in range(len(circles) - 1):
        for i2 in range(i1 + 1, len(circles)):
            c1, c2 = circles[i1], circles[i2]
            d = ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** 0.5
            if d <= c1.r + c2.r:
                c1.alpha += pi
                c2.alpha += pi
                circles[i1] = c1
                circles[i2] = c2


def check_collide_squares():
    """
    Функция проверяет столкновение квадратов и реализует отскок
    """
    for i1 in range(len(squares) - 1):
        for i2 in range(i1 + 1, len(squares)):
            c1, c2 = squares[i1], squares[i2]
            a = abs (c1.x + (c1.r / 2) - (c2.x + (c2.r / 2)))
            b = abs (c1.y + (c1.r / 2) - (c2.y + (c2.r / 2)))
            if a <= c1.r / 2 + c2.r / 2 and b <= c1.r / 2 + c2.r / 2:
                c1.alpha += pi
                c2.alpha += pi
                squares[i1] = c1
                squares[i2] = c2


def check_collide():
    """
    Функция проверяет столкновение квадрата и круга и реализует отскок
    """
    for i1 in range(len(squares)):
        for i2 in range(len(circles)):
            c1, c2 = squares[i1], circles[i2]
            d = ((abs(c1.x + (c1.r / 2) - c2.x)) ** 2 + (abs(c1.y + (c1.r / 2) - c2.y)) ** 2) ** 0.5
            if d <= c2.r + (c1.r / ((2) ** 0.5)):
                c1.alpha += pi
                c2.alpha += pi
                squares[i1] = c1
                circles[i2] = c2


def check_walls():
    """
    Функция check_walls проверяет удар мишени о стенку и считает новый угол
    """
    for circle in circles:
        if circle.x + circle.r > WIDTH - 10:
            circle.alpha = radians(90 + randint(10, 170))
        if circle.x - circle.r < 0 + 10:
            circle.alpha = radians(randint(10, 170) - 90)
        if circle.y + circle.r > HEIGHT - 10:
            circle.alpha = radians(randint(10, 170))
        if circle.y - circle.r < 0 + 10:
            circle.alpha = radians(randint(10, 170) - 180)
    for square in squares:
        if square.x + square.r > WIDTH - 10:
            square.alpha = radians(90 + randint(10, 170))
        if square.x < 0 + 10:
            square.alpha = radians(randint(10, 170) - 90)
        if square.y + square.r > HEIGHT - 10:
            square.alpha = radians(randint(10, 170))
        if square.y < 0 + 10:
            square.alpha = radians(randint(10, 170) - 180)
        square.alpha %= 2 * pi


def check_click(ev):
    """
    Функция check_click проверяет попадание мышки в мишень, подсчитывает очки и создает новые мишени при необходимости.
    :param ev: параметры события
    """
    global count
    coord = ev.pos
    for circle in circles[:]:
        if (circle.x - coord[0]) ** 2 + (circle.y - coord[1]) ** 2 <= circle.r ** 2:
            count += 1
            circles.remove(circle)
            draw.circle(screen, BLACK, *circle.wr()[1:])
            new_target()
    for square in squares[:]:
        if 0 <= coord[0] - square.x <= square.r and 0 <= coord[1] - square.y <= square.r:
            count += 5
            squares.remove(square)
            draw.rect(screen, BLACK, *square.wr()[1:])
            new_target()


pygame.display.update()
clock = pygame.time.Clock()

finished = False


while not finished:
    clock.tick(FPS)
    for i in range(NUM):
        new_target()
    pygame.display.update()
    f = True
    while f:
        clock.tick(FPS)
        move_targets()
        table(count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event)
    screen.fill(BLACK)
    pygame.display.update()

pygame.quit()

creating = open('records.txt', 'a', encoding='utf-8')
creating.close()

old_records = open('records.txt', 'r', encoding='utf-8')

names = []
results = []

for line in old_records:
    line.rstrip()
    name, result = line.split(' ')
    names.append(name)
    results.append(int(result))

old_records.close()

f = True
for i in range(len(names)):
    if names[i] == new_name:
        f = False
        if count > results[i]:
            results[i] = count

if f:
    names.append(new_name)
    results.append(count)

for i in range(len(names)):
    for j in range(i, len(names)):
        if results[j] > results[i]:
            results[i], results[j] = results[j], results[i]
            names[i], names[j] = names[j], names[i]

new_records = open('records.txt', 'w', encoding='utf-8')

for i in range(len(names)):
    print(names[i], results[i], file=new_records)

new_records.close()
