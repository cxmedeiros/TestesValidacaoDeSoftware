import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import flatten


## Geração de Testes Unitários
### Teste para caminho de lista vazia
def test_flatten_caminho_lista_vazia():
    result = flatten([])
    assert result == []

### Teste para caminho de lista com sublistas
def test_flatten_caminho_lista_com_sublistas():
    result = flatten([[1, 2], [3, 4]])
    assert result == [1, 2, 3, 4]

### Teste para caminho de lista com sublistas vazias
def test_flatten_caminho_lista_com_sublistas_vazias():
    result = flatten([[], []])
    assert result == []

### Teste para caminho de lista com elementos não lista (edge case)
def test_flatten_caminho_elementos_nao_lista():
    try:
        flatten([1, 2, 3])
        assert False, "Esperado TypeError ou comportamento definido para elementos não lista"
    except TypeError:
        assert True
    except Exception as e:
        assert False, f"Exceção inesperada: {e}"

### Teste para caminho de lista com sublistas aninhadas (se aplicável)
def test_flatten_caminho_lista_com_sublistas_aninhadas():
    try:
        flatten([[1, [2]], 3])
        assert False, "Esperado TypeError ou comportamento definido para sublistas aninhadas"
    except TypeError:
        assert True
    except Exception as e:
        assert False, f"Exceção inesperada: {e}"

