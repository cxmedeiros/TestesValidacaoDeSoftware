import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import fibonacci

def test_fibonacci_caminho_n_menor_que_zero():
    result = fibonacci(-1)
    assert result is None

def test_fibonacci_caminho_n_menor_ou_igual_a_um():
    result1 = fibonacci(0)
    result2 = fibonacci(1)
    assert result1 == 0
    assert result2 == 1

def test_fibonacci_caminho_n_maior_que_um():
    result = fibonacci(3)
    assert result == 2  # fibonacci(2) + fibonacci(1) = 1 + 1 = 2