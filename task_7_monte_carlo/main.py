"""
Головний файл для демонстрації методу Монте-Карло.

Симулює кидки кубиків, обчислює ймовірності та порівнює з аналітичними розрахунками.
"""

from monte_carlo import monte_carlo_simulation, analytical_probabilities
from visualization import create_probability_table, plot_probabilities, print_probability_table


def main():
    """Демонстрація методу Монте-Карло для кидків кубиків."""
    
    num_rolls = 100000
    print(f"Виконується симуляція {num_rolls} кидків...")
    mc_probs = monte_carlo_simulation(num_rolls)
    anal_probs = analytical_probabilities()
    
    df = create_probability_table(mc_probs, anal_probs)
    print_probability_table(df)
    
    plot_probabilities(mc_probs, anal_probs)
    
    print("\nВисновки:")
    print("Метод Монте-Карло дає результати, близькі до аналітичних розрахунків.")
    print("Збільшення кількості симуляцій покращує точність результатів.")
    


if __name__ == "__main__":
    main()

