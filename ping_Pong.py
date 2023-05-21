#ИМПОРТ МОДУЛЕЙ
from pygame import *
from random import randint

#ФУНКЦИЯ ДЛЯ СОЗДАНИЯ БОТИКА
def computer_move():
    if ball.rect.y > platform2.rect.y:
        platform2.rect.y += randint(2, 3)
    else:
        platform2.rect.y -= randint(2, 3)


#КЛАСС ДЛЯ СОЗДАНИЯ СПРАЙТА
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#КЛАСС ДЛЯ ДВИЖЕНИЯ ИГРОКА
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
#ПЕРЕМЕННЫЕ
back = (255, 228, 181)
width = 600
height = 500
window = display.set_mode((width, height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 60
#СОЗДАНИЕ СПРАЙТОВ
platform1 = Player('platform.png', 15, 200, 4, 150, 100)
platform2 = Player('platform2.png', 455, 200, 4, 150, 100)
ball = GameSprite('ball.png', 200, 200, 4, 100, 75) 

#ШРИФТ
font.init()
font = font.Font(None, 35)
#НАДПИСИ НА ИГРОВОМ ОКНЕ
lose1 = font.render('PLAYER 1 LOSE!', True, (0, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (0, 0, 0))

start_label = font.render('Press SPACE to start', True, (170, 0, 255))
window.blit(start_label, (200,200))
dx = 3
dy = 3
#ИГРОВОЙ ЦИКЛ
start = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                start = True

    if finish != True and start == True:
        window.fill(back)
        platform1.update_left()
        computer_move()
        ball.rect.x += dx
        ball.rect.y += dy
        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            dx *= -1
        if ball.rect.y > height - 50 or ball.rect.y < 0:
            dy *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))    

        platform1.reset()
        platform2.reset()
        ball.reset()

    display.update()
    clock.tick(fps)
