import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import reverse_list


### Teste para Lista Vazia
def test_reverse_list_lista_vazia():
    result = reverse_list([])
    assert result == []

### Teste para Lista com Um Elemento
def test_reverse_list_lista_um_elemento():
    result = reverse_list([1])
    assert result == [1]

### Teste para Lista com Múltiplos Elementos
def test_reverse_list_lista_multiplos_elementos():
    result = reverse_list([1, 2, 3, 4, 5])
    assert result == [5, 4, 3, 2, 1]

### Teste para Lista com Elementos de Diferentes Tipos
def test_reverse_list_lista_elementos_diferentes_tipos():
    result = reverse_list([1, 'a', 3.5, True])
    assert result == [True, 3.5, 'a', 1]

#
def test_reverse_list_entrada_nao_lista():
    try:
        reverse_list('not a list')
    except Exception as e:
        assert isinstance(e, TypeError) or isinstance(e, AttributeError)
