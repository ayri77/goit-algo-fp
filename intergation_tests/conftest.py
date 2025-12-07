"""
Спільні фікстури для всіх тестів.

Містить фікстури, які можуть бути використані в тестах для різних завдань.
"""

import pytest


@pytest.fixture
def sample_linked_list_data():
    """Фікстура з тестовими даними для однозв'язного списку."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_graph_data():
    """Фікстура з тестовими даними для графа."""
    return {
        'vertices': ['A', 'B', 'C', 'D'],
        'edges': [
            ('A', 'B', 1.0),
            ('B', 'C', 2.0),
            ('C', 'D', 3.0),
            ('A', 'D', 5.0),
        ]
    }


@pytest.fixture
def sample_tree_data():
    """Фікстура з тестовими даними для дерева."""
    return {
        'root_val': 0,
        'left_val': 4,
        'right_val': 1,
        'left_left_val': 5,
        'left_right_val': 10,
        'right_left_val': 3,
    }


@pytest.fixture
def sample_food_items():
    """Фікстура з тестовими даними про їжу."""
    return {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

