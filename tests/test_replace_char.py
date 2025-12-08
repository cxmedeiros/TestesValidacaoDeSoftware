import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import replace_char

def test_replace_char_substituicao_simples():
    result = replace_char("hello", "l", "x")
    assert result == "hexxo"

def test_replace_char_sem_substituicao():
    result = replace_char("hello", "z", "x")
    assert result == "hello"

def test_replace_char_string_vazia():
    result = replace_char("", "a", "b")
    assert result == ""

def test_replace_char_old_equals_new():
    result = replace_char("aaa", "a", "a")
    assert result == "aaa"

def test_replace_char_caractere_unico():
    result = replace_char("a", "a", "b")
    assert result == "b"

def test_replace_char_old_nao_existe():
    result = replace_char("abc", "d", "e")
    assert result == "abc"

def test_replace_char_todos_caracteres_substituidos():
    result = replace_char("aaa", "a", "b")
    assert result == "bbb"