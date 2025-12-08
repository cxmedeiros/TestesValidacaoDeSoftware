import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import month_name

def test_month_name_janeiro():
    result = month_name(1)
    assert result == 'Janeiro'

def test_month_name_fevereiro():
    result = month_name(2)
    assert result == 'Fevereiro'

def test_month_name_marco():
    result = month_name(3)
    assert result == 'Março'

def test_month_name_abril():
    result = month_name(4)
    assert result == 'Abril'

def test_month_name_maio():
    result = month_name(5)
    assert result == 'Maio'

def test_month_name_junho():
    result = month_name(6)
    assert result == 'Junho'

def test_month_name_julho():
    result = month_name(7)
    assert result == 'Julho'

def test_month_name_agosto():
    result = month_name(8)
    assert result == 'Agosto'

def test_month_name_setembro():
    result = month_name(9)
    assert result == 'Setembro'

def test_month_name_outubro():
    result = month_name(10)
    assert result == 'Outubro'

def test_month_name_novembro():
    result = month_name(11)
    assert result == 'Novembro'

def test_month_name_dezembro():
    result = month_name(12)
    assert result == 'Dezembro'

def test_month_name_invalido():
    result = month_name(13)
    assert result == 'Inválido'

def test_month_name_valor_negativo():
    result = month_name(-1)
    assert result == 'Inválido'

def test_month_name_valor_zero():
    result = month_name(0)
    assert result == 'Inválido'

def test_month_name_valor_nao_inteiro():
    result = month_name('1')
    assert result == 'Inválido'