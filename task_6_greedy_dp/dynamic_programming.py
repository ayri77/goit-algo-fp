"""
Алгоритм динамічного програмування для вибору їжі.

Обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""

from typing import Dict, List, Tuple

def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    """
    Алгоритм динамічного програмування для вибору їжі.
    
    Обчислює оптимальний набір страв для максимізації калорійності
    при заданому бюджеті.
    
    Args:
        items: Словник з даними про їжу {назва: {"cost": вартість, "calories": калорії}}
        budget: Доступний бюджет
        
    Returns:
        Кортеж (список назв вибраних страв, загальна вартість, загальна калорійність)
        
    Примітка:
        Використовується підхід задачі про рюкзак (knapsack problem).
        Створіть таблицю DP[b][i], де:
        - b - бюджет (від 0 до budget)
        - i - індекс страви
        - DP[b][i] - максимальна калорійність при бюджеті b з використанням перших i страв
        
        Після заповнення таблиці, відстежте оптимальний набір страв.
    """
    # Валідація вхідних даних
    if not items:
        return [], 0, 0
    
    if budget < 0:
        return [], 0, 0
    
    # Для нульового бюджету перевіряємо, чи є безкоштовні страви
    if budget == 0:
        free_items = [(name, data) for name, data in items.items() if data["cost"] == 0]
        if free_items:
            selected = [name for name, _ in free_items]
            calories = sum(data["calories"] for _, data in free_items)
            return selected, 0, calories
        return [], 0, 0
    
    # Перевірка коректності даних про страви
    for name, data in items.items():
        if "cost" not in data or "calories" not in data:
            raise ValueError(f"Страва '{name}' має некоректну структуру даних")
        if data["cost"] < 0:
            raise ValueError(f"Страва '{name}' має від'ємну вартість: {data['cost']}")
        if data["calories"] < 0:
            raise ValueError(f"Страва '{name}' має від'ємну калорійність: {data['calories']}")
   
    # Розділяємо страви на безкоштовні (cost == 0) та платні
    free_items = []
    paid_items = []
    
    for name, data in items.items():
        if data["cost"] == 0:
            free_items.append((name, data))
        else:
            paid_items.append((name, data))
    
    # Додаємо всі безкоштовні страви (вони не витрачають бюджет)
    selected_items = [name for name, _ in free_items]
    total_calories_from_free = sum(data["calories"] for _, data in free_items)
    
    # Якщо немає платних страв, повертаємо тільки безкоштовні
    if not paid_items:
        total_cost = 0
        total_calories = total_calories_from_free
        return selected_items, total_cost, total_calories
    
    # Працюємо тільки з платними стравами
    items_list = paid_items
    n = len(items_list)
    
    # створюємо таблицю DP розміром (budget + 1) x (кількість страв + 1)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # заповнюємо таблицю: для кожної страви та кожного бюджету
    # обчислюємо максимальну калорійність
    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            if items_list[i-1][1]["cost"] <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - items_list[i-1][1]["cost"]] + items_list[i-1][1]["calories"])
            else:
                # Якщо страва дорожча за бюджет, просто копіюємо значення з попереднього рядка
                dp[i][b] = dp[i-1][b]
    
    # відстежуємо оптимальний набір платних страв
    paid_selected = []
    b = budget
    for i in range(n, 0, -1):
        item_cost = items_list[i-1][1]["cost"]
        item_calories = items_list[i-1][1]["calories"]
        
        # Перевіряємо, чи була використана ця страва в оптимальному рішенні
        if item_cost <= b and dp[i][b] == dp[i-1][b - item_cost] + item_calories:
            paid_selected.append(items_list[i-1][0])
            b -= item_cost
    
    # Додаємо вибрані платні страви до списку
    selected_items.extend(paid_selected)
    
    # рахуємо загальну вартість та калорійність
    total_cost = sum(items[item]["cost"] for item in paid_selected)
    total_calories = total_calories_from_free + sum(items[item]["calories"] for item in paid_selected)
    
    return selected_items, total_cost, total_calories

