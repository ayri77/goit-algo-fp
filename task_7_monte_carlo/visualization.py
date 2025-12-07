"""
Візуалізація результатів методу Монте-Карло.

Створює таблиці та графіки ймовірностей сум при киданні двох кубиків.
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict


def create_probability_table(monte_carlo: Dict[int, float], analytical: Dict[int, float]) -> pd.DataFrame:
    """
    Створює таблицю з порівнянням ймовірностей.
    
    Args:
        monte_carlo: Ймовірності з методу Монte-Карло
        analytical: Аналітичні ймовірності
        
    Returns:
        DataFrame з колонками: Сума, Монте-Карло, Аналітична, Різниця
    """
    data = {
        'Сума': list(range(2, 13)),
        'Монте-Карло': [monte_carlo.get(i, 0) for i in range(2, 13)],
        'Аналітична': [analytical.get(i, 0) for i in range(2, 13)],
    }
    df = pd.DataFrame(data)
    df['Різниця'] = df['Монте-Карло'] - df['Аналітична']
    
    return df


def plot_probabilities(monte_carlo: Dict[int, float], analytical: Dict[int, float]):
    """
    Створює графік порівняння ймовірностей.
    
    Args:
        monte_carlo: Ймовірності з методу Монте-Карло
        analytical: Аналітичні ймовірності
    """
    
    sums = list(range(2, 13))
    mc_probs = [monte_carlo.get(s, 0) for s in sums]
    anal_probs = [analytical.get(s, 0) for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sums, mc_probs, 'o-', label='Монте-Карло', linewidth=2, markersize=8)
    plt.plot(sums, anal_probs, 's-', label='Аналітична', linewidth=2, markersize=8)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(sums)
    plt.show()


def print_probability_table(df: pd.DataFrame):
    """
    Виводить таблицю ймовірностей у консоль.
    
    Args:
        df: DataFrame з ймовірностями
    """
    print("\nТаблиця ймовірностей сум при киданні двох кубиків:")
    print("=" * 60)
    print(df.to_string(index=False))
    print("=" * 60)

