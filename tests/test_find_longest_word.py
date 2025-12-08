import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_longest_word

def test_find_longest_word_caminho_lista_vazia():
    result = find_longest_word([])
    assert result is None

def test_find_longest_word_caminho_lista_nao_vazia():
    result = find_longest_word(["a", "bb", "ccc"])
    assert result == "ccc"

def test_find_longest_word_caminho_lista_com_um_elemento():
    result = find_longest_word(["hello"])
    assert result == "hello"

def test_find_longest_word_caminho_lista_com_palavras_iguais():
    result = find_longest_word(["aaa", "bbb", "ccc"])
    assert result == "aaa"  # or "bbb" or "ccc" depending on implementation

def test_find_longest_word_caminho_lista_com_palavras_vazias():
    result = find_longest_word(["", "a", "bb"])
    assert result == "bb"