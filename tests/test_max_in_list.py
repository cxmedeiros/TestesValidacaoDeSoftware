import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import max_in_list

def test_max_in_list_lista_vazia():
    result = max_in_list([])
    assert result is None

def test_max_in_list_lista_nao_vazia():
    result = max_in_list([3, 1, 4, 1, 5, 9, 2])
    assert result == 9

def test_max_in_list_lista_com_um_elemento():
    result = max_in_list([5])
    assert result == 5

def test_max_in_list_lista_com_valores_negativos():
    result = max_in_list([-1, -5, -3])
    assert result == -1

def test_max_in_list_lista_com_valores_repetidos():
    result = max_in_list([2, 2, 2, 2])
    assert result == 2