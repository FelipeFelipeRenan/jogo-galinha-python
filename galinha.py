import pygame as pg


class Galinha(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 800/2
        self.velo = 4
        self.width = 100
        self.height = 50

        # Imagem do ser de asas bicudo aqui #
        self.cococo = pg.image.load("galinha2.png")

        self.cococo = pg.transform.scale(self.cococo, (self.width, self.height))

        self.image = self.cococo

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.moves()
        self.correcao()
        self.rect.center = (self.x, self.y)

    def moves(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT] or teclas[pg.K_a]:
            self.x -= self.velo

        if teclas[pg.K_RIGHT] or teclas[pg.K_d]:
            self.x += self.velo

        if teclas[pg.K_UP] or teclas[pg.K_w]:
            self.y -= self.velo

        if teclas[pg.K_DOWN] or teclas[pg.K_s]:
            self.y += self.velo

    def correcao(self):
        if self.x - self.width/2 < 0:
            self.x = self.width/2

        elif self.x + self.width/2 >= 800 + 200:
            self.x = 800 - self.width/2

        if self.y - self.height/2 < 0:
            self.y = self.height/2

        elif self.y + self.height/2 >= 600:
            self.y = 600 - self.height/2
