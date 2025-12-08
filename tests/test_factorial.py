import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import factorial

def test_factorial_caminho_n_menor_que_zero():
    result = factorial(-1)
    assert result is None

def test_factorial_caminho_n_zero():
    result = factorial(0)
    assert result == 1

def test_factorial_caminho_n_positivo():
    result = factorial(5)
    assert result == 120

def test_factorial_caminho_n_um():
    result = factorial(1)
    assert result == 1