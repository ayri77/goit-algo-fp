"""
Юніт-тести для алгоритму динамічного програмування вибору їжі.

Перевіряє коректність обчислення оптимального набору страв.
"""

import pytest
import sys
from pathlib import Path

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from dynamic_programming import dynamic_programming
from main import ITEMS


@pytest.mark.unit
class TestDynamicProgramming:
    """Тести для функції dynamic_programming."""
    
    def test_dp_empty_budget(self):
        """Тест ДП з нульовим бюджетом."""
        result = dynamic_programming(ITEMS, 0)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_dp_small_budget(self):
        """Тест ДП з малим бюджетом."""
        result = dynamic_programming(ITEMS, 10)
        selected, cost, calories = result
        assert cost <= 10
        assert len(selected) > 0
    
    def test_dp_medium_budget(self):
        """Тест ДП з середнім бюджетом."""
        result = dynamic_programming(ITEMS, 50)
        selected, cost, calories = result
        assert cost <= 50
        assert len(selected) > 0
    
    def test_dp_large_budget(self):
        """Тест ДП з великим бюджетом."""
        result = dynamic_programming(ITEMS, 200)
        selected, cost, calories = result
        assert cost <= 200
        assert len(selected) > 0
    
    def test_dp_budget_not_exceeded(self):
        """Тест, що бюджет не перевищується."""
        budgets = [10, 50, 100, 150]
        for budget in budgets:
            result = dynamic_programming(ITEMS, budget)
            selected, cost, calories = result
            assert cost <= budget, f"Бюджет {budget} перевищено: {cost}"
    
    def test_dp_returns_valid_items(self):
        """Тест, що повертаються валідні назви страв."""
        result = dynamic_programming(ITEMS, 100)
        selected, cost, calories = result
        
        for item in selected:
            assert item in ITEMS, f"Невідома страва: {item}"
    
    def test_dp_calories_calculation(self):
        """Тест правильності обчислення калорійності."""
        result = dynamic_programming(ITEMS, 100)
        selected, cost, calories = result
        
        expected_calories = sum(ITEMS[item]["calories"] for item in selected)
        assert calories == expected_calories
    
    def test_dp_cost_calculation(self):
        """Тест правильності обчислення вартості."""
        result = dynamic_programming(ITEMS, 100)
        selected, cost, calories = result
        
        expected_cost = sum(ITEMS[item]["cost"] for item in selected)
        assert cost == expected_cost
    
    def test_dp_optimality(self):
        """Тест, що ДП знаходить оптимальне рішення."""
        # Для малого бюджету перевіряємо оптимальність
        result = dynamic_programming(ITEMS, 50)
        selected, cost, calories = result
        
        # Перевіряємо, що використано весь бюджет або знайдено оптимальне рішення
        assert cost <= 50
        
        # Порівнюємо з жадібним алгоритмом - ДП повинен давати >= калорій
        from greedy import greedy_algorithm
        greedy_result = greedy_algorithm(ITEMS, 50)
        greedy_calories = greedy_result[2]
        assert calories >= greedy_calories, \
            f"ДП ({calories}) повинен давати >= калорій ніж жадібний ({greedy_calories})"
    
    def test_dp_empty_items(self):
        """Тест ДП з порожнім словником страв."""
        result = dynamic_programming({}, 100)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_dp_negative_budget(self):
        """Тест ДП з від'ємним бюджетом."""
        result = dynamic_programming(ITEMS, -10)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_dp_all_items_too_expensive(self):
        """Тест ДП, коли всі страви дорожчі за бюджет."""
        expensive_items = {
            "expensive1": {"cost": 100, "calories": 500},
            "expensive2": {"cost": 200, "calories": 800}
        }
        result = dynamic_programming(expensive_items, 50)
        selected, cost, calories = result
        assert len(selected) == 0
        assert cost == 0
        assert calories == 0
    
    def test_dp_zero_cost_item(self):
        """Тест ДП зі стравою з нульовою вартістю."""
        items_with_free = {
            "free": {"cost": 0, "calories": 100},
            "paid": {"cost": 20, "calories": 200}
        }
        result = dynamic_programming(items_with_free, 20)
        selected, cost, calories = result
        assert "free" in selected  # Безкоштовна страва повинна бути включена
        assert cost <= 20
    
    def test_dp_invalid_data_structure(self):
        """Тест ДП з некоректною структурою даних."""
        invalid_items = {
            "item1": {"price": 10, "calories": 100}  # Неправильне поле "price" замість "cost"
        }
        with pytest.raises(ValueError, match="некоректну структуру даних"):
            dynamic_programming(invalid_items, 50)
    
    def test_dp_negative_cost(self):
        """Тест ДП з від'ємною вартістю."""
        invalid_items = {
            "item1": {"cost": -10, "calories": 100}
        }
        with pytest.raises(ValueError, match="від'ємну вартість"):
            dynamic_programming(invalid_items, 50)
    
    def test_dp_negative_calories(self):
        """Тест ДП з від'ємною калорійністю."""
        invalid_items = {
            "item1": {"cost": 10, "calories": -100}
        }
        with pytest.raises(ValueError, match="від'ємну калорійність"):
            dynamic_programming(invalid_items, 50)
    
    def test_dp_optimality_specific_case(self):
        """Тест оптимальності ДП на конкретному прикладі."""
        # Створюємо простий набір для перевірки оптимальності
        test_items = {
            "item1": {"cost": 10, "calories": 60},  # 6 ккал/грн
            "item2": {"cost": 20, "calories": 100},  # 5 ккал/грн
            "item3": {"cost": 15, "calories": 80}   # ~5.33 ккал/грн
        }
        budget = 25
        
        # Оптимальне рішення: item1 (10) + item3 (15) = 25, калорії = 140
        # Жадібний вибір: item1 (10) + item2 (20) = 30 > 25, тому тільки item1 = 60 ккал
        # Або: item1 (10) + item3 (15) = 25, калорії = 140
        
        result = dynamic_programming(test_items, budget)
        selected, cost, calories = result
        
        assert cost <= budget
        # Перевіряємо, що знайдено оптимальне рішення (має бути 140 ккал)
        assert calories == 140, f"Очікувалось 140 ккал, отримано {calories}"

