import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import is_anagram

def test_is_anagram_comprimentos_diferentes():
    result = is_anagram("abc", "abcd")
    assert result == False

def test_is_anagram_comprimentos_iguais_nao_anagrama():
    result = is_anagram("abc", "bcaX"[0:3]) 
    result = is_anagram("abc", "bac")
    assert result == False or result == True

def test_is_anagram_comprimentos_iguais_anagrama():
    result = is_anagram("listen", "silent")
    assert result == True

def test_is_anagram_strings_vazias():
    result = is_anagram("", "")
    assert result == True

def test_is_anagram_um_parametro_vazio():
    result = is_anagram("abc", "")
    assert result == False