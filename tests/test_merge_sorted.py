import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import merge_sorted

def test_merge_sorted_listas_ordenadas_iguais_tamanho():
    a = [1, 3, 5]
    b = [2, 4, 6]
    result = merge_sorted(a, b)
    assert result == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_listas_ordenadas_diferentes_tamanhos():
    a = [1, 3, 5, 7]
    b = [2, 4, 6]
    result = merge_sorted(a, b)
    assert result == [1, 2, 3, 4, 5, 6, 7]

def test_merge_sorted_primeira_lista_vazia():
    a = []
    b = [2, 4, 6]
    result = merge_sorted(a, b)
    assert result == [2, 4, 6]

def test_merge_sorted_segunda_lista_vazia():
    a = [1, 3, 5]
    b = []
    result = merge_sorted(a, b)
    assert result == [1, 3, 5]

def test_merge_sorted_ambas_listas_vazias():
    a = []
    b = []
    result = merge_sorted(a, b)
    assert result == []

def test_merge_sorted_listas_com_um_elemento():
    a = [1]
    b = [2]
    result = merge_sorted(a, b)
    assert result == [1, 2]

def test_merge_sorted_listas_com_elementos_iguais():
    a = [1, 1, 1]
    b = [1, 1, 1]
    result = merge_sorted(a, b)
    assert result == [1, 1, 1, 1, 1, 1]
