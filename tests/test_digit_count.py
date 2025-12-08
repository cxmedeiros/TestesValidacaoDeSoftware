import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import digit_count

def test_digit_count_zero():
    result = digit_count(0)
    assert result == 1

def test_digit_count_nao_zero():
    result = digit_count(123)
    assert result == 3

def test_digit_count_negativo():
    result = digit_count(-456)
    assert result == 3

def test_digit_count_um_digito():
    result = digit_count(5)
    assert result == 1

def test_digit_count_tipo_invalido():
    try:
        digit_count("abc")
        assert False, "Expected TypeError or ValueError"
    except (TypeError, ValueError):
        assert True