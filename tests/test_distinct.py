import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import distinct

def test_distinct_lista_vazia():
    result = distinct([])
    assert result == []

def test_distinct_lista_com_elementos_repetidos():
    result = distinct([1, 2, 2, 3, 4, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_distinct_lista_com_elementos_distintos():
    result = distinct([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_distinct_lista_com_um_unico_elemento():
    result = distinct([1])
    assert result == [1]

def test_distinct_lista_com_elementos_nao_numericos():
    result = distinct(['a', 'b', 'b', 'c'])
    assert result == ['a', 'b', 'c']

def test_distinct_lista_com_mistura_de_tipos():
    result = distinct([1, 'a', 'a', 2, 'b', 'b'])
    assert result == [1, 'a', 2, 'b']