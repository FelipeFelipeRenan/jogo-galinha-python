import pygame as pg

#tirar do repositorio as imagens n usadas
class Tela(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem1 = pg.image.load("images/bg1.png")
        self.imagem2 = pg.image.load("images/over.png")
        self.imagem3 = pg.image.load("images/bg2.png")
        self.imagem4 = pg.image.load("images/Tutorial.png")
        self.imagem5 = pg.image.load("images/bg0.png")

        self.imagem1 = pg.transform.scale(self.imagem1, (850, 600))
        self.imagem2 = pg.transform.scale(self.imagem2, (850, 600))
        self.imagem3 = pg.transform.scale(self.imagem3, (850, 600))
        self.imagem4 = pg.transform.scale(self.imagem4, (850, 600))
        self.imagem5 = pg.transform.scale(self.imagem5, (850, 600))

        self.image = self.imagem1

        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def setSize(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.rect.topleft = (self.x, self.y)
