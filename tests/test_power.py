import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import power

def test_power_exp_menor_que_zero():
    result = power(2, -1)
    assert result is None

def test_power_exp_igual_a_zero():
    result = power(2, 0)
    assert result == 1

def test_power_exp_igual_a_um():
    result = power(2, 1)
    assert result == 2

def test_power_exp_maior_que_um():
    result = power(2, 3)
    assert result == 8