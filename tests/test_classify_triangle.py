import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import classify_triangle

def test_classify_triangle_lado_menor_igual_zero():
    result = classify_triangle(-1, 3, 4)
    assert result == 'invalido'

def test_classify_triangle_soma_dois_lados_menor_terceiro():
    result = classify_triangle(1, 2, 4)
    assert result == 'invalido'

def test_classify_triangle_todos_lados_iguais():
    result = classify_triangle(3, 3, 3)
    assert result == 'equilatero'

def test_classify_triangle_dois_lados_iguais():
    result = classify_triangle(3, 3, 4)
    assert result == 'isosceles'

def test_classify_triangle_nenhum_lado_igual():
    result = classify_triangle(3, 4, 5)
    assert result == 'escaleno'