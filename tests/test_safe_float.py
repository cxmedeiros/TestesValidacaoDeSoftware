import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import safe_float

def test_safe_float_conversao_bem_sucedida():
    result = safe_float("10.5")
    assert result == 10.5

def test_safe_float_value_error():
    result = safe_float("abc")
    assert result is None

def test_safe_float_type_error():
    result = safe_float([1, 2, 3])
    assert result is None