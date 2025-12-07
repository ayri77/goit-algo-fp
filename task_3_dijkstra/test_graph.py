"""
Юніт-тести для структури графа.

Перевіряє операції з графом: додавання вершин та ребер.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from graph import Graph


@pytest.mark.unit
class TestGraph:
    """Тести для класу Graph."""
    
    def test_create_empty_graph(self):
        """Тест створення порожнього графа."""
        graph = Graph()
        assert len(graph.vertices) == 0
    
    def test_add_vertex(self):
        """Тест додавання вершини."""
        graph = Graph()
        graph.add_vertex('A')
        assert 'A' in graph.vertices
        assert graph.vertices['A'] == []
    
    def test_add_multiple_vertices(self):
        """Тест додавання кількох вершин."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        assert len(graph.vertices) == 3
        assert 'A' in graph.vertices
        assert 'B' in graph.vertices
        assert 'C' in graph.vertices
    
    def test_add_edge(self):
        """Тест додавання ребра."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_edge('A', 'B', 5.0)
        
        neighbors = graph.get_neighbors('A')
        assert len(neighbors) == 1
        assert neighbors[0] == ('B', 5.0)
    
    def test_add_multiple_edges(self):
        """Тест додавання кількох ребер."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 1.0)
        graph.add_edge('A', 'C', 2.0)
        
        neighbors = graph.get_neighbors('A')
        assert len(neighbors) == 2
        assert ('B', 1.0) in neighbors
        assert ('C', 2.0) in neighbors
    
    def test_get_neighbors_empty(self):
        """Тест отримання сусідів для вершини без сусідів."""
        graph = Graph()
        graph.add_vertex('A')
        neighbors = graph.get_neighbors('A')
        assert neighbors == []
    
    def test_get_neighbors_nonexistent_vertex(self):
        """Тест отримання сусідів для неіснуючої вершини."""
        graph = Graph()
        neighbors = graph.get_neighbors('X')
        assert neighbors == []
    
    def test_directed_graph(self):
        """Тест, що граф є спрямованим (ребра односторонні)."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_edge('A', 'B', 5.0)
        
        # Перевіряємо, що B не має ребра до A
        neighbors_b = graph.get_neighbors('B')
        assert len(neighbors_b) == 0

    def test_add_edge_auto_creates_vertices(self):
        """Тест, що add_edge автоматично створює вершини."""
        graph = Graph()
        # Додаємо ребро без попереднього створення вершин
        graph.add_edge('A', 'B', 5.0)
        
        assert 'A' in graph.vertices
        assert 'B' in graph.vertices
        neighbors = graph.get_neighbors('A')
        assert neighbors[0] == ('B', 5.0)

    def test_update_existing_edge(self):
        """Тест оновлення існуючого ребра."""
        graph = Graph()
        graph.add_edge('A', 'B', 5.0)
        
        # Оновлюємо вагу ребра
        graph.add_edge('A', 'B', 10.0)
        
        neighbors = graph.get_neighbors('A')
        assert len(neighbors) == 1
        assert neighbors[0] == ('B', 10.0)

    def test_add_vertex_idempotent(self):
        """Тест, що додавання вершини двічі не створює дублікатів."""
        graph = Graph()
        graph.add_vertex('A')
        graph.add_vertex('A')  # Додаємо вдруге
        
        assert len(graph.vertices) == 1
        assert 'A' in graph.vertices
        assert graph.vertices['A'] == []

    def test_self_loop(self):
        """Тест додавання ребра від вершини до самої себе."""
        graph = Graph()
        graph.add_edge('A', 'A', 3.0)
        
        neighbors = graph.get_neighbors('A')
        assert len(neighbors) == 1
        assert neighbors[0] == ('A', 3.0)

    def test_bidirectional_edges(self):
        """Тест додавання ребер в обидва напрямки."""
        graph = Graph()
        graph.add_edge('A', 'B', 5.0)
        graph.add_edge('B', 'A', 3.0)  # Зворотне ребро
        
        neighbors_a = graph.get_neighbors('A')
        neighbors_b = graph.get_neighbors('B')
        
        assert len(neighbors_a) == 1
        assert neighbors_a[0] == ('B', 5.0)
        assert len(neighbors_b) == 1
        assert neighbors_b[0] == ('A', 3.0)

    def test_multiple_edges_from_same_vertex(self):
        """Тест додавання кількох ребер від однієї вершини."""
        graph = Graph()
        graph.add_edge('A', 'B', 1.0)
        graph.add_edge('A', 'C', 2.0)
        graph.add_edge('A', 'D', 3.0)
        
        neighbors = graph.get_neighbors('A')
        assert len(neighbors) == 3
        assert ('B', 1.0) in neighbors
        assert ('C', 2.0) in neighbors
        assert ('D', 3.0) in neighbors

    def test_complex_graph_structure(self):
        """Тест складного графа з багатьма вершинами та ребрами."""
        graph = Graph()
        # Створюємо граф: A -> B -> C, A -> D, B -> D
        graph.add_edge('A', 'B', 1.0)
        graph.add_edge('B', 'C', 2.0)
        graph.add_edge('A', 'D', 3.0)
        graph.add_edge('B', 'D', 1.5)
        
        assert len(graph.vertices) == 4
        assert len(graph.get_neighbors('A')) == 2
        assert len(graph.get_neighbors('B')) == 2
        assert len(graph.get_neighbors('C')) == 0
        assert len(graph.get_neighbors('D')) == 0