import pygame as pg


class Galinha(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.clock = pg.time.Clock()
        self.x = 50
        self.y = 700/2
        self.velo = 4
        self.width = 60
        self.height = 60
        self.moveseq = []
        self.movdir = []
        self.idle = []

        self.right = pg.image.load("images/DW1.png")
        self.left = pg.image.load("images/EW1.png")
        self.cococo = pg.image.load("images/DI1.png")
        self.cococo2 = pg.image.load("images/DI3.png")

        self.right = pg.transform.scale(self.right, (self.width, self.height))
        self.left = pg.transform.scale(self.left, (self.width, self.height))
        self.cococo = pg.transform.scale(self.cococo, (self.width, self.height))
        self.cococo2 = pg.transform.scale(self.cococo2, (self.width, self.height))

        # lista de animaçoes para esquerda
        self.moveseq.append(self.left)
        self.moveseq.append(self.left)
        self.moveseq.append(self.left)
        self.moveseq.append(self.left)
        self.moveseq.append(self.left)
        self.moveseq.append(self.cococo)
        self.moveseq.append(self.cococo)
        self.moveseq.append(self.cococo)
        self.moveseq.append(self.cococo)
        self.moveseq.append(self.cococo)

        # lista de animaçoes para direita
        self.movdir.append(self.right)
        self.movdir.append(self.right)
        self.movdir.append(self.right)
        self.movdir.append(self.right)
        self.movdir.append(self.right)
        self.movdir.append(self.cococo)
        self.movdir.append(self.cococo)
        self.movdir.append(self.cococo)
        self.movdir.append(self.cococo)
        self.movdir.append(self.cococo)

        # lista de animaçoes parada
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)
        self.idle.append(self.cococo)

        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)
        self.idle.append(self.cococo2)


        self.index = 0

        self.image = self.cococo
        self.rect = self.image.get_rect()

    def update(self):
        self.moves()
        self.correcao()
        self.rect.center = (self.x, self.y)
        self.index += 1

        if self.index >= len(self.movdir):
            self.index = 0
        elif self.index >= len(self.moveseq):
            self.index = 0
        elif self.index >= len(self.idle):
            self.index = 0

        self.rect.center = (self.x, self.y)

    def moves(self):

        teclas = pg.key.get_pressed()

        if teclas[pg.K_LEFT] or teclas[pg.K_a]:
            self.x -= self.velo
            self.image = self.moveseq[self.index]

        elif teclas[pg.K_RIGHT] or teclas[pg.K_d]:
            self.x += self.velo
            self.image = self.movdir[self.index]

        elif teclas[pg.K_UP] or teclas[pg.K_w]:
            self.y -= self.velo

        elif teclas[pg.K_DOWN] or teclas[pg.K_s]:
            self.y += self.velo
        else:
            self.image = self.idle[self.index]


    def correcao(self):
        if self.x - self.width/2 < 0:
            self.x = self.width/2

        elif self.x + self.width/2 >= 800 + 200:
            self.x = 800 - self.width/2

        if self.y - self.height/2 < 0:
            self.y = self.height/2

        elif self.y + self.height/2 >= 600:
            self.y = 600 - self.height/2
