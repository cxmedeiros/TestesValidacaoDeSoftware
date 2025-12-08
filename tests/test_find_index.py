import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_index

def test_find_index_valor_encontrado():
    result = find_index([1, 2, 3, 4, 5], 3)
    assert result == 2

def test_find_index_valor_nao_encontrado():
    result = find_index([1, 2, 3, 4, 5], 6)
    assert result == -1

def test_find_index_lista_vazia():
    result = find_index([], 3)
    assert result == -1

def test_find_index_primeiro_elemento():
    result = find_index([1, 2, 3, 4, 5], 1)
    assert result == 0

def test_find_index_ultimo_elemento():
    result = find_index([1, 2, 3, 4, 5], 5)
    assert result == 4