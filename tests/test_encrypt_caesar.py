import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import encrypt_caesar

def test_encrypt_caesar_caracteres_minusculos_shift_positivo():
    result = encrypt_caesar("abc", 1)
    assert result == "bcd"

def test_encrypt_caesar_caracteres_minusculos_shift_negativo():
    result = encrypt_caesar("abc", -1)
    assert result == "zab"

def test_encrypt_caesar_caracteres_fora_do_intervalo():
    result = encrypt_caesar("ABC123!@#", 1)
    assert result == "ABC123!@#"

def test_encrypt_caesar_string_vazia():
    result = encrypt_caesar("", 1)
    assert result == ""

def test_encrypt_caesar_shift_zero():
    result = encrypt_caesar("abc", 0)
    assert result == "abc"

def test_encrypt_caesar_shift_maior_que_26():
    result = encrypt_caesar("abc", 27)
    assert result == "bcd"

def test_encrypt_caesar_shift_menor_que_menos_26():
    result = encrypt_caesar("abc", -27)
    assert result == "zab"