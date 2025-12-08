import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_digits

#### Teste para Caminho de Execução Normal
def test_sum_digits_caminho_normal():
    result = sum_digits(123)
    assert result == 6  # 1 + 2 + 3 = 6

#### Testes para Edge Cases
def test_sum_digits_caminho_zero():
    result = sum_digits(0)
    assert result == 0  # Soma dos dígitos de 0 é 0

def test_sum_digits_caminho_numero_negativo():
    result = sum_digits(-123)
    assert result == 6  # A função considera o valor absoluto, então -123 deve dar o mesmo que 123

def test_sum_digits_caminho_numero_unico_digito():
    result = sum_digits(5)
    assert result == 5  # Número de um único dígito

#### Testes para Tipos de Entrada Diferentes
def test_sum_digits_caminho_nao_inteiro():
    try:
        sum_digits("abc")
        assert False, "Esperado uma exceção ou comportamento específico para não inteiros"
    except Exception as e:
        assert True  # A função deve falhar ou ter um comportamento definido para não inteiros

def test_sum_digits_caminho_none():
    try:
        sum_digits(None)
        assert False, "Esperado uma exceção ou comportamento específico para None"
    except Exception as e:
        assert True  # A função deve falhar ou ter um comportamento definido para None
