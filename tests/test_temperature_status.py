import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import temperature_status

def test_temperature_status_congelante():
    result = temperature_status(0)
    assert result == 'congelante'

def test_temperature_status_frio():
    result = temperature_status(10)
    assert result == 'frio'

def test_temperature_status_agradavel():
    result = temperature_status(25)
    assert result == 'agradável'

def test_temperature_status_quente():
    result = temperature_status(30)
    assert result == 'quente'

def test_temperature_status_valor_negativo():
    result = temperature_status(-5)
    assert result == 'congelante'