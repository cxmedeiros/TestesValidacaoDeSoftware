import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import lcm

def test_lcm_caminho_zero_a():
    result = lcm(0, 5)
    assert result == 0

def test_lcm_caminho_zero_b():
    result = lcm(5, 0)
    assert result == 0

def test_lcm_caminho_a_menor_que_b():
    result = lcm(2, 3)
    assert result == 6

def test_lcm_caminho_a_nao_menor_que_b():
    result = lcm(3, 2)
    assert result == 6