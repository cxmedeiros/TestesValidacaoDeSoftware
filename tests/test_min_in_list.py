import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import min_in_list

def test_min_in_list_lista_vazia():
    result = min_in_list([])
    assert result is None

def test_min_in_list_lista_nao_vazia():
    result = min_in_list([5, 2, 9, 1, 7])
    assert result == 1

def test_min_in_list_lista_com_um_elemento():
    result = min_in_list([5])
    assert result == 5

def test_min_in_list_lista_com_valores_negativos():
    result = min_in_list([5, -2, 9, -1, 7])
    assert result == -2

def test_min_in_list_lista_com_todos_valores_iguais():
    result = min_in_list([5, 5, 5, 5])
    assert result == 5