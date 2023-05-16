#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((600,400))

clock = time.Clock()
FPS = 60


font.init()
mixer.init()

font1 = font.SysFont('Arial' ,80)
win = font1.render('ТЫ ПОБЕДИЛ', 1, (0,255,0))
lose = font1.render('ТЫ ПРОИГРАЛ(', 1, (255,0,0))


speed = 5
lost = 0
score = 0
goal = 10
max_lost = 5
fire_sound = mixer.Sound('fire.ogg')


display.set_caption('рембо')

class GameSprite(sprite.Sprite):
    def __init__ (self, player_img, player_x, player_y,width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600 - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top,15,20,15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > 400:
            self.rect.x = randint(80, 600 - 80)
            self.rect.y = 0
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= randint(5,10)
        if self.rect.y<0:
            self.kill()

font2 = font.SysFont('Arial', 26)

img_bullet = 'bullet.png'
img_enemy = 'ufo.png'
img_hero = 'rocket.png'

ship = Hero(img_hero, 5, 400 - 100, 80, 100, 10)




monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, randint(80, 600 - 80), -40, 80, 50, 2)
    monsters.add(monster)
#создай 2 спрайта и размести их на сцене

background = transform.scale(image.load('galaxy.jpg'),(600,400))
# sprite1 = Hero('rocket.png',40,350,10,)
# sprite2 = Enemy('asteroid.png',500,250,10)

game = True
finish = False

bullets = sprite.Group()



while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()


    

    if not finish:
        window.blit(background,(0,0))


        ship.update()
        monsters.update()
        bullets.update()


        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        collide = sprite.groupcollide(monsters,bullets,True,True)
        for c in collide:
            score = score +1
            monster = Enemy(img_enemy, randint(80, 600 - 80), -40, 80, 50, randint(1,3))
            monsters.add(monster)
    
        if lost >= 1:
            finish = True
            window.blit(lose,(100,100))
    
        if score >= goal:
            finish = True
            window.blit(win,(100,100))

        text = font2.render("Пропущено:" + str(lost), 1 ,(255,255,255))
        window.blit(text,(10,50))

        scored = font2.render("Счет:" + str(score),1, (255,255,255))
        window.blit(scored,(10,10))


        
    
        display.update()
    clock.tick(FPS)