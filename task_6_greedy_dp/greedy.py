"""
Жадібний алгоритм для вибору їжі з максимізацією калорійності.

Алгоритм вибирає страви, максимізуючи співвідношення калорій до вартості.
"""

from typing import Dict, List, Tuple

def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    """
    Жадібний алгоритм вибору їжі з максимізацією калорійності.
    
    Алгоритм вибирає страви, максимізуючи співвідношення калорій до вартості,
    не перевищуючи заданий бюджет.
    
    Args:
        items: Словник з даними про їжу {назва: {"cost": вартість, "calories": калорії}}
        budget: Доступний бюджет
        
    Returns:
        Кортеж (список назв вибраних страв, загальна вартість, загальна калорійність)
        
    Примітка:
        Алгоритм повинен:
        1. Обчислити співвідношення калорій/вартість для кожної страви
        2. Відсортувати страви за цим співвідношенням (спадання)
        3. Вибирати страви по черзі, поки не перевищимо бюджет
    """
    # Валідація вхідних даних
    if not items:
        return [], 0, 0
    
    if budget < 0:
        return [], 0, 0
    
    if budget == 0:
        return [], 0, 0
    
    # Перевірка коректності даних про страви
    for name, data in items.items():
        if "cost" not in data or "calories" not in data:
            raise ValueError(f"Страва '{name}' має некоректну структуру даних")
        if data["cost"] < 0:
            raise ValueError(f"Страва '{name}' має від'ємну вартість: {data['cost']}")
        if data["calories"] < 0:
            raise ValueError(f"Страва '{name}' має від'ємну калорійність: {data['calories']}")

    selected_items = []
    total_cost = 0
    total_calories = 0

    items_list = list(items.items())
    # Фільтруємо страви з нульовою вартістю та обчислюємо співвідношення
    # Страви з нульовою вартістю мають нескінченне співвідношення, тому їх додаємо першими
    valid_items = []
    free_items = []
    
    for name, data in items_list:
        if data["cost"] == 0:
            # Страви з нульовою вартістю додаємо безкоштовно
            free_items.append((name, data))
        elif data["cost"] > 0:
            valid_items.append((name, data))
    
    # Додаємо безкоштовні страви
    for item in free_items:
        selected_items.append(item[0])
        total_calories += item[1]["calories"]
    
    # Рахуємо співвідношення калорій/вартість для кожної страви
    # і сортуємо від більшого до меншого
    valid_items.sort(key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    # Ітеруємо по відсортованих стравах та додаємо їх, поки є бюджет
    for item in valid_items:
        if total_cost + item[1]["cost"] <= budget:
            selected_items.append(item[0])
            total_cost += item[1]["cost"] 
            total_calories += item[1]["calories"]
    
    return selected_items, total_cost, total_calories

