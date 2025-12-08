import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import decrypt_caesar

def test_decrypt_caesar_string_vazia():
    result = decrypt_caesar("", 3)
    assert result == ""

def test_decrypt_caesar_shift_zero():
    result = decrypt_caesar("abc", 0)
    assert result == "abc"

def test_decrypt_caesar_shift_negativo():
    result = decrypt_caesar("abc", -1)
    assert result == "bcd"

def test_decrypt_caesar_caracteres_minusculos():
    result = decrypt_caesar("abc", 1)
    assert result == "zab"

def test_decrypt_caesar_caracteres_maiusculos():
    result = decrypt_caesar("ABC", 1)
    assert result == "ZAB"

def test_decrypt_caesar_caracteres_especiais():
    result = decrypt_caesar("!@#", 1)
    assert result == "!@#"

def test_decrypt_caesar_caracteres_mistos():
    result = decrypt_caesar("aBc!@#", 1)
    assert result == "zAb!@#"

def test_decrypt_caesar_shift_maior_que_alfabeto():
    result = decrypt_caesar("abc", 27)
    assert result == "zab"