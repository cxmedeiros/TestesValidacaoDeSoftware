import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import quicksort

def test_quicksort_caminho_lista_com_um_elemento():
    result = quicksort([5])
    assert result == [5]

def test_quicksort_caminho_lista_com_mais_de_um_elemento():
    result = quicksort([5, 2, 9, 1, 7])
    assert result == [1, 2, 5, 7, 9]

def test_quicksort_caminho_lista_vazia():
    result = quicksort([])
    assert result == []