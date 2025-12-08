import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import bubble_sort

def test_bubble_sort_lista_desordenada():
    result = bubble_sort([5, 3, 8, 4, 2])
    assert result == [2, 3, 4, 5, 8]

def test_bubble_sort_lista_ordenada():
    result = bubble_sort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_bubble_sort_lista_vazia():
    result = bubble_sort([])
    assert result == []

def test_bubble_sort_lista_com_um_elemento():
    result = bubble_sort([5])
    assert result == [5]

def test_bubble_sort_lista_com_elementos_repetidos():
    result = bubble_sort([5, 2, 8, 2, 1])
    assert result == [1, 2, 2, 5, 8]

def test_bubble_sort_lista_com_negativos():
    result = bubble_sort([5, -3, 8, -4, 2])
    assert result == [-4, -3, 2, 5, 8]