"""
Головний файл для демонстрації фрактала "дерево Піфагора".

Відповідає за оркестрацію процесу: отримання параметрів, обчислення координат
та візуалізацію фрактала.
"""

import sys
from arguments import ParametersProcessor
from visualization import draw_pythagorean_tree, draw_pythagorean_tree_turtle
from fractal import calculate_pythagorean_tree

def main() -> None:
    """
    Головна функція для запуску програми.
    
    Оркеструє процес: отримання параметрів, обчислення координат та візуалізацію.
    
    Підтримує два режими:
    1. Через аргументи командного рядка: python main.py --level 5
    2. Інтерактивний режим: python main.py (запитує параметри у користувача)
    """
    # Обробка параметрів через окремий модуль
    processor = ParametersProcessor()
    params = processor.process()
    
    # Виведення інформації про параметри
    print(f"\n{'=' * 60}")
    print(f"Побудова дерева Піфагора з параметрами:")
    print(f"{'=' * 60}")
    print(f"  Рівень рекурсії: {params['level']}")
    print(f"  Розмір початкового квадрата: {params['size']}")
    print(f"  Кут розгалуження: {params['angle']}°")
    print(f"  Початкова позиція: ({params['start_x']}, {params['start_y']})")
    print(f"  Візуалізація: {params['visualization']}")
    print(f"  Режим: {params['mode']}")
    if params['visualization'] == 'turtle':
        print(f"  Швидкість turtle: {params['turtle_speed']}")
    print(f"{'=' * 60}\n")
    
    # Обчислюємо координати квадратів
    # Початковий квадрат: горизонтальна лінія від (start_x, start_y) до (start_x + size, start_y)
    x1 = params['start_x']
    y1 = params['start_y']
    x2 = params['start_x'] + params['size']
    y2 = params['start_y']
    
    squares = calculate_pythagorean_tree(x1, y1, x2, y2, 0, params['level'], params['angle'])
    
    print(f"Обчислено {len(squares)} квадратів.")
    print("Відображення візуалізації...\n")
    
    # Візуалізуємо фрактал
    if params['visualization'] == 'turtle':
        # Для turtle використовуємо початкову позицію
        start_pos = (params['start_x'], params['start_y'] - 50)  # Трохи нижче для кращого відображення
        draw_pythagorean_tree_turtle(
            squares, 
            params['level'], 
            params['size'], 
            params['angle'],
            mode=params['mode'],
            speed=params['turtle_speed'],
            start_position=start_pos
        )
    else:
        # Для matplotlib передаємо режим
        draw_pythagorean_tree(squares, params['level'], params['size'], params['angle'], mode=params['mode'])


if __name__ == "__main__":
    main()

