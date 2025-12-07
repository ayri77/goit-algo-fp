"""
Юніт-тести для функцій візуалізації фрактала "дерево Піфагора".

Перевіряє коректність візуалізації для різних режимів та типів візуалізації.
"""

import pytest
import sys
import math
from pathlib import Path
from unittest.mock import patch, MagicMock

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from visualization import draw_pythagorean_tree, draw_pythagorean_tree_turtle
from fractal import calculate_pythagorean_tree


@pytest.mark.unit
class TestVisualizationMatplotlib:
    """Тести для matplotlib-візуалізації."""
    
    def test_draw_pythagorean_tree_empty_squares(self):
        """Тест візуалізації з порожнім списком квадратів."""
        with patch('visualization.plt.show'):
            # Не повинно викликати помилку
            draw_pythagorean_tree([], mode='tree')
    
    def test_draw_pythagorean_tree_mode_squares(self):
        """Тест візуалізації квадратів для перевірки координат."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        with patch('visualization.plt.show'):
            # Не повинно викликати помилку
            draw_pythagorean_tree(squares, level=1, mode='squares')
    
    def test_draw_pythagorean_tree_mode_tree(self):
        """Тест візуалізації дерева (лінії)."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        with patch('visualization.plt.show'):
            # Не повинно викликати помилку
            draw_pythagorean_tree(squares, level=1, mode='tree')
    
    def test_draw_pythagorean_tree_multiple_levels(self):
        """Тест візуалізації для різних рівнів рекурсії."""
        for level in range(1, 4):
            squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, level, 45)
            
            with patch('visualization.plt.show'):
                draw_pythagorean_tree(squares, level=level, mode='tree')
                draw_pythagorean_tree(squares, level=level, mode='squares')
    
    def test_draw_pythagorean_tree_different_angles(self):
        """Тест візуалізації з різними кутами."""
        angles = [30, 45, 60]
        for angle in angles:
            squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 2, angle)
            
            with patch('visualization.plt.show'):
                draw_pythagorean_tree(squares, level=2, angle=angle, mode='tree')
    
    def test_draw_pythagorean_tree_square_coordinates(self):
        """Тест перевірки координат квадратів."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        # Перевіряємо, що квадрати мають правильну структуру
        assert len(squares) > 0
        for square in squares:
            x1, y1, x2, y2, size = square
            assert isinstance(x1, (int, float))
            assert isinstance(y1, (int, float))
            assert isinstance(x2, (int, float))
            assert isinstance(y2, (int, float))
            assert isinstance(size, (int, float))
            assert size > 0
            
            # Перевіряємо, що розмір відповідає відстані між точками
            calculated_size = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            assert abs(calculated_size - size) < 0.01  # Допускаємо невелику похибку


@pytest.mark.unit
class TestVisualizationTurtle:
    """Тести для turtle-візуалізації."""
    
    def test_draw_pythagorean_tree_turtle_mode_squares(self):
        """Тест turtle-візуалізації в режимі squares."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        with patch('visualization.turtle.done'):
            with patch('visualization._draw_tree_recursive_turtle'):
                # Не повинно викликати помилку
                draw_pythagorean_tree_turtle(
                    squares, level=1, size=100, angle=45, 
                    mode='squares', speed=0
                )
    
    def test_draw_pythagorean_tree_turtle_mode_tree(self):
        """Тест turtle-візуалізації в режимі tree."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        with patch('visualization.turtle.done'):
            with patch('visualization.turtle.goto'):
                with patch('visualization.turtle.pendown'):
                    with patch('visualization.turtle.penup'):
                        # Не повинно викликати помилку
                        draw_pythagorean_tree_turtle(
                            squares, level=1, size=100, angle=45, 
                            mode='tree', speed=0
                        )
    
    def test_draw_pythagorean_tree_turtle_empty_squares_tree_mode(self):
        """Тест turtle-візуалізації з порожнім списком у режимі tree."""
        with patch('visualization.turtle.done'):
            # Не повинно викликати помилку
            draw_pythagorean_tree_turtle([], mode='tree')
   
    def test_draw_pythagorean_tree_turtle_custom_start_position(self):
        """Тест turtle-візуалізації з користувацькою початковою позицією."""
        squares = calculate_pythagorean_tree(0, 0, 100, 0, 0, 1, 45)
        
        with patch('visualization.turtle.done'):
            with patch('visualization._draw_tree_recursive_turtle'):
                draw_pythagorean_tree_turtle(
                    squares, level=1, mode='squares', 
                    start_position=(10, 20)
                )

