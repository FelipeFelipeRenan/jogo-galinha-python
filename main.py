from galinha import Galinha
from carros import Carro
from telas import Tela
import pygame as pg
from random import randint


def galinhabater():
    global vidas
    global galinha

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
    global galinha
    if galinha.x >= LARGURA:
        print("opa meu rei")


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

carro_1 = Carro(1)
carro_2 = Carro(2)
carro_3 = Carro(3)
carro_4 = Carro(4)

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

    mudarLevel()
    galinhabater()

    tela_group.update()
    galinha_group.update()
    carros_group.update()
    pg.display.update()

pg.quit()