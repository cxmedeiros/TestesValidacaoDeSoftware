import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import contains

def test_contains_retorna_true_quando_valor_existe_na_lista():
    result = contains([1, 2, 3], 2)
    assert result == True

def test_contains_retorna_false_quando_valor_nao_existe_na_lista():
    result = contains([1, 2, 3], 4)
    assert result == False