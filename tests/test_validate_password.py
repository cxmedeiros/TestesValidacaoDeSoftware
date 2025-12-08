import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import validate_password

def test_validate_password_muito_curta():
    result = validate_password("Ab1!")
    assert result == 'muito_curta'

def test_validate_password_sem_maiuscula():
    result = validate_password("abcdefgh1!")
    assert result == 'sem_maiuscula'

def test_validate_password_sem_minuscula():
    result = validate_password("ABCDEFGH1!")
    assert result == 'sem_minuscula'

def test_validate_password_sem_numero():
    result = validate_password("Abcdefgh!")
    assert result == 'sem_numero'

def test_validate_password_sem_especial():
    result = validate_password("Abcdefgh1")
    assert result == 'sem_especial'

def test_validate_password_valida():
    result = validate_password("Abcdefgh1!")
    assert result == 'valida'