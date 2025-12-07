"""
Юніт-тести для жадібного алгоритму вибору їжі.

Перевіряє коректність вибору страв з максимізацією калорійності.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from greedy import greedy_algorithm
from main import ITEMS


@pytest.mark.unit
class TestGreedyAlgorithm:
    """Тести для функції greedy_algorithm."""
    
    def test_greedy_empty_budget(self):
        """Тест жадібного алгоритму з нульовим бюджетом."""
        result = greedy_algorithm(ITEMS, 0)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_greedy_small_budget(self):
        """Тест жадібного алгоритму з малим бюджетом."""
        result = greedy_algorithm(ITEMS, 10)
        selected, cost, calories = result
        assert cost <= 10
        assert len(selected) > 0
    
    def test_greedy_medium_budget(self):
        """Тест жадібного алгоритму з середнім бюджетом."""
        result = greedy_algorithm(ITEMS, 50)
        selected, cost, calories = result
        assert cost <= 50
        assert len(selected) > 0
    
    def test_greedy_large_budget(self):
        """Тест жадібного алгоритму з великим бюджетом."""
        result = greedy_algorithm(ITEMS, 200)
        selected, cost, calories = result
        assert cost <= 200
        # З великим бюджетом можна вибрати багато страв
        assert len(selected) > 0
    
    def test_greedy_budget_not_exceeded(self):
        """Тест, що бюджет не перевищується."""
        budgets = [10, 50, 100, 150]
        for budget in budgets:
            result = greedy_algorithm(ITEMS, budget)
            selected, cost, calories = result
            assert cost <= budget, f"Бюджет {budget} перевищено: {cost}"
    
    def test_greedy_returns_valid_items(self):
        """Тест, що повертаються валідні назви страв."""
        result = greedy_algorithm(ITEMS, 100)
        selected, cost, calories = result
        
        for item in selected:
            assert item in ITEMS, f"Невідома страва: {item}"
    
    def test_greedy_calories_calculation(self):
        """Тест правильності обчислення калорійності."""
        result = greedy_algorithm(ITEMS, 100)
        selected, cost, calories = result
        
        # Перевіряємо, що калорійність обчислена правильно
        expected_calories = sum(ITEMS[item]["calories"] for item in selected)
        assert calories == expected_calories
    
    def test_greedy_cost_calculation(self):
        """Тест правильності обчислення вартості."""
        result = greedy_algorithm(ITEMS, 100)
        selected, cost, calories = result
        
        # Перевіряємо, що вартість обчислена правильно
        expected_cost = sum(ITEMS[item]["cost"] for item in selected)
        assert cost == expected_cost
    
    def test_greedy_empty_items(self):
        """Тест жадібного алгоритму з порожнім словником страв."""
        result = greedy_algorithm({}, 100)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_greedy_negative_budget(self):
        """Тест жадібного алгоритму з від'ємним бюджетом."""
        result = greedy_algorithm(ITEMS, -10)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_greedy_all_items_too_expensive(self):
        """Тест жадібного алгоритму, коли всі страви дорожчі за бюджет."""
        expensive_items = {
            "expensive1": {"cost": 100, "calories": 500},
            "expensive2": {"cost": 200, "calories": 800}
        }
        result = greedy_algorithm(expensive_items, 50)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_greedy_zero_cost_item(self):
        """Тест жадібного алгоритму зі стравою з нульовою вартістю."""
        items_with_free = {
            "free": {"cost": 0, "calories": 100},
            "paid": {"cost": 20, "calories": 200}
        }
        result = greedy_algorithm(items_with_free, 20)
        selected, cost, calories = result
        assert "free" in selected  # Безкоштовна страва повинна бути включена
        assert cost <= 20
        assert calories >= 100  # Мінімум калорії від безкоштовної страви
    
    def test_greedy_invalid_data_structure(self):
        """Тест жадібного алгоритму з некоректною структурою даних."""
        invalid_items = {
            "item1": {"price": 10, "calories": 100}  # Неправильне поле "price" замість "cost"
        }
        with pytest.raises(ValueError, match="некоректну структуру даних"):
            greedy_algorithm(invalid_items, 50)
    
    def test_greedy_negative_cost(self):
        """Тест жадібного алгоритму з від'ємною вартістю."""
        invalid_items = {
            "item1": {"cost": -10, "calories": 100}
        }
        with pytest.raises(ValueError, match="від'ємну вартість"):
            greedy_algorithm(invalid_items, 50)
    
    def test_greedy_negative_calories(self):
        """Тест жадібного алгоритму з від'ємною калорійністю."""
        invalid_items = {
            "item1": {"cost": 10, "calories": -100}
        }
        with pytest.raises(ValueError, match="від'ємну калорійність"):
            greedy_algorithm(invalid_items, 50)

