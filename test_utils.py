from utils import *

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
