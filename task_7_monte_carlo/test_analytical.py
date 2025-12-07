"""
Юніт-тести для аналітичних розрахунків ймовірностей.

Перевіряє коректність аналітичних формул.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from monte_carlo import analytical_probabilities


@pytest.mark.unit
class TestAnalyticalProbabilities:
    """Тести для функції analytical_probabilities."""
    
    def test_analytical_all_sums_present(self):
        """Тест, що всі суми від 2 до 12 присутні."""
        result = analytical_probabilities()
        expected_sums = list(range(2, 13))
        
        for sum_val in expected_sums:
            assert sum_val in result, f"Сума {sum_val} відсутня"
    
    def test_analytical_probabilities_range(self):
        """Тест, що ймовірності знаходяться в діапазоні [0, 1]."""
        result = analytical_probabilities()
        
        for sum_val, probability in result.items():
            assert 0 <= probability <= 1, \
                f"Ймовірність {probability} для суми {sum_val} поза діапазоном"
    
    def test_analytical_probabilities_sum(self):
        """Тест, що сума ймовірностей дорівнює 1."""
        result = analytical_probabilities()
        total_probability = sum(result.values())
        
        assert abs(total_probability - 1.0) < 0.0001, \
            f"Сума ймовірностей {total_probability} не дорівнює 1"
    
    def test_analytical_most_likely_sum(self):
        """Тест, що найбільш ймовірна сума - 7."""
        result = analytical_probabilities()
        
        sum_7_prob = result[7]
        other_probs = [prob for sum_val, prob in result.items() if sum_val != 7]
        
        assert sum_7_prob > max(other_probs), \
            "Сума 7 не має найбільшої ймовірності"
    
    def test_analytical_symmetry(self):
        """Тест симетрії ймовірностей (суми 2 і 12, 3 і 11, тощо)."""
        result = analytical_probabilities()
        
        # Перевіряємо симетрію
        assert result[2] == result[12], "Сума 2 і 12 повинні мати однакову ймовірність"
        assert result[3] == result[11], "Сума 3 і 11 повинні мати однакову ймовірність"
        assert result[4] == result[10], "Сума 4 і 10 повинні мати однакову ймовірність"
        assert result[5] == result[9], "Сума 5 і 9 повинні мати однакову ймовірність"
        assert result[6] == result[8], "Сума 6 і 8 повинні мати однакову ймовірність"
    
    def test_analytical_specific_values(self):
        """Тест конкретних значень ймовірностей."""
        result = analytical_probabilities()
        
        # Перевіряємо відомі значення
        assert abs(result[2] - 1/36) < 0.0001, "Ймовірність суми 2 повинна бути 1/36"
        assert abs(result[7] - 6/36) < 0.0001, "Ймовірність суми 7 повинна бути 6/36"
        assert abs(result[12] - 1/36) < 0.0001, "Ймовірність суми 12 повинна бути 1/36"

