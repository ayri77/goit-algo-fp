"""
Симуляція кидків двох кубиків методом Монте-Карло.

Обчислює суми чисел та ймовірності кожної можливої суми.
"""

import random
from typing import Dict
from collections import Counter


def roll_dice() -> int:
    """
    Симулює кидок одного кубика.
    
    Returns:
        Випадкове число від 1 до 6
    """
    return random.randint(1, 6)


def roll_two_dice() -> int:
    """
    Симулює кидок двох кубиків.
    
    Returns:
        Сума чисел на обох кубиках (від 2 до 12)
    """
    return roll_dice() + roll_dice()


def monte_carlo_simulation(num_rolls: int = 100000) -> Dict[int, float]:
    """
    Виконує симуляцію великої кількості кидків двох кубиків.
    
    Args:
        num_rolls: Кількість кидків для симуляції (за замовчуванням 100000)
        
    Returns:
        Словник {сума: ймовірність} для сум від 2 до 12
        
    Примітка:
        Функція повинна:
        1. Симулювати num_rolls кидків двох кубиків
        2. Підрахувати, скільки разів кожна можлива сума (2-12) з'являється
        3. Обчислити ймовірність кожної суми (кількість / загальна кількість)
    """
    
    sums_counter = Counter()
    for _ in range(num_rolls):
        sums_counter[roll_two_dice()] += 1

    
    probabilities = {}
    for sum, count in sums_counter.items():
        probabilities[sum] = count / num_rolls
    
    return probabilities


def analytical_probabilities() -> Dict[int, float]:
    """
    Обчислює аналітичні ймовірності сум при киданні двох кубиків.
    
    Returns:
        Словник {сума: ймовірність} для сум від 2 до 12
        
    Примітка:
        Аналітичні ймовірності:
        Сума 2: 1/36
        Сума 3: 2/36
        Сума 4: 3/36
        Сума 5: 4/36
        Сума 6: 5/36
        Сума 7: 6/36
        Сума 8: 5/36
        Сума 9: 4/36
        Сума 10: 3/36
        Сума 11: 2/36
        Сума 12: 1/36
    """
    total_outcomes = 36
    analytical = {
        2: 1 / total_outcomes,
        3: 2 / total_outcomes,
        4: 3 / total_outcomes,
        5: 4 / total_outcomes,
        6: 5 / total_outcomes,
        7: 6 / total_outcomes,
        8: 5 / total_outcomes,
        9: 4 / total_outcomes,
        10: 3 / total_outcomes,
        11: 2 / total_outcomes,
        12: 1 / total_outcomes,
    }
    return analytical

