import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import filter_odd

def test_filter_odd_lista_com_elementos_impares():
    result = filter_odd([1, 2, 3, 4, 5])
    assert result == [1, 3, 5]

def test_filter_odd_lista_vazia():
    result = filter_odd([])
    assert result == []