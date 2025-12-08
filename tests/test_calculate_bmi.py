import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import calculate_bmi

def test_calculate_bmi_peso_zero():
    result = calculate_bmi(0, 1.75)
    assert result == (None, 'invalido')

def test_calculate_bmi_altura_zero():
    result = calculate_bmi(70, 0)
    assert result == (None, 'invalido')

def test_calculate_bmi_peso_negativo():
    result = calculate_bmi(-1, 1.75)
    assert result == (None, 'invalido')

def test_calculate_bmi_altura_negativa():
    result = calculate_bmi(70, -1.75)
    assert result == (None, 'invalido')

def test_calculate_bmi_abaixo_peso():
    result = calculate_bmi(40, 1.75)
    bmi = 40 / (1.75 ** 2)
    assert result == (bmi, 'abaixo_peso')

def test_calculate_bmi_normal():
    result = calculate_bmi(60, 1.75)
    bmi = 60 / (1.75 ** 2)
    assert result == (bmi, 'normal')

def test_calculate_bmi_sobrepeso():
    result = calculate_bmi(80, 1.75)
    bmi = 80 / (1.75 ** 2)
    assert result == (bmi, 'sobrepeso')

def test_calculate_bmi_obesidade_1():
    result = calculate_bmi(90, 1.60)
    bmi = 90 / (1.60 ** 2)
    assert result == (bmi, 'obesidade_1')

def test_calculate_bmi_obesidade_2():
    result = calculate_bmi(100, 1.60)
    bmi = 100 / (1.60 ** 2)
    assert result == (bmi, 'obesidade_2')

def test_calculate_bmi_obesidade_3():
    result = calculate_bmi(110, 1.60)
    bmi = 110 / (1.60 ** 2)
    assert result == (bmi, 'obesidade_3')