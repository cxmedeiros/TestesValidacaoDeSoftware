import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import divide_safe

def test_divide_safe_divisao_valida():
    result = divide_safe(10, 2)
    assert result == 5

def test_divide_safe_divisao_por_zero():
    result = divide_safe(10, 0)
    assert result is None

def test_divide_safe_tipo_invalido():
    result = divide_safe(10, 'a')
    assert result is None