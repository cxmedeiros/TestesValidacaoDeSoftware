import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import product_list

def test_product_list_lista_vazia():
    result = product_list([])
    assert result == 1

def test_product_list_lista_com_um_elemento():
    result = product_list([5])
    assert result == 5

def test_product_list_lista_com_multiplos_elementos():
    result = product_list([1, 2, 3, 4])
    assert result == 24

def test_product_list_lista_com_zero():
    result = product_list([1, 0, 3, 4])
    assert result == 0

def test_product_list_lista_com_valores_negativos():
    result = product_list([-1, 2, -3, 4])
    assert result == 24
def test_product_list_lista_com_valores_reais():
    result = product_list([1.5, 2, 3, 4])
    assert result == 36.0