import utils
from utils import *
import pygame as pg


def jogo():
    pg.init()

    clock = pg.time.Clock()
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    utils.teclaSecreta()

        utils.tela_group.draw(utils.tela_jogo)
        utils.galinha_group.draw(utils.tela_jogo)
        utils.carros_group.draw(utils.tela_jogo)

        utils.tela_group.update()

        utils.galinha_group.update()
        utils.mudarLevel()
        utils.galinhabater()
        #utils.animacao_move()
        utils.carros_group.update()
        utils.vitoria()
        pg.display.update()


if __name__ == "__main__":
    utils.menu()
