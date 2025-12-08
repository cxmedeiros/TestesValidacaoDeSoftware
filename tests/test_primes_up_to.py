import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import primes_up_to

def test_primes_up_to_menor_que_2_retorna_lista_vazia():
    result = primes_up_to(1)
    assert result == []

def test_primes_up_to_maior_ou_igual_a_2_retorna_primos():
    result = primes_up_to(5)
    assert result == [2, 3, 5]

def test_primes_up_to_valor_negativo_retorna_lista_vazia():
    result = primes_up_to(-5)
    assert result == []

def test_primes_up_to_zero_retorna_lista_vazia():
    result = primes_up_to(0)
    assert result == []

def test_primes_up_to_dois_retorna_dois():
    result = primes_up_to(2)
    assert result == [2]