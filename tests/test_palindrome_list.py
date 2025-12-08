import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import palindrome_list

def test_palindrome_list_caminho_lista_vazia():
    result = palindrome_list([])
    assert result == []

def test_palindrome_list_caminho_lista_com_palindromos():
    result = palindrome_list(["madam", "hello", "dad"])
    assert result == ["madam", "dad"]

def test_palindrome_list_caminho_lista_sem_palindromos():
    result = palindrome_list(["hello", "world", "python"])
    assert result == []

def test_palindrome_list_caminho_lista_com_um_unico_elemento_palindromo():
    result = palindrome_list(["madam"])
    assert result == ["madam"]

def test_palindrome_list_caminho_lista_com_um_unico_elemento_nao_palindromo():
    result = palindrome_list(["hello"])
    assert result == []

def test_palindrome_list_caminho_lista_com_muitos_elementos_misturados():
    result = palindrome_list(["madam", "hello", "dad", "python", "level"])
    assert result == ["madam", "dad", "level"]