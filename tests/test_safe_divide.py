import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import safe_divide

def test_safe_divide_divisao_por_zero():
    result = safe_divide(10, 0)
    assert result is None

def test_safe_divide_divisao_valida():
    result = safe_divide(10, 2)
    assert result == 5