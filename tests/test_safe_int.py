import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import safe_int

def test_safe_int_conversao_bem_sucedida():
    result = safe_int("123")
    assert result == 123

def test_safe_int_value_error():
    result = safe_int("abc")
    assert result is None

def test_safe_int_type_error():
    result = safe_int([1, 2, 3])
    assert result is None