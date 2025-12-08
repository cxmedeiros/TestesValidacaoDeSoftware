import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import title_case

### Testes para Cobertura Máxima

def test_title_case_string_com_varias_palavras():
    result = title_case("hello world")
    assert result == "Hello World"

def test_title_case_string_com_uma_palavra():
    result = title_case("hello")
    assert result == "Hello"

def test_title_case_string_vazia():
    result = title_case("")
    assert result == ""

def test_title_case_none():
    try:
        title_case(None)
        assert False, "Esperado uma exceção"
    except Exception as e:
        assert True

def test_title_case_nao_string():
    try:
        title_case(123)
        assert False, "Esperado uma exceção"
    except Exception as e:
        assert True

