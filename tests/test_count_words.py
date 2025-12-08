import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import count_words

def test_count_words_string_vazia():
    result = count_words("")
    assert result == 0

def test_count_words_string_com_espacos():
    result = count_words("   ")
    assert result == 0

def test_count_words_string_com_uma_palavra():
    result = count_words("palavra")
    assert result == 1

def test_count_words_string_com_multiplas_palavras():
    result = count_words("uma frase com várias palavras")
    assert result == 5

def test_count_words_string_com_espacos_no_inicio_e_fim():
    result = count_words("   uma frase com várias palavras   ")
    assert result == 5