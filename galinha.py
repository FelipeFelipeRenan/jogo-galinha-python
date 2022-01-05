import pygame as pg

class Galinha(pg.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.clock = pg.time.Clock()
        self.x = 50
        self.y = 700/2
        self.velo = 5
        self.width = 60
        self.height = 60

        self.walk_right = False
        self.right = []
        self.right.append(pg.image.load('images/galinha/walk/Walk_1.png'))
        self.right.append(pg.image.load('images/galinha/walk/Walk_2.png'))
        self.right.append(pg.image.load('images/galinha/walk/Walk_3.png'))
        self.right.append(pg.image.load('images/galinha/walk/Walk_4.png'))
        self.right.append(pg.image.load('images/galinha/walk/Walk_5.png'))
        self.right.append(pg.image.load('images/galinha/walk/Walk_6.png'))

        self.walk_left = False
        self.left = []
        self.left.append(pg.image.load('images/galinha/walk/Walk_7.png'))
        self.left.append(pg.image.load('images/galinha/walk/Walk_8.png'))
        self.left.append(pg.image.load('images/galinha/walk/Walk_9.png'))
        self.left.append(pg.image.load('images/galinha/walk/Walk_10.png'))
        self.left.append(pg.image.load('images/galinha/walk/Walk_11.png'))
        self.left.append(pg.image.load('images/galinha/walk/Walk_12.png'))

        self.walk_idle = False
        self.idle = []
        self.idle.append(pg.image.load('images/galinha/idle/idle_1.png'))
        self.idle.append(pg.image.load('images/galinha/idle/idle_2.png'))
        self.idle.append(pg.image.load('images/galinha/idle/idle_3.png'))

        self.index = 0
        self.image = self.idle[self.index]

        self.rect = self.image.get_rect()


    def update(self):

        self.moves()
        self.correcao()
        self.rect.center = (self.x, self.y)

    def walkRight(self):

        if self.walk_right == True:
            self.index += 0.35
            if int(self.index) >= len(self.right):
                self.index = 0
                self.walk_right = False

        self.image = self.right[int(self.index)]

    def walkLeft(self):

        if self.walk_left == True:
            self.index += 0.35
            if int(self.index) >= len(self.left):
                self.index = 0
                self.walk_left = False
        self.image = self.left[int(self.index)]


    def status_idle(self):
        if self.walk_idle == True:
            self.index += 0.10
            if int(self.index) >= len(self.idle):
                self.index = 0
                self.walk_idle = False
        self.image = self.idle[int(self.index)]

    def moves(self):

        teclas = pg.key.get_pressed()

        if teclas[pg.K_LEFT] or teclas[pg.K_a]:
            self.x -= self.velo
            self.walk_right = False
            self.walk_left = True
            self.walkLeft()

        elif teclas[pg.K_RIGHT] or teclas[pg.K_d]:
            self.x += self.velo
            self.walk_left = False
            self.walk_right = True
            self.walkRight()

        elif teclas[pg.K_UP] or teclas[pg.K_w]:
            self.y -= self.velo

            self.walk_idle = True
            self.status_idle()

        elif teclas[pg.K_DOWN] or teclas[pg.K_s]:
            self.y += self.velo

            self.walk_idle = True
            self.status_idle()

        else:
            self.walk_left = False
            self.walk_right = False
            self.walk_idle = True
            self.status_idle()


    def correcao(self):
        if self.x - self.width/2 < 0:
            self.x = self.width/2

        elif self.x + self.width/2 >= 800 + 200:
            self.x = 800 - self.width/2

        if self.y - self.height/2 < 0:
            self.y = self.height/2

        elif self.y + self.height/2 >= 600:
            self.y = 600 - self.height/2