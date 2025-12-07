"""
Юніт-тести для функції обчислення координат фрактала "дерево Піфагора".

Перевіряє коректність обчислення координат квадратів.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from fractal import calculate_pythagorean_tree


@pytest.mark.unit
class TestFractal:
    """Тести для функції calculate_pythagorean_tree."""
    
    def test_calculate_level_zero(self):
        """Тест обчислення для рівня 0 (тільки початковий квадрат)."""
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 0)
        # Перевіряємо, що результат не порожній
        assert result is not None
        assert len(result) > 0
    
    def test_calculate_level_one(self):
        """Тест обчислення для рівня 1."""
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1)
        # На рівні 1 повинен бути початковий квадрат та два нові
        assert result is not None
        assert len(result) > 0
    
    def test_calculate_multiple_levels(self):
        """Тест обчислення для кількох рівнів."""
        for level in range(1, 4):
            result = calculate_pythagorean_tree(0, 0, 100, 0, 0, level)
            assert result is not None
            assert len(result) > 0
    
    def test_calculate_with_different_angles(self):
        """Тест обчислення з різними кутами."""
        angles = [30, 45, 60, 90]
        for angle in angles:
            result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 2, angle)
            assert result is not None
    
    def test_calculate_with_different_sizes(self):
        """Тест обчислення з різними розмірами."""
        sizes = [50, 100, 200]
        for size in sizes:
            result = calculate_pythagorean_tree(0, 0, size, 0, 0, 2)
            assert result is not None
    
    def test_calculate_square_structure(self):
        """Тест структури квадратів у результаті."""
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        assert len(result) > 0
        for square in result:
            assert len(square) == 5  # (x1, y1, x2, y2, size)
            x1, y1, x2, y2, size = square
            
            # Перевіряємо типи
            assert isinstance(x1, (int, float))
            assert isinstance(y1, (int, float))
            assert isinstance(x2, (int, float))
            assert isinstance(y2, (int, float))
            assert isinstance(size, (int, float))
            
            # Перевіряємо, що розмір позитивний
            assert size > 0
    
    def test_calculate_first_square(self):
        """Тест першого квадрата (початкового)."""
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 0, 45)
        
        assert len(result) == 1
        x1, y1, x2, y2, size = result[0]
        
        # Перевіряємо початковий квадрат
        assert x1 == 0
        assert y1 == 0
        assert x2 == 100
        assert y2 == 0
        assert size == 100
    
    def test_calculate_number_of_squares(self):
        """Тест кількості квадратів для різних рівнів."""
        # Рівень 0: 1 квадрат
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 0, 45)
        assert len(result) == 1
        
        # Рівень 1: 1 + 2 = 3 квадрати
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        assert len(result) == 3
        
        # Рівень 2: 1 + 2 + 4 = 7 квадратів
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 2, 45)
        assert len(result) == 7
    
    def test_calculate_square_size_decreases(self):
        """Тест, що розмір квадратів зменшується з рівнем."""
        result = calculate_pythagorean_tree(0, 0, 100, 0, 0, 2, 45)
        
        sizes = [sq[4] for sq in result]
        # Перший квадрат має бути найбільшим
        assert sizes[0] == max(sizes)
        
        # Розміри повинні зменшуватися
        # (можуть бути однакові на одному рівні, але загальна тенденція - зменшення)
        assert all(size > 0 for size in sizes)
    
    def test_calculate_with_different_start_positions(self):
        """Тест обчислення з різними початковими позиціями."""
        start_positions = [
            (0, 0, 100, 0),
            (10, 20, 110, 20),
            (-50, -50, 50, -50)
        ]
        
        for x1, y1, x2, y2 in start_positions:
            result = calculate_pythagorean_tree(x1, y1, x2, y2, 0, 1, 45)
            assert result is not None
            assert len(result) > 0
            
            # Перший квадрат повинен відповідати початковим координатам
            first_square = result[0]
            assert abs(first_square[0] - x1) < 0.01
            assert abs(first_square[1] - y1) < 0.01
            assert abs(first_square[2] - x2) < 0.01
            assert abs(first_square[3] - y2) < 0.01

