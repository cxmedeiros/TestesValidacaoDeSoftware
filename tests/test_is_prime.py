import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import is_prime

def test_is_prime_caminho_1_menor_que_2():
    result = is_prime(1)
    assert result == False

def test_is_prime_caminho_2_igual_a_2():
    result = is_prime(2)
    assert result == True

def test_is_prime_caminho_3_par_diferente_de_2():
    result = is_prime(4)
    assert result == False

def test_is_prime_caminho_4_impar_com_divisor():
    result = is_prime(9)
    assert result == False

def test_is_prime_caminho_5_impar_sem_divisor():
    result = is_prime(7)
    assert result == True