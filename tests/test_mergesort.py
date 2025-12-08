import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import mergesort

def test_mergesort_caminho_lista_vazia():
    result = mergesort([])
    assert result == []

def test_mergesort_caminho_lista_unitaria():
    result = mergesort([5])
    assert result == [5]

def test_mergesort_caminho_lista_ordenada():
    result = mergesort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_mergesort_caminho_lista_desordenada():
    result = mergesort([5, 3, 8, 4, 2])
    assert result == [2, 3, 4, 5, 8]

def test_mergesort_caminho_lista_com_elementos_repetidos():
    result = mergesort([4, 2, 7, 1, 3, 3, 7])
    assert result == [1, 2, 3, 3, 4, 7, 7]