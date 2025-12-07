"""
Юніт-тести для бінарної купи (мінімальної).

Перевіряє операції з купою: вставка, видалення мінімуму, зменшення ключа.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху (важливо для уникнення конфлікту з task_4)
sys.path.insert(0, str(Path(__file__).parent))

from binary_heap import MinHeap


@pytest.mark.unit
class TestMinHeap:
    """Тести для класу MinHeap."""
    
    def test_create_empty_heap(self):
        """Тест створення порожньої купи."""
        heap = MinHeap()
        assert heap.is_empty()
        assert len(heap.heap) == 0
    
    def test_insert_single_element(self):
        """Тест вставки одного елемента."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        assert not heap.is_empty()
        assert len(heap.heap) == 1
    
    def test_insert_multiple_elements(self):
        """Тест вставки кількох елементів."""
        heap = MinHeap()
        heap.insert(3.0, 'A')
        heap.insert(1.0, 'B')
        heap.insert(2.0, 'C')
        assert len(heap.heap) == 3
    
    def test_extract_min(self):
        """Тест видалення мінімального елемента."""
        heap = MinHeap()
        heap.insert(3.0, 'A')
        heap.insert(1.0, 'B')
        heap.insert(2.0, 'C')
        
        min_elem = heap.extract_min()
        assert min_elem is not None
        assert min_elem[0] == 1.0  # Мінімальна відстань
        assert min_elem[1] == 'B'
        assert len(heap.heap) == 2
    
    def test_extract_min_empty_heap(self):
        """Тест видалення з порожньої купи."""
        heap = MinHeap()
        result = heap.extract_min()
        assert result is None
    
    def test_extract_min_maintains_heap_property(self):
        """Тест, що після видалення зберігається властивість купи."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        heap.insert(3.0, 'B')
        heap.insert(1.0, 'C')
        heap.insert(4.0, 'D')
        heap.insert(2.0, 'E')
        
        # Видаляємо мінімум
        min_elem = heap.extract_min()
        assert min_elem[0] == 1.0
        
        # Наступний мінімум повинен бути 2.0
        next_min = heap.extract_min()
        assert next_min[0] == 2.0
    
    def test_extract_all_elements(self):
        """Тест послідовного видалення всіх елементів."""
        heap = MinHeap()
        values = [(5.0, 'A'), (1.0, 'B'), (3.0, 'C'), (2.0, 'D')]
        for dist, vertex in values:
            heap.insert(dist, vertex)
        
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())
        
        # Перевіряємо, що елементи витягнуті в правильному порядку
        distances = [elem[0] for elem in extracted]
        assert distances == [1.0, 2.0, 3.0, 5.0]
    
    def test_decrease_key(self):
        """Тест зменшення ключа елемента."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        heap.insert(3.0, 'B')
        heap.insert(4.0, 'C')
        
        # Зменшуємо ключ для 'A'
        heap.decrease_key('A', 1.0)
        
        # Тепер мінімум повинен бути 'A'
        min_elem = heap.extract_min()
        assert min_elem[1] == 'A'
        assert min_elem[0] == 1.0
    
    def test_decrease_key_vertex_not_found(self):
        """Тест зменшення ключа для неіснуючої вершини."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        heap.insert(3.0, 'B')
        
        # Спробуємо зменшити ключ для неіснуючої вершини
        with pytest.raises(ValueError, match="Вершина C не знайдена в купі"):
            heap.decrease_key('C', 1.0)
    
    def test_decrease_key_to_minimum(self):
        """Тест зменшення ключа до мінімального значення."""
        heap = MinHeap()
        heap.insert(10.0, 'A')
        heap.insert(5.0, 'B')
        heap.insert(7.0, 'C')
        
        # Зменшуємо 'A' до мінімуму
        heap.decrease_key('A', 1.0)
        
        # Перевіряємо, що 'A' тепер мінімум
        min_elem = heap.extract_min()
        assert min_elem == (1.0, 'A')
    
    def test_decrease_key_multiple_times(self):
        """Тест множинного зменшення ключа для однієї вершини."""
        heap = MinHeap()
        heap.insert(10.0, 'A')
        heap.insert(5.0, 'B')
        heap.insert(8.0, 'C')
        
        # Зменшуємо 'A' кілька разів
        heap.decrease_key('A', 6.0)
        heap.decrease_key('A', 3.0)
        heap.decrease_key('A', 1.0)
        
        # Перевіряємо порядок видалення
        assert heap.extract_min() == (1.0, 'A')
        assert heap.extract_min() == (5.0, 'B')
        assert heap.extract_min() == (8.0, 'C')
    
    def test_decrease_key_maintains_heap_property(self):
        """Тест, що після зменшення ключа зберігається властивість купи."""
        heap = MinHeap()
        heap.insert(10.0, 'A')
        heap.insert(5.0, 'B')
        heap.insert(7.0, 'C')
        heap.insert(8.0, 'D')
        heap.insert(6.0, 'E')
        
        # Зменшуємо ключ для 'A'
        heap.decrease_key('A', 2.0)
        
        # Перевіряємо, що всі елементи витягуються в правильному порядку
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_min())
        
        distances = [elem[0] for elem in extracted]
        assert distances == [2.0, 5.0, 6.0, 7.0, 8.0]
    
    def test_insert_maintains_heap_property(self):
        """Тест, що вставка зберігає властивість купи."""
        heap = MinHeap()
        values = [(10.0, 'A'), (5.0, 'B'), (1.0, 'C'), (7.0, 'D'), (3.0, 'E')]
        for dist, vertex in values:
            heap.insert(dist, vertex)
        
        # Перевіряємо, що мінімум завжди на вершині
        assert heap.extract_min()[0] == 1.0
        assert heap.extract_min()[0] == 3.0
        assert heap.extract_min()[0] == 5.0
    
    def test_heap_property_after_complex_operations(self):
        """Тест властивості купи після складних операцій."""
        heap = MinHeap()
        heap.insert(10.0, 'A')
        heap.insert(5.0, 'B')
        heap.insert(15.0, 'C')
        heap.insert(3.0, 'D')
        
        # Видаляємо мінімум
        assert heap.extract_min() == (3.0, 'D')
        
        # Зменшуємо ключ
        heap.decrease_key('C', 2.0)
        
        # Додаємо новий елемент
        heap.insert(1.0, 'E')
        
        # Перевіряємо порядок
        assert heap.extract_min() == (1.0, 'E')
        assert heap.extract_min() == (2.0, 'C')
        assert heap.extract_min() == (5.0, 'B')
        assert heap.extract_min() == (10.0, 'A')
    
    def test_decrease_key_with_same_distance(self):
        """Тест зменшення ключа до того ж значення."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        heap.insert(3.0, 'B')
        
        # Зменшуємо 'A' до того ж значення (технічно не зменшення)
        heap.decrease_key('A', 5.0)
        
        # Перевіряємо, що структура не зламалася
        assert heap.extract_min() == (3.0, 'B')
        assert heap.extract_min() == (5.0, 'A')
    
    def test_decrease_key_increase_distance(self):
        """Тест збільшення ключа через decrease_key (некоректне використання)."""
        heap = MinHeap()
        heap.insert(5.0, 'A')
        heap.insert(3.0, 'B')
        
        # Збільшуємо ключ (некоректне використання, але функція це дозволяє)
        heap.decrease_key('A', 10.0)
        
        # Перевіряємо, що структура все ще працює
        # Але 'A' не буде мінімумом
        assert heap.extract_min() == (3.0, 'B')
        # Примітка: після збільшення ключа потрібно просіювання вниз,
        # але поточна реалізація просіює тільки вгору
        # Це тест показує обмеження поточної реалізації

