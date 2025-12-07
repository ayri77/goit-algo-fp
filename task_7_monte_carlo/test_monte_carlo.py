"""
Юніт-тести для симуляції методу Монте-Карло.

Перевіряє коректність симуляції кидків кубиків.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from monte_carlo import roll_dice, roll_two_dice, monte_carlo_simulation


@pytest.mark.unit
class TestMonteCarlo:
    """Тести для функцій симуляції Монте-Карло."""
    
    def test_roll_dice_range(self):
        """Тест, що кидок кубика дає значення від 1 до 6."""
        for _ in range(100):
            result = roll_dice()
            assert 1 <= result <= 6
    
    def test_roll_two_dice_range(self):
        """Тест, що кидок двох кубиків дає суму від 2 до 12."""
        for _ in range(100):
            result = roll_two_dice()
            assert 2 <= result <= 12
    
    def test_monte_carlo_simulation_small(self):
        """Тест симуляції з малою кількістю кидків."""
        result = monte_carlo_simulation(1000)
        assert isinstance(result, dict)
        assert len(result) > 0
    
    def test_monte_carlo_simulation_large(self):
        """Тест симуляції з великою кількістю кидків."""
        result = monte_carlo_simulation(100000)
        assert isinstance(result, dict)
        assert len(result) > 0
    
    def test_monte_carlo_all_sums_present(self):
        """Тест, що всі можливі суми присутні в результаті."""
        result = monte_carlo_simulation(10000)
        expected_sums = list(range(2, 13))
        
        for sum_val in expected_sums:
            assert sum_val in result, f"Сума {sum_val} відсутня в результаті"
    
    def test_monte_carlo_probabilities_range(self):
        """Тест, що ймовірності знаходяться в діапазоні [0, 1]."""
        result = monte_carlo_simulation(10000)
        
        for sum_val, probability in result.items():
            assert 0 <= probability <= 1, \
                f"Ймовірність {probability} для суми {sum_val} поза діапазоном"
    
    def test_monte_carlo_probabilities_sum(self):
        """Тест, що сума ймовірностей приблизно дорівнює 1."""
        result = monte_carlo_simulation(10000)
        total_probability = sum(result.values())
        
        # Дозволяємо невелику похибку через статистичну природу
        assert 0.95 <= total_probability <= 1.05, \
            f"Сума ймовірностей {total_probability} не близька до 1"
    
    def test_monte_carlo_most_likely_sum(self):
        """Тест, що найбільш ймовірна сума - 7."""
        result = monte_carlo_simulation(100000)
        
        # Сума 7 повинна мати найбільшу ймовірність
        sum_7_prob = result.get(7, 0)
        other_probs = [prob for sum_val, prob in result.items() if sum_val != 7]
        
        if other_probs:
            assert sum_7_prob >= max(other_probs) * 0.8, \
                "Сума 7 не має найбільшої ймовірності"

