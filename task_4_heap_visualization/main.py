"""
Головний файл для демонстрації візуалізації бінарної купи.

Створює купу та відображає її структуру.
"""

from binary_heap import BinaryHeap
from visualization import draw_heap


def main():
    """Демонстрація візуалізації бінарної купи."""
    
    # Приклад:
    heap = BinaryHeap()
    heap.insert(0)
    heap.insert(27)
    heap.insert(4)
    heap.insert(1)
    heap.insert(32)
    heap.insert(5)
    heap.insert(10)
    heap.insert(3)
    heap.insert(18)
    heap.insert(19)
    heap.insert(20)
    
    root = heap.build_tree_from_heap()
    draw_heap(root)

if __name__ == "__main__":
    main()

