import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import validate_cpf

def test_validate_cpf_comprimento_diferente_de_11():
    result = validate_cpf('1234567890')
    assert result == False

def test_validate_cpf_composto_por_um_unico_digito_repetido():
    result = validate_cpf('11111111111')
    assert result == False

def test_validate_cpf_primeiro_digito_verificador_invalido():
    result = validate_cpf('52998224725') # CPF inválido com primeiro dígito verificador incorreto
    assert result == False

def test_validate_cpf_segundo_digito_verificador_invalido():
    cpf = '52998224724' # CPF com primeiro dígito verificador correto, mas segundo incorreto
    result = validate_cpf(cpf)
    assert result == False

def test_validate_cpf_todos_os_digitos_validos():
    cpf = '52998224725' # Altere para um CPF válido conhecido
    cpf = '45401368090' # CPF válido
    result = validate_cpf(cpf)
    assert result == True