import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import list_depth

def test_list_depth_nao_e_lista():
    result = list_depth("not a list")
    assert result == 0

def test_list_depth_lista_vazia():
    result = list_depth([])
    assert result == 1

def test_list_depth_lista_nao_vazia_sem_listas_internas():
    result = list_depth([1, 2, 3])
    assert result == 1

def test_list_depth_lista_com_lista_interna():
    result = list_depth([1, [2], 3])
    assert result == 2

def test_list_depth_lista_com_listas_aninhadas():
    result = list_depth([1, [2, [3]], 4])
    assert result == 3