import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import gcd

def test_gcd_caminho_b_igual_zero():
    result = gcd(10, 0)
    assert result == 10

def test_gcd_caminho_b_nao_igual_zero():
    result = gcd(48, 18)
    assert result == 6