from galinha import Galinha
from carros import Carro
from telas import Tela
import pygame as pg
from random import randint


def galinhabater():
    global vidas,galinha, carro_1, carro_2, carro_3, carro_4

    if galinha.rect.colliderect(carro_1) or galinha.rect.colliderect(carro_2) or galinha.rect.colliderect(carro_3) or \
            galinha.rect.colliderect(carro_4):
        galinha.x = 0
        vidas -= 1
        print(vidas)
        if vidas <= 0:
            tela.image = tela.imagem2
            tela.x = ALTURA/2
            tela.y = LARGURA/2
            galinha.kill()
            carros_group.empty()
            vidas = 0


def mudarLevel():
    global galinha, carro_1, carro_2, carro_3, carro_4

    if galinha.x >= LARGURA:
        carro_1 = Carro(1, 2, 1)
        carro_2 = Carro(2, 2, 1)
        carro_3 = Carro(3, 2, 1)
        carro_4 = Carro(4, 2, 1)
        galinha_group.add(galinha)
        carros_group.empty()
        carros_group.add(carro_1, carro_2, carro_3, carro_4)
        print("opa meu rei")
        tela.image = tela.imagem3
        tela_group.add(tela)
        galinha.x = 0
        if tela.image == tela.imagem3:
            if galinha.x >= LARGURA:
                print("ganhou")


def teclaSecreta():
    galinha.x = LARGURA + 150


LARGURA = 600
ALTURA = 850

pg.init()

tela_jogo = pg.display.set_mode((ALTURA, LARGURA))

pg.display.set_caption("ATRAVESSE")

clock = pg.time.Clock()

vidas = 6
tela = Tela()
tela_group = pg.sprite.Group()
tela_group.add(tela)

galinha = Galinha()
galinha_group = pg.sprite.Group()
galinha_group.add(galinha)

carro_1 = Carro(1, 1, 1)
carro_2 = Carro(2, 1, 1)
carro_3 = Carro(3, 1, 1)
carro_4 = Carro(4, 1, 1)

carros = [carro_1, carro_2, carro_3, carro_4]


carros_group = pg.sprite.Group()
carros_group.add(carro_1, carro_2, carro_3, carro_4)

while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_b:
                teclaSecreta()

    tela_group.draw(tela_jogo)
    galinha_group.draw(tela_jogo)
    carros_group.draw(tela_jogo)

    galinhabater()

    tela_group.update()
    mudarLevel()
    galinha_group.update()
    carros_group.update()
    pg.display.update()


pg.quit()