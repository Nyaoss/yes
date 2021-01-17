import pygame
from random import randrange as rnd
import sys
import os

w, h = 800, 600
fps = 120

e = False
n = False
hd = False
x = False

platform_width_e = 300
platform_height_e = 35
platform_speed_e = 8
platform_e = pygame.Rect(w // 2 - platform_width_e // 2, h - platform_height_e - 10,\
                     platform_width_e, platform_height_e)

platform_width_n = 200
platform_height_n = 25
platform_speed_n = 6
platform_n = pygame.Rect(w // 2 - platform_width_n // 2, h - platform_height_n - 10,\
                     platform_width_n, platform_height_n)

platform_width_h = 150
platform_height_h = 20
platform_speed_h = 4
platform_h = pygame.Rect(w // 2 - platform_width_h // 2, h - platform_height_h - 10,\
                     platform_width_h, platform_height_h)

platform_width_x = 100
platform_height_x = 15
platform_speed_x = 3.5
platform_x = pygame.Rect(w // 2 - platform_width_x // 2, h - platform_height_x - 10,\
                     platform_width_x, platform_height_x)

ball_radius_e = 16
ball_speed_e = 2
ball_rect_e = int(ball_radius_e * 2 ** 0.5)
ball_e = pygame.Rect(rnd(ball_rect_e, w - ball_rect_e), h // 2, ball_rect_e, ball_rect_e)

ball_radius_n = 12
ball_speed_n = 3
ball_rect_n = int(ball_radius_n * 2 ** 0.5)
ball_n = pygame.Rect(rnd(ball_rect_n, w - ball_rect_n), h // 2, ball_rect_n, ball_rect_n)

ball_radius_h = 8
ball_speed_h = 4
ball_rect_h = int(ball_radius_h * 2 ** 0.5)
ball_h = pygame.Rect(rnd(ball_rect_h, w - ball_rect_h), h // 2, ball_rect_h, ball_rect_h)

ball_radius_x = 4
ball_speed_x = 4.5
ball_rect_x = int(ball_radius_h * 2 ** 0.5)
ball_x = pygame.Rect(rnd(ball_rect_h, w - ball_rect_h), h // 2, ball_rect_h, ball_rect_h)

move_x, move_y = 1, -1

block_list_e = [pygame.Rect(160 * i, 25 * j, 160, 25) for i in range(5) for j in range(4)]
color_list_e = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(5) for j in range(4)]

block_list_n = [pygame.Rect(100 * i, 22.5 * j, 100, 22.5) for i in range(8) for j in range(5)]
color_list_n = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(8) for j in range(5)]

block_list_h = [pygame.Rect(80 * i, 20 * j, 80, 20) for i in range(10) for j in range(6)]
color_list_h = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(6)]

block_list_x = [pygame.Rect(20 * i, 5 * j, 20, 5) for i in range(40) for j in range(30)]
color_list_x = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(40) for j in range(30)]

pygame.init()
score = 0
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.mixer.music.load('data/music_system.mp3')
img_fon_e = pygame.image.load('data/background_easy.jpg').convert()
img_fon_n = pygame.image.load('data/background_normal.jpg').convert()
img_fon_h = pygame.image.load('data/background_hard.jpg').convert()
img_fon_x = pygame.image.load('data/background_extrime.jpg').convert()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["                Арканойд" ,
                  "             Правила игры:",
                  "     Вы должны разбить все",
                  "     кирпичики шариком,",
                  "    который отскакивает от",
                  "           платформы.",
                  "          ЖЕЛАЮ УДАЧИ!"]

    fon = pygame.transform.scale(load_image('start.jpg'), (w, h))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('Impact', 50)
    text_coord = 40
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    play_text = ["Нажмите любую кнопку "
                 "для начала"]
    font = pygame.font.Font(None, 40)
    text_coord = 525
    for line in play_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 125
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)

start_screen()

def difficult():
    global e
    global n
    global hd
    global x
    easy = ["Easy"]
    fon = pygame.transform.scale(load_image('start.jpg'), (w, h))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('Impact', 100)
    text_coord = 250
    for line in easy:
        string_rendered = font.render(line, 1, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 20
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    normal = ["Normal"]
    font = pygame.font.SysFont('Impact', 100)
    text_coord = 250
    for line in normal:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 230
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    hard = ["Hard"]
    font = pygame.font.SysFont('Impact', 100)
    text_coord = 250
    for line in hard:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 570
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    dif = ["Выберите уровень сложности:"]
    font = pygame.font.SysFont('Impact', 50)
    text_coord = 100
    for line in dif:
        string_rendered = font.render(line, 1, pygame.Color('blue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    aaa = ["Для выбора уровня сложности",
           "нажмите цифры 1, 2 и 3 соответственно"]
    font = pygame.font.SysFont('Impact', 30)
    text_coord = 400
    for line in aaa:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 5
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    e = True
                    pygame.mixer.music.play()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    n = True
                    pygame.mixer.music.play()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    hd = True
                    pygame.mixer.music.play()
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    x = True
                    pygame.mixer.music.play()
                    return
        pygame.display.flip()
        clock.tick(fps)

difficult()

def detect_collision(move_x, move_y, ball, rect):
    if move_x > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if move_y > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        move_x, move_y = -move_x, -move_y
    elif delta_x > delta_y:
        move_y = -move_y
    elif delta_y > delta_x:
        move_x = -move_x
    return move_x, move_y

while e:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    screen.blit(img_fon_e, (0, 0))

    [pygame.draw.rect(screen, color_list_e[color], block) for color, block in enumerate(block_list_e)]
    pygame.draw.rect(screen, pygame.Color('white'), platform_e)
    pygame.draw.circle(screen, pygame.Color('green'), ball_e.center, ball_radius_e)

    ball_e.x += ball_speed_e * move_x
    ball_e.y += ball_speed_e * move_y

    if ball_e.centerx < ball_radius_e or ball_e.centerx > w - ball_radius_e:
        move_x = -move_x
    if ball_e.centery < ball_radius_e:
        move_y = -move_y
    if ball_e.colliderect(platform_e) and move_y > 0:
        move_x, move_y = detect_collision(move_x, move_y, ball_e, platform_e)
    hit_index = ball_e.collidelist(block_list_e)
    if hit_index != -1:
        hit_rect = block_list_e.pop(hit_index)
        hit_color = color_list_e.pop(hit_index)
        move_x, move_y = detect_collision(move_x, move_y, ball_e, hit_rect)
        fps += 1.5
        score += 1

    if ball_e.bottom > h:
        lose = ["Вы проиграли!",
                "Перезайдите чтобы",
                "попробовать еще раз!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in lose:
            string_rendered = font.render(line, 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        score_text = ["Score - {}".format(score)]
        font = pygame.font.Font(None, 80)
        text_coord = 400
        for line in score_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    elif not len(block_list_e):
        win = ["Вы выиграли!",
                "Перезайдите чтобы",
                "сыграть вновь!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in win:
            string_rendered = font.render(line, 1, pygame.Color('green'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 100
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and platform_e.left > 0:
        platform_e.left -= platform_speed_e
    if key[pygame.K_d] and platform_e.right < w:
        platform_e.right += platform_speed_e

    pygame.display.flip()
    clock.tick(fps)

while n:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    screen.blit(img_fon_n, (0, 0))

    [pygame.draw.rect(screen, color_list_n[color], block) for color, block in enumerate(block_list_n)]
    pygame.draw.rect(screen, pygame.Color('white'), platform_n)
    pygame.draw.circle(screen, pygame.Color('yellow'), ball_n.center, ball_radius_n)

    ball_n.x += ball_speed_n * move_x
    ball_n.y += ball_speed_n * move_y

    if ball_n.centerx < ball_radius_n or ball_n.centerx > w - ball_radius_n:
        move_x = -move_x
    if ball_n.centery < ball_radius_n:
        move_y = -move_y
    if ball_n.colliderect(platform_n) and move_y > 0:
        move_x, move_y = detect_collision(move_x, move_y, ball_n, platform_n)
    hit_index = ball_n.collidelist(block_list_n)
    if hit_index != -1:
        hit_rect = block_list_n.pop(hit_index)
        hit_color = color_list_n.pop(hit_index)
        move_x, move_y = detect_collision(move_x, move_y, ball_n, hit_rect)
        fps += 1
        score += 1

    if ball_n.bottom > h:
        lose = ["Вы проиграли!",
                "Перезайдите чтобы",
                "попробовать еще раз!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in lose:
            string_rendered = font.render(line, 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        score_text = ["Score - {}".format(score)]
        font = pygame.font.Font(None, 80)
        text_coord = 400
        for line in score_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    elif not len(block_list_n):
        win = ["Вы выиграли!",
                "Перезайдите чтобы",
                "сыграть вновь!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in win:
            string_rendered = font.render(line, 1, pygame.Color('green'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 100
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and platform_n.left > 0:
        platform_n.left -= platform_speed_n
    if key[pygame.K_d] and platform_n.right < w:
        platform_n.right += platform_speed_n

    pygame.display.flip()
    clock.tick(fps)

while hd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    screen.blit(img_fon_h, (0, 0))

    [pygame.draw.rect(screen, color_list_h[color], block) for color, block in enumerate(block_list_h)]
    pygame.draw.rect(screen, pygame.Color('white'), platform_h)
    pygame.draw.circle(screen, pygame.Color('red'), ball_h.center, ball_radius_h)

    ball_h.x += ball_speed_h * move_x
    ball_h.y += ball_speed_h * move_y

    if ball_h.centerx < ball_radius_h or ball_h.centerx > w - ball_radius_h:
        move_x = -move_x
    if ball_h.centery < ball_radius_h:
        move_y = -move_y
    if ball_h.colliderect(platform_h) and move_y > 0:
        move_x, move_y = detect_collision(move_x, move_y, ball_h, platform_h)
    hit_index = ball_h.collidelist(block_list_h)
    if hit_index != -1:
        hit_rect = block_list_h.pop(hit_index)
        hit_color = color_list_h.pop(hit_index)
        move_x, move_y = detect_collision(move_x, move_y, ball_h, hit_rect)
        fps += 0.5
        score += 1

    if ball_h.bottom > h:
        lose = ["Вы проиграли!",
                "Перезайдите чтобы",
                "попробовать еще раз!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in lose:
            string_rendered = font.render(line, 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        score_text = ["Score - {}".format(score)]
        font = pygame.font.Font(None, 80)
        text_coord = 400
        for line in score_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    elif not len(block_list_h):
        win = ["Вы выиграли!",
                "Перезайдите чтобы",
                "сыграть вновь!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in win:
            string_rendered = font.render(line, 1, pygame.Color('green'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 100
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and platform_h.left > 0:
        platform_h.left -= platform_speed_h
    if key[pygame.K_d] and platform_h.right < w:
        platform_h.right += platform_speed_h

    pygame.display.flip()
    clock.tick(fps)

while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    screen.blit(img_fon_x, (0, 0))

    [pygame.draw.rect(screen, color_list_x[color], block) for color, block in enumerate(block_list_x)]
    pygame.draw.rect(screen, pygame.Color('white'), platform_x)
    pygame.draw.circle(screen, pygame.Color('#ffd800'), ball_x.center, ball_radius_x)

    ball_x.x += ball_speed_x * move_x
    ball_x.y += ball_speed_x * move_y

    if ball_x.centerx < ball_radius_x or ball_x.centerx > w - ball_radius_x:
        move_x = -move_x
    if ball_x.centery < ball_radius_x:
        move_y = -move_y
    if ball_x.colliderect(platform_x) and move_y > 0:
        move_x, move_y = detect_collision(move_x, move_y, ball_x, platform_x)
    hit_index = ball_x.collidelist(block_list_x)
    if hit_index != -1:
        hit_rect = block_list_x.pop(hit_index)
        hit_color = color_list_x.pop(hit_index)
        move_x, move_y = detect_collision(move_x, move_y, ball_x, hit_rect)
        fps += 0.2
        score += 1

    if ball_x.bottom > h:
        lose = ["Вы проиграли!",
                "Перезайдите чтобы",
                "попробовать еще раз!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in lose:
            string_rendered = font.render(line, 1, pygame.Color('yellow'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        score_text = ["Score - {}".format(score)]
        font = pygame.font.Font(None, 80)
        text_coord = 400
        for line in score_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 35
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    elif not len(block_list_x):
        win = ["Вы выиграли!",
                "Перезайдите чтобы",
                "сыграть вновь!"]

        font = pygame.font.Font(None, 100)
        text_coord = 130
        for line in win:
            string_rendered = font.render(line, 1, pygame.Color('green'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 100
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    terminate()
            pygame.display.flip()
            clock.tick(fps)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and platform_x.left > 0:
        platform_x.left -= platform_speed_x
    if key[pygame.K_d] and platform_x.right < w:
        platform_x.right += platform_speed_x

    pygame.display.flip()
    clock.tick(fps)
