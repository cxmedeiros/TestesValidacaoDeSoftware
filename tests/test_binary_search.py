import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import binary_search

def test_binary_search_lista_vazia_retorna_none():
    result = binary_search([], 5)
    assert result is None

def test_binary_search_encontra_elemento_no_meio():
    lst = [1, 2, 3, 4, 5]
    result = binary_search(lst, 3)
    assert result == 2

def test_binary_search_elemento_menor_que_meio():
    lst = [1, 2, 3, 4, 5]
    result = binary_search(lst, 2)
    assert result == 1

def test_binary_search_elemento_maior_que_meio():
    lst = [1, 2, 3, 4, 5]
    result = binary_search(lst, 4)
    assert result == 3

def test_binary_search_elemento_nao_encontrado():
    lst = [1, 2, 3, 4, 5]
    result = binary_search(lst, 6)
    assert result is None