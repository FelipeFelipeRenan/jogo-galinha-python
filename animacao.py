import pygame as pg

class Animacao(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 700/2
        self.velo = 4
        self.width = 60
        self.height = 60
        self.images = []

        self.frame1 = pg.image.load('images/galinha/idle/idle_1.png')
        self.frame2 = pg.image.load('images/galinha/idle/idle_2.png')
        self.frame3 = pg.image.load('images/galinha/idle/idle_3.png')

        self.images.append(self.frame1)
        self.images.append(self.frame2)
        self.images.append(self.frame3)

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pg.Rect(3, 3, 10, 10)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.rect.center = (self.x, self.y)
