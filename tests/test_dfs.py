import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import dfs

def test_dfs_start_nao_esta_em_graph():
    graph = {'A': ['B', 'C'], 'B': ['D']}
    start = 'X'
    result = dfs(graph, start)
    assert result == ['X']

def test_dfs_start_esta_em_graph_sem_vizinhos_visitados():
    graph = {'A': ['B', 'C'], 'B': ['D']}
    start = 'A'
    result = dfs(graph, start)
    assert result == ['A']

def test_dfs_start_esta_em_graph_com_vizinhos_nao_visitados():
    graph = {'A': ['B', 'C'], 'B': ['D']}
    start = 'A'
    visited = set()
    result = dfs(graph, start, visited)
    assert result == ['A']

def test_dfs_visited_nao_none():
    graph = {'A': ['B', 'C'], 'B': ['D']}
    start = 'A'
    visited = set(['A'])
    result = dfs(graph, start, visited)
    assert result == ['A']

def test_dfs_graph_vazio():
    graph = {}
    start = 'A'
    result = dfs(graph, start)
    assert result == ['A']

def test_dfs_start_nao_esta_em_graph_com_visited():
    graph = {'A': ['B', 'C'], 'B': ['D']}
    start = 'X'
    visited = set()
    result = dfs(graph, start, visited)
    assert result == ['X']