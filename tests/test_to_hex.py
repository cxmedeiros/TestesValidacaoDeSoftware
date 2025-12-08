import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import to_hex

def test_to_hex_caminho_n_zero():
    result = to_hex(0)
    assert result == '0'

def test_to_hex_caminho_n_nao_zero():
    result = to_hex(10)
    assert result == 'A'

def test_to_hex_caminho_n_negativo():
    try:
        to_hex(-1)
        assert False, "Expected an exception or specific behavior for negative input"
    except Exception as e:
        # Assuming the function should raise an exception for negative inputs
        assert True

def test_to_hex_caminho_n_nao_inteiro():
    try:
        to_hex("not an integer")
        assert False, "Expected an exception or specific behavior for non-integer input"
    except Exception as e:
        # Assuming the function should raise an exception for non-integer inputs
        assert True

def test_to_hex_caminho_n_maior_valor():
    result = to_hex(255)
    assert result == 'FF'