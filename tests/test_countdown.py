import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import countdown

def test_countdown_caminho_n_menor_igual_zero():
    result = countdown(0)
    assert result == [0]

def test_countdown_caminho_n_maior_zero():
    result = countdown(3)
    assert result == [3, 2, 1, 0]

def test_countdown_caminho_n_negativo():
    result = countdown(-1)
    assert result == [0]