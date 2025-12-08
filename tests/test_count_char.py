import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import count_char


### Testes para o Caminho de Execução 1
def test_count_char_string_nao_vazia_com_char_presente():
    result = count_char("hello", 'l')
    assert result == 2

def test_count_char_string_nao_vazia_sem_char():
    result = count_char("hello", 'x')
    assert result == 0

def test_count_char_string_vazia():
    result = count_char("", 'x')
    assert result == 0

### Edge Cases
def test_count_char_char_vazio():
    result = count_char("hello", '')
    assert result == 0

def test_count_char_s_nao_string():
    try:
        count_char(123, 'x')
    except Exception as e:
        assert isinstance(e, TypeError) or isinstance(e, AttributeError)

def test_count_char_char_nao_char():
    try:
        count_char("hello", 'ab')
    except Exception as e:
        assert isinstance(e, TypeError)

