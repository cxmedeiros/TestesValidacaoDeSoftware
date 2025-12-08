import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import flatten_dict

def test_flatten_dict_dicionario_vazio():
    result = flatten_dict({})
    assert result == {}

def test_flatten_dict_sem_parent_key_e_valor_nao_dicionario():
    result = flatten_dict({'a': 1})
    assert result == {'a': 1}

def test_flatten_dict_com_parent_key_e_valor_nao_dicionario():
    result = flatten_dict({'a': 1}, 'parent')
    assert result == {'parent.a': 1}

def test_flatten_dict_sem_parent_key_e_valor_dicionario():
    result = flatten_dict({'a': {'b': 2}})
    assert result == {'a.b': 2}

def test_flatten_dict_com_parent_key_e_valor_dicionario():
    result = flatten_dict({'a': {'b': 2}}, 'parent')
    assert result == {'parent.a.b': 2}

def test_flatten_dict_com_multiple_niveis():
    result = flatten_dict({'a': {'b': {'c': 3}}})
    assert result == {'a.b.c': 3}

def test_flatten_dict_com_separador_diferente():
    result = flatten_dict({'a': {'b': 2}}, sep='_')
    assert result == {'a_b': 2}