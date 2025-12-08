import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import validate_email

def test_validate_email_caminho_1_email_nulo():
    result = validate_email(None)
    assert result == False

def test_validate_email_caminho_1_email_nao_string():
    result = validate_email(123)
    assert result == False

def test_validate_email_caminho_2_sem_arroba():
    result = validate_email("email_sem_arroba.com")
    assert result == False

def test_validate_email_caminho_2_mais_de_um_arroba():
    result = validate_email("email@com@outro.com")
    assert result == False

def test_validate_email_caminho_3_parte_local_vazia():
    result = validate_email("@domain.com")
    assert result == False

def test_validate_email_caminho_3_dominio_vazio():
    result = validate_email("local@")
    assert result == False

def test_validate_email_caminho_4_dominio_sem_ponto():
    result = validate_email("local@dominio")
    assert result == False

def test_validate_email_caminho_5_dominio_comeca_com_ponto():
    result = validate_email("local@.dominio.com")
    assert result == False

def test_validate_email_caminho_5_dominio_termina_com_ponto():
    result = validate_email("local@dominio.")
    assert result == False

def test_validate_email_caminho_6_dominio_com_dois_pontos_consecutivos():
    result = validate_email("local@dom..inio.com")
    assert result == False

def test_validate_email_caminho_7_email_valido():
    result = validate_email("local@dominio.com")
    assert result == True