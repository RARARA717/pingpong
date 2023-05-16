from pygame import *






back = transform.scale(image.load('green.jpg'), (600,400))
window = display.set_mode((600,400))


speed = 5
clock = time.Clock()
FPS = 60
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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400 - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400 - 80:
            self.rect.y += self.speed

img_ball = 'ball.png'
img_line = 'line.png'

line_r = Hero(img_line, 5, 200, 100,100, 5)
line_l = Hero(img_line, 500, 200, 100, 100 ,5)
ball = GameSprite(img_ball, 300,200, 40,40,5)




game = False

while not game:
    for e in event.get():
        if e.type == QUIT:
            game = True


    window.blit(back, (0,0))
    line_r.update_l()
    line_l.update_r()
    ball.update()

    line_r.reset()
    line_l.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)



