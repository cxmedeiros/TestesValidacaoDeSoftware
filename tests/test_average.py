import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import average

def test_average_lista_vazia():
    result = average([])
    assert result is None

def test_average_lista_nao_vazia():
    result = average([1, 2, 3])
    assert result == 2

def test_average_lista_com_um_elemento():
    result = average([5])
    assert result == 5

def test_average_lista_com_valores_negativos():
    result = average([-1, 0, 1])
    assert result == 0

def test_average_lista_com_valores_decimais():
    result = average([1.5, 2.5, 3.5])
    assert result == 2.5