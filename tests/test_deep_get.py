import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import deep_get

def test_deep_get_keys_falso_retorna_d():
    d = {'a': 1}
    keys = []
    result = deep_get(d, keys)
    assert result == d

def test_deep_get_d_nao_eh_dicionario_retorna_default():
    d = 'not a dict'
    keys = ['a']
    default = 'default'
    result = deep_get(d, keys, default)
    assert result == default

def test_deep_get_key_nao_existe_retorna_default():
    d = {'a': 1}
    keys = ['b']
    default = 'default'
    result = deep_get(d, keys, default)
    assert result == default

def test_deep_get_key_existe_chama_recursivamente():
    d = {'a': {'b': 2}}
    keys = ['a', 'b']
    result = deep_get(d, keys)
    assert result == 2