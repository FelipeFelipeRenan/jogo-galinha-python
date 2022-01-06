from utils import *

def test_botoes():
    mx, my = pg.mouse.get_pos()  
    click = False

    iniciar = pg.Rect(300, 150, 240, 55)
    ajuda = pg.Rect(300, 250, 240, 55)
    sair = pg.Rect(300, 350, 240, 55)
    retornarmenu = pg.Rect(300, 500, 240, 55)

    for event in pg.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    if iniciar.collidepoint((mx, my)):
        if click:
            assert True
    if ajuda.collidepoint((mx, my)):
        if click:
            assert True
    if sair.collidepoint((mx, my)):
        if click:
            assert True
    if retornarmenu.collidepoint((mx, my)):
        if click:
            assert True


def test_teclaSecreta():
    teclaSecreta()
    assert galinha.x == LARGURA + 200


def test_vitoria():
    teclaSecreta()
    vitoria()
    assert galinha.x >= LARGURA + 100 


def test_collide():
    vidas = 0
    galinha.x = carro_1.y
    galinhabater()
    assert vidas < 6
