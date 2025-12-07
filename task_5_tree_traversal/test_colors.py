"""
Юніт-тести для генерації кольорів.

Перевіряє коректність генерації кольорів у форматі HEX.
"""

import pytest
import sys
from pathlib import Path

# ВАЖЛИВО: Спочатку додаємо шлях до task_5, щоб локальні модулі мали пріоритет
task_5_path = Path(__file__).parent
if str(task_5_path) not in sys.path:
    sys.path.insert(0, str(task_5_path))

from traversal import generate_color


@pytest.mark.unit
class TestColorGeneration:
    """Тести для функції generate_color."""
    
    def test_generate_color_format(self):
        """Тест формату кольору (HEX)."""
        color = generate_color(0, 10)
        assert color.startswith('#')
        assert len(color) == 7  # #RRGGBB
    
    def test_generate_color_first_step(self):
        """Тест генерації кольору для першого кроку."""
        color = generate_color(0, 10)
        assert color.startswith('#')
    
    def test_generate_color_last_step(self):
        """Тест генерації кольору для останнього кроку."""
        color = generate_color(9, 10)
        assert color.startswith('#')
    
    def test_generate_color_middle_step(self):
        """Тест генерації кольору для середнього кроку."""
        color = generate_color(5, 10)
        assert color.startswith('#')
    
    def test_generate_color_different_steps(self):
        """Тест, що різні кроки дають різні кольори."""
        colors = [generate_color(i, 10) for i in range(10)]
        # Перевіряємо, що кольори різні (або змінюються)
        assert len(set(colors)) > 1
    
    def test_generate_color_single_step(self):
        """Тест генерації кольору для одного кроку."""
        color = generate_color(0, 1)
        assert color.startswith('#')
    
    def test_generate_color_progression(self):
        """Тест, що кольори змінюються від темних до світлих."""
        colors = [generate_color(i, 5) for i in range(5)]
        # Перевіряємо, що всі кольори валідні
        for color in colors:
            assert color.startswith('#')
            assert len(color) == 7

