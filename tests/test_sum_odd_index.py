import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_odd_index

def test_sum_odd_index_lista_com_elementos():
    result = sum_odd_index([1, 2, 3, 4, 5])
    assert result == 6

def test_sum_odd_index_lista_vazia():
    result = sum_odd_index([])
    assert result == 0