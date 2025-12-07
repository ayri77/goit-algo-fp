"""
Головний файл для демонстрації жадібного алгоритму та динамічного програмування.

Порівнює результати обох підходів для задачі вибору їжі.
"""

from greedy import greedy_algorithm
from dynamic_programming import dynamic_programming

# Дані про їжу
ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def print_items_table(items: dict):
    """Виводить таблицю доступних страв."""
    print("\n" + "=" * 70)
    print("  ДОСТУПНІ СТРАВИ")
    print("=" * 70)
    print(f"{'Назва':<15} {'Вартість':<12} {'Калорії':<12} {'Калорії/Вартість':<18}")
    print("-" * 70)
    
    for name, data in sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True):
        ratio = data["calories"] / data["cost"]
        print(f"{name:<15} {data['cost']:<12} {data['calories']:<12} {ratio:.2f}")
    
    print("=" * 70)


def print_algorithm_result(title: str, result: tuple, items: dict):
    """Виводить результат роботи алгоритму."""
    selected_items, total_cost, total_calories = result
    
    print(f"\n{title}")
    print("-" * 70)
    
    if selected_items:
        print(f"Вибрані страви ({len(selected_items)}):")
        for item in selected_items:
            cost = items[item]["cost"]
            calories = items[item]["calories"]
            ratio = calories / cost
            print(f"  • {item:<15} - {cost:>3} грн, {calories:>4} ккал (ефективність: {ratio:.2f})")
        
        print(f"\nПідсумок:")
        print(f"  Загальна вартість: {total_cost} грн")
        print(f"  Загальна калорійність: {total_calories} ккал")
        if total_cost > 0:
            efficiency = total_calories / total_cost
            print(f"  Ефективність набору: {efficiency:.2f} ккал/грн")
    else:
        print("  Не вдалося вибрати страви (недостатньо бюджету)")


def print_comparison(greedy_result: tuple, dp_result: tuple):
    """Виводить порівняння результатів."""
    _, greedy_cost, greedy_calories = greedy_result
    _, dp_cost, dp_calories = dp_result
    
    print("\n" + "=" * 70)
    print("  ПОРІВНЯННЯ РЕЗУЛЬТАТІВ")
    print("=" * 70)
    
    print(f"{'Параметр':<30} {'Жадібний':<20} {'ДП':<20}")
    print("-" * 70)
    print(f"{'Калорійність':<30} {greedy_calories:<20} {dp_calories:<20}")
    print(f"{'Вартість':<30} {greedy_cost:<20} {dp_cost:<20}")
    
    if greedy_cost > 0 and dp_cost > 0:
        greedy_eff = greedy_calories / greedy_cost
        dp_eff = dp_calories / dp_cost
        print(f"{'Ефективність (ккал/грн)':<30} {greedy_eff:<20.2f} {dp_eff:<20.2f}")
    
    print("-" * 70)
    
    if dp_calories > greedy_calories:
        diff = dp_calories - greedy_calories
        print(f"\nДинамічне програмування знайшло краще рішення на {diff} ккал")
        print(f"(на {diff/greedy_calories*100:.1f}% більше калорій)")
    elif greedy_calories > dp_calories:
        diff = greedy_calories - dp_calories
        print(f"\nЖадібний алгоритм знайшов краще рішення на {diff} ккал")
        print(f"(на {diff/dp_calories*100:.1f}% більше калорій)")
    else:
        print("\nОбидва алгоритми знайшли однакове рішення")
    
    print("=" * 70 + "\n")


def main():
    """Демонстрація та порівняння алгоритмів."""
    
    print("\n" + "=" * 70)
    print("  ЖАДІБНИЙ АЛГОРИТМ ТА ДИНАМІЧНЕ ПРОГРАМУВАННЯ")
    print("  Задача вибору їжі з максимізацією калорійності")
    print("=" * 70)
    
    # Виводимо таблицю доступних страв
    print_items_table(ITEMS)
    
    # Отримуємо бюджет від користувача
    try:
        budget = int(input("\nВведіть бюджет (грн): "))
        if budget < 0:
            print("Помилка: бюджет не може бути від'ємним")
            return
    except ValueError:
        print("Помилка: введіть коректне число")
        return
    
    print(f"\nБюджет: {budget} грн")
    print("\n" + "=" * 70)
    print("  ОБЧИСЛЕННЯ РЕЗУЛЬТАТІВ")
    print("=" * 70)
    
    # Обчислюємо результати
    greedy_result = greedy_algorithm(ITEMS, budget)
    dp_result = dynamic_programming(ITEMS, budget)
    
    # Виводимо результати
    print_algorithm_result("ЖАДІБНИЙ АЛГОРИТМ", greedy_result, ITEMS)
    print_algorithm_result("ДИНАМІЧНЕ ПРОГРАМУВАННЯ", dp_result, ITEMS)
    
    # Порівнюємо результати
    print_comparison(greedy_result, dp_result)
    
    # Статистика
    print("Статистика:")
    total_items_cost = sum(item["cost"] for item in ITEMS.values())
    total_items_calories = sum(item["calories"] for item in ITEMS.values())
    print(f"  • Загальна вартість всіх страв: {total_items_cost} грн")
    print(f"  • Загальна калорійність всіх страв: {total_items_calories} ккал")
    if budget > 0:
        used_budget = max(greedy_result[1], dp_result[1])
        usage_percent = (used_budget / budget) * 100
        print(f"  • Використано бюджету: {used_budget} / {budget} грн ({usage_percent:.1f}%)")
    print()


if __name__ == "__main__":
    main()

