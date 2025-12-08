import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import parity

def test_parity_par():
    result = parity(4)
    assert result == 'par'

def test_parity_impar():
    result = parity(3)
    assert result == 'ímpar'