import pygame as pg

class Carro(pg.sprite.Sprite):
    def __init__(self, quantidade, nivel):
        super().__init__()

        if nivel == 1:
            if quantidade == 1:
                self.x = 290
                self.image = pg.image.load("carroNovo.png")
                self.velo = -1

            elif quantidade == 2:
                self.x = 375
                self.image = pg.image.load("carroNovo.png")
                self.velo = -2
            elif quantidade == 3:
                self.x = 575
                self.image = pg.image.load("carroNovo.png")
                self.velo = -3
            else:
                self.x = 660
                self.image = pg.image.load("carroNovo.png")
                self.velo = -2
        else:
            if quantidade == 1:
                self.x = 290
                self.image = pg.image.load("carroNovo.png")
                self.velo = -2

            elif quantidade == 2:
                self.x = 370
                self.image = pg.image.load("carroNovo.png")
                self.velo = -3
            elif quantidade == 3:
                self.x = 575
                self.image = pg.image.load("carroNovo.png")
                self.velo = -5
            else:
                self.x = 660
                self.image = pg.image.load("carroNovo.png")
                self.velo = -3

        self.y = 650/2
        self.width = 140
        self.height = 150
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.moves()
        self.rect.center = (self.x, self.y)

    def moves(self):
        self.y += self.velo

        if self.y < -8:
            self.y = 700
            self.velo *= -1

        elif self.y + self.height/2 > 750:
            self.y = 650 - self.height/2
            self.velo *= -1