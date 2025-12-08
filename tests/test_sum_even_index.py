import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_even_index

def test_sum_even_index_lista_vazia():
    result = sum_even_index([])
    assert result == 0

def test_sum_even_index_lista_com_um_elemento():
    result = sum_even_index([1])
    assert result == 1

def test_sum_even_index_lista_com_indices_pares_somados():
    result = sum_even_index([1, 2, 3, 4, 5])
    assert result == 9

def test_sum_even_index_lista_com_todos_elementos_negativos():
    result = sum_even_index([-1, -2, -3, -4, -5])
    assert result == -9

def test_sum_even_index_lista_com_elementos_nao_numericos():
    try:
        sum_even_index([1, 'a', 3, 4, 5])
        assert False, "Expected TypeError or ValueError"
    except (TypeError, ValueError):
        assert True

def test_sum_even_index_lista_com_elementos_nulos():
    try:
        sum_even_index([1, None, 3, 4, 5])
        assert False, "Expected TypeError or ValueError"
    except (TypeError, ValueError):
        assert True