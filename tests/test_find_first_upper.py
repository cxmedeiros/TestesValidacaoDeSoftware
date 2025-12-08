import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_first_upper

def test_find_first_upper_encontra_maiusculo_no_inicio():
    result = find_first_upper("Abc")
    assert result == "A"

def test_find_first_upper_encontra_maiusculo_no_meio():
    result = find_first_upper("aBc")
    assert result == "B"

def test_find_first_upper_encontra_maiusculo_no_fim():
    result = find_first_upper("abC")
    assert result == "C"

def test_find_first_upper_nao_encontra_maiusculo():
    result = find_first_upper("abc")
    assert result is None

def test_find_first_upper_string_vazia():
    result = find_first_upper("")
    assert result is None

def test_find_first_upper_um_caractere_maiusculo():
    result = find_first_upper("A")
    assert result == "A"

def test_find_first_upper_um_caractere_minusculo():
    result = find_first_upper("a")
    assert result is None