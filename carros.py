import pygame as pg

# imagens de carros no metodo pg.image.load("carroNovo.png")


class Carro(pg.sprite.Sprite):
    def __init__(self, quantidade, nivel):
        super().__init__()
        # normal
        if nivel == 1:
            if quantidade == 1:
                self.x = 250
                self.image = pg.image.load("carroNovo.png")
                self.velo = -4

            elif quantidade == 2:
                self.x = 350
                self.image = pg.image.load("carroNovo.png")
                self.velo = 5
            elif quantidade == 3:
                self.x = 450
                self.image = pg.image.load("carroNovo.png")
                self.velo = 3
            else:
                self.x = 580
                self.image = pg.image.load("carroNovo.png")
                self.velo = -2
        else:
            if quantidade == 1:
                self.x = 250
                self.image = pg.image.load("carroNovo.png")
                self.velo = -3

            elif quantidade == 2:
                self.x = 350
                self.image = pg.image.load("carroNovo.png")
                self.velo = 3
            elif quantidade == 3:
                self.x = 450
                self.image = pg.image.load("carroNovo.png")
                self.velo = 6
            else:
                self.x = 580
                self.image = pg.image.load("carroNovo.png")
                self.velo = -5
    # facil
        self.y = 650/2
        self.width = 100
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