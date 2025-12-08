import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import calculate_discount

def test_calculate_discount_preco_ou_quantidade_invalida():
    result = calculate_discount(-1, 'normal', 10)
    assert result == 0

def test_calculate_discount_cliente_normal_sem_desconto():
    result = calculate_discount(100, 'normal', 1)
    assert result == round(100 * (1 - 0), 2)

def test_calculate_discount_cliente_especial_com_desconto():
    result = calculate_discount(100, 'special', 5)
    discount = min(0.2, 0.3)  # Supondo que o desconto para 'special' é 0.2
    assert result == round(100 * (1 - discount), 2)

def test_calculate_discount_cliente_normal_com_desconto_por_quantidade():
    result = calculate_discount(100, 'normal', 10)
    discount = 0.1  # Supondo que o desconto por quantidade é 0.1 para 10 itens
    assert result == round(100 * (1 - discount), 2)

def test_calculate_discount_desconto_maximo():
    result = calculate_discount(100, 'special', 100)
    discount = 0.3  # Desconto máximo
    assert result == round(100 * (1 - discount), 2)
    
def test_calculate_discount_quantidade_zero():
    result = calculate_discount(100, 'normal', 0)
    assert result == 0

def test_calculate_discount_preco_zero():
    result = calculate_discount(0, 'normal', 10)
    assert result == 0