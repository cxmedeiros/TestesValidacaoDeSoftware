import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import filter_even

def test_filter_even_lista_vazia():
    result = filter_even([])
    assert result == []

def test_filter_even_lista_com_numeros_pares_e_impares():
    result = filter_even([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]

def test_filter_even_lista_com_apenas_numeros_pares():
    result = filter_even([2, 4, 6, 8, 10])
    assert result == [2, 4, 6, 8, 10]

def test_filter_even_lista_com_apenas_numeros_impares():
    result = filter_even([1, 3, 5, 7, 9])
    assert result == []

def test_filter_even_lista_com_um_unico_elemento_par():
    result = filter_even([2])
    assert result == [2]

def test_filter_even_lista_com_um_unico_elemento_impar():
    result = filter_even([1])
    assert result == []

def test_filter_even_lista_com_zero():
    result = filter_even([0, 1, 2, 3, 4])
    assert result == [0, 2, 4]

def test_filter_even_lista_com_numeros_negativos():
    result = filter_even([-1, -2, -3, -4, -5, -6])
    assert result == [-2, -4, -6]