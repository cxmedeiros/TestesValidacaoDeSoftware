import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import is_leap_year

def test_is_leap_year_divisivel_por_400():
    result = is_leap_year(2000)
    assert result == True

def test_is_leap_year_divisivel_por_100_mas_nao_por_400():
    result = is_leap_year(1900)
    assert result == False

def test_is_leap_year_divisivel_por_4_mas_nao_por_100():
    result = is_leap_year(2020)
    assert result == True

def test_is_leap_year_nao_divisivel_por_4_100_ou_400():
    result = is_leap_year(2019)
    assert result == False