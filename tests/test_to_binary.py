import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import to_binary

def test_to_binary_zero():
    result = to_binary(0)
    assert result == '0'

def test_to_binary_nao_zero():
    result = to_binary(5)
    assert result == '101'

def test_to_binary_tipo_invalido():
    try:
        to_binary("a")
    except Exception as e:
        assert isinstance(e, TypeError) or isinstance(e, ValueError)

def test_to_binary_valor_negativo():
    try:
        to_binary(-1)
    except Exception as e:
        assert isinstance(e, ValueError)