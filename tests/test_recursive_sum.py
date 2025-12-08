import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import recursive_sum

def test_recursive_sum_caminho_lista_vazia():
    result = recursive_sum([])
    assert result == 0

def test_recursive_sum_caminho_lista_nao_vazia():
    result = recursive_sum([1, 2, 3])
    assert result == 6

def test_recursive_sum_caminho_lista_com_valor_negativo():
    result = recursive_sum([1, -2, 3])
    assert result == 2

def test_recursive_sum_caminho_lista_com_um_unico_elemento():
    result = recursive_sum([5])
    assert result == 5

def test_recursive_sum_caminho_lista_com_zero():
    result = recursive_sum([0, 0, 0])
    assert result == 0