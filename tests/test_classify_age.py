import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import classify_age

def test_classify_age_idade_negativa():
    result = classify_age(-1)
    assert result == 'inválido'

def test_classify_age_menor_de_idade():
    result = classify_age(17)
    assert result == 'menor'

def test_classify_age_adulto():
    result = classify_age(30)
    assert result == 'adulto'

def test_classify_age_idoso():
    result = classify_age(65)
    assert result == 'idoso'

def test_classify_age_limite_inferior_valido():
    result = classify_age(0)
    assert result == 'menor'

def test_classify_age_limite_superior_adulto():
    result = classify_age(64)
    assert result == 'adulto'