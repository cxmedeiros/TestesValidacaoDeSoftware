import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import days_in_month

def test_days_in_month_fevereiro_ano_bissexto():
    result = days_in_month(2, leap=True)
    assert result == 29

def test_days_in_month_fevereiro_ano_nao_bissexto():
    result = days_in_month(2, leap=False)
    assert result == 28

def test_days_in_month_meses_com_30_dias():
    result = days_in_month(4)
    assert result == 30

def test_days_in_month_meses_com_31_dias():
    result = days_in_month(1)
    assert result == 31

def test_days_in_month_mes_invalido():
    result = days_in_month(13)
    assert result is None

def test_days_in_month_mes_negativo():
    result = days_in_month(-1)
    assert result is None

def test_days_in_month_mes_zero():
    result = days_in_month(0)
    assert result is None