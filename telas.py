import pygame as pg


class Tela(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem1 = pg.image.load("rua-teste.jpg")
        self.imagem2 = pg.image.load("gameover.jpg")
        self.imagem3 = pg.image.load("nivel2.png")

        self.imagem1 = pg.transform.scale(self.imagem1, (850, 600))
        self.imagem2 = pg.transform.scale(self.imagem2, (200, 200))
        self.imagem3 = pg.transform.scale(self.imagem3, (850, 600))

        self.image = self.imagem1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)
