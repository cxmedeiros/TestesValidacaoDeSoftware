import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_list


def test_sum_list_lista_vazia():
    result = sum_list([])
    assert result == 0



def test_sum_list_elementos_positivos():
    result = sum_list([1, 2, 3, 4, 5])
    assert result == 15


def test_sum_list_elementos_negativos():
    result = sum_list([-1, -2, -3, -4, -5])
    assert result == -15



def test_sum_list_elementos_mistos():
    result = sum_list([-1, 2, -3, 4, -5])
    assert result == -3



def test_sum_list_um_elemento():
    result = sum_list([5])
    assert result == 5

