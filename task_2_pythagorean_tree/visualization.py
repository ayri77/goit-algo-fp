"""
Візуалізація фрактала "дерево Піфагора" за допомогою matplotlib та turtle.

Містить функції для відображення фрактала на графіку.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import turtle
import numpy as np


def _find_square_connections(
    square_geometries: list[tuple[tuple[float, float], tuple[float, float], ...]],
    squares: list[tuple[float, float, float, float, float]],
    threshold_factor: float = 0.5
) -> list[tuple[int, int]]:
    """
    Знаходить з'єднання між квадратами (батьківський -> дочірній).
    
    Args:
        square_geometries: Список кортежів (bottom_mid, top_mid, ...) для кожного квадрата.
                          Може містити 2 або 3 елементи (для turtle або matplotlib).
        squares: Список кортежів (x1, y1, x2, y2, size) для кожного квадрата
        threshold_factor: Коефіцієнт для визначення порогу відстані (за замовчуванням: 0.5)
        
    Returns:
        Список кортежів (parent_idx, child_idx) для з'єднань
    """
    connections = []
    for i, geometry in enumerate(square_geometries):
        _, parent_top = geometry[0], geometry[1]
        parent_top_x, parent_top_y = parent_top
        parent_size = squares[i][4]
        
        for j, child_geometry in enumerate(square_geometries):
            if i >= j:  # Перевіряємо тільки для наступних квадратів (дочірні завжди пізніше)
                continue
            
            child_bottom = child_geometry[0]
            child_bottom_x, child_bottom_y = child_bottom
            # Перевіряємо відстань (з урахуванням помилок округлення)
            distance = math.hypot(child_bottom_x - parent_top_x, child_bottom_y - parent_top_y)
            
            # Поріг залежить від розміру батьківського квадрата
            threshold = parent_size * threshold_factor
            if distance < threshold:
                connections.append((i, j))
    
    return connections


def _get_square_geometry(x1: float, y1: float, x2: float, y2: float, size: float):
    """
    Обчислює геометрію квадрата на основі координат основи.
    
    Args:
        x1, y1: Початок нижньої сторони
        x2, y2: Кінець нижньої сторони
        size: Розмір квадрата
        
    Returns:
        Кортеж (bottom_mid, top_mid, vertices), де:
        - bottom_mid: (x, y) - середина нижньої сторони
        - top_mid: (x, y) - середина верхньої сторони
        - vertices: список вершин квадрата [(x1, y1), (x2, y2), (top_x2, top_y2), (top_x1, top_y1)]
    """
    # Нормалізуємо вектор напрямку нижньої сторони
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    
    if length == 0:
        return None, None, None
    
    dx /= length
    dy /= length
    
    # Перпендикулярний вектор для верхньої сторони
    perp_dx = -dy
    perp_dy = dx
    
    # Середина нижньої сторони
    bottom_mid = ((x1 + x2) / 2, (y1 + y2) / 2)
    
    # Координати верхньої сторони
    top_x1 = x1 + perp_dx * size
    top_y1 = y1 + perp_dy * size
    top_x2 = x2 + perp_dx * size
    top_y2 = y2 + perp_dy * size
    
    # Середина верхньої сторони
    top_mid = ((top_x1 + top_x2) / 2, (top_y1 + top_y2) / 2)
    
    # Вершини квадрата
    vertices = [
        (x1, y1),
        (x2, y2),
        (top_x2, top_y2),
        (top_x1, top_y1)
    ]
    
    return bottom_mid, top_mid, vertices


def draw_pythagorean_tree(
    squares: list[tuple[float, float, float, float, float]],
    level: int | None = None,
    size: float = 100,
    angle: float = 45,
    mode: str = 'tree'
) -> None:
    """
    Візуалізує фрактал "дерево Піфагора" на основі обчислених координат квадратів.
    
    Args:
        squares: Список кортежів (x1, y1, x2, y2, size) для кожного квадрата
        level: Рівень рекурсії (опціонально, для інформації)
        size: Розмір початкового квадрата (опціонально, для інформації)
        angle: Кут розгалуження (опціонально, для інформації)
        mode: Режим візуалізації - 'tree' (лінії дерева) або 'squares' (всі квадрати для перевірки)
        
    Примітка:
        Кожен квадрат представлений як (x1, y1, x2, y2, size), де:
        - (x1, y1) - початок нижньої сторони квадрата
        - (x2, y2) - кінець нижньої сторони квадрата
        - size - розмір квадрата
    """
    if not squares:
        print("Попередження: немає квадратів для відображення.")
        return
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Знаходимо межі для правильного масштабування
    all_x = []
    all_y = []
    
    if mode == 'squares':
        # Режим перевірки - малюємо всі квадрати для перевірки координат
        for square in squares:
            x1, y1, x2, y2, square_size = square
            bottom_mid, top_mid, vertices = _get_square_geometry(x1, y1, x2, y2, square_size)
            
            if vertices is None:
                continue
            
            # Збираємо координати для меж
            for vx, vy in vertices:
                all_x.append(vx)
                all_y.append(vy)
            
            # Малюємо квадрат
            square_poly = patches.Polygon(
                vertices,
                closed=True,
                edgecolor='black',
                facecolor='lightblue',
                linewidth=1,
                alpha=0.5
            )
            ax.add_patch(square_poly)
            
    elif mode == 'tree':
        # Режим "дерева" - малюємо лінії скелета дерева
        # З'єднуємо: середина нижньої сторони -> середина верхньої сторони (всередині квадрата)
        # Та: середина верхньої сторони батьківського -> середина нижньої сторони дочірнього (між квадратами)
        
        # Обчислюємо геометрію для всіх квадратів
        square_geometries = []
        for square in squares:
            x1, y1, x2, y2, square_size = square
            bottom_mid, top_mid, vertices = _get_square_geometry(x1, y1, x2, y2, square_size)
            if bottom_mid and top_mid:
                square_geometries.append((bottom_mid, top_mid, vertices))
        
        # Знаходимо з'єднання між квадратами
        connections = _find_square_connections(square_geometries, squares)
        
        # Малюємо лінії дерева
        for i, (bottom_mid, top_mid, vertices) in enumerate(square_geometries):
            bottom_x, bottom_y = bottom_mid
            top_x, top_y = top_mid
            
            # Лінія всередині квадрата: середина нижньої -> середина верхньої
            ax.plot([bottom_x, top_x], [bottom_y, top_y], 
                   '-', linewidth=1.5, color='darkred')
            
            # Лінії між квадратами: верхня сторона батьківського -> нижня сторона дочірнього
            for parent_idx, child_idx in connections:
                if parent_idx == i:
                    child_bottom, _, _ = square_geometries[child_idx]
                    child_bottom_x, child_bottom_y = child_bottom
                    ax.plot([top_x, child_bottom_x], [top_y, child_bottom_y], 
                           '-', linewidth=1.5, color='darkred')
            
            # Збираємо координати для меж
            if vertices:
                for vx, vy in vertices:
                    all_x.append(vx)
                    all_y.append(vy)
            all_x.extend([bottom_x, top_x])
            all_y.extend([bottom_y, top_y])
    
    # Встановлюємо межі з невеликим відступом
    if all_x and all_y:
        margin = max(max(all_x) - min(all_x), max(all_y) - min(all_y)) * 0.1
        ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
        ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    
    # Додаємо заголовок з інформацією
    title_parts = [f"Дерево Піфагора"]
    if level is not None:
        title_parts.append(f"Рівень: {level}")
    title_parts.append(f"Квадратів: {len(squares)}")
    title_parts.append(f"Режим: {mode}")
    ax.set_title(" | ".join(title_parts), fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.show()


def draw_pythagorean_tree_turtle(
    squares: list[tuple[float, float, float, float, float]],
    level: int | None = None,
    size: float = 100,
    angle: float = 45,
    mode: str = 'squares',
    speed: int = 5,
    start_position: tuple[float, float] | None = None
) -> None:
    """
    Візуалізує фрактал "дерево Піфагора" за допомогою turtle.
    
    Для режиму 'squares' - використовує рекурсивну побудову, як у temp.py.
    Для режиму 'tree' - використовує координати з calculate_pythagorean_tree.
    
    Args:
        squares: Список кортежів (x1, y1, x2, y2, size) - використовується для режиму 'tree'
        level: Рівень рекурсії (максимальна глибина)
        size: Розмір початкового квадрата
        angle: Кут розгалуження (в градусах)
        mode: Режим візуалізації - 'squares' (квадрати + трикутники) або 'tree' (лінії дерева)
        speed: Швидкість малювання (0-100, де 0 - найшвидше)
        start_position: Початкова позиція turtle (x, y), якщо None - автоматично
    """
    # Налаштування turtle
    turtle.speed(speed)
    turtle.penup()
    turtle.hideturtle()
    turtle.bgcolor("white")
    
    if mode == 'tree':
        # Режим "дерева" - використовуємо координати з calculate_pythagorean_tree
        if not squares:
            print("Попередження: немає квадратів для відображення.")
            return
        
        # Обчислюємо геометрію для всіх квадратів
        square_geometries = []
        for square in squares:
            x1, y1, x2, y2, square_size = square
            bottom_mid, top_mid, _ = _get_square_geometry(x1, y1, x2, y2, square_size)
            if bottom_mid and top_mid:
                square_geometries.append((bottom_mid, top_mid))
        
        # Знаходимо з'єднання між квадратами
        connections = _find_square_connections(square_geometries, squares)
        
        # Малюємо лінії дерева
        turtle.color("darkred")
        turtle.pensize(2)
        
        for i, (bottom_mid, top_mid) in enumerate(square_geometries):
            bottom_x, bottom_y = bottom_mid
            top_x, top_y = top_mid
            
            # Лінія всередині квадрата
            turtle.penup()
            turtle.goto(bottom_x, bottom_y)
            turtle.pendown()
            turtle.goto(top_x, top_y)
            turtle.penup()
            
            # Лінії між квадратами
            for parent_idx, child_idx in connections:
                if parent_idx == i:
                    child_bottom, _ = square_geometries[child_idx]
                    child_bottom_x, child_bottom_y = child_bottom
                    
                    turtle.goto(top_x, top_y)
                    turtle.pendown()
                    turtle.goto(child_bottom_x, child_bottom_y)
                    turtle.penup()
        
        turtle.done()
        
    else:  # mode == 'squares'
        # Режим "квадратів" - рекурсивна побудова як у temp.py
        # Визначаємо початкову позицію
        if start_position is None:
            start_position = (0, -300)  # Як у temp.py
        
        # Переходимо до початкової позиції
        turtle.goto(start_position[0], start_position[1])
        turtle.setheading(0)  # Направляємо вправо (як у temp.py)
        
        # Рекурсивно малюємо дерево
        if level is None:
            level = 3  # За замовчуванням
        
        _draw_tree_recursive_turtle(size, level, mode, angle, max_depth=level)
        
        # Повертаємося до початкової позиції
        turtle.penup()
        turtle.goto(start_position[0], start_position[1])
        
        # Завершуємо
        turtle.done()


def _draw_tree_recursive_turtle(
    s: float,
    depth: int,
    mode: str = 'squares',
    angle: float = 45,
    max_depth: int | None = None
) -> None:
    """
    Рекурсивна функція для малювання дерева через turtle.
    
    Працює як у temp.py - малює квадрати та трикутники.
    
    Args:
        s: Розмір поточного квадрата
        depth: Глибина рекурсії (залишилося рівнів)
        mode: 'squares' (квадрати + трикутники, як у temp.py)
        angle: Кут розгалуження (в градусах)
        max_depth: Максимальна глибина (для визначення рівня вкладеності)
    """
    if depth == 0:
        return
    
    if max_depth is None:
        max_depth = depth
    
    # Визначаємо поточний рівень вкладеності
    current_level = max_depth - depth
    
    # Режим "квадратів" - квадрати + трикутники (як у temp.py)
    # Визначаємо, чи робити заливку (не робимо для маленьких квадратів)
    no_fill = current_level > 4
    
    # Малюємо квадрат
    _draw_square_turtle_recursive(s, "red", fill=not no_fill)
    
    # Малюємо трикутник
    _draw_triangle_turtle_recursive(s, "blue", fill=not no_fill)
    
    # Обчислюємо розмір дочірнього квадрата
    s_child = s / math.sqrt(2)
    
    # Ліва гілка (як у temp.py)
    pos = turtle.position()
    ang = turtle.heading()
    
    turtle.left(angle)
    turtle.forward(s / (2 * math.sqrt(2)))
    turtle.right(90)
    _draw_tree_recursive_turtle(s_child, depth - 1, mode, angle, max_depth)
    
    # Повертаємося до початкової позиції
    turtle.penup()
    turtle.setposition(pos)
    turtle.setheading(ang)
    
    # Права гілка (як у temp.py)
    turtle.left(90 + angle)
    turtle.forward(s / (2 * math.sqrt(2)))
    turtle.right(90)
    _draw_tree_recursive_turtle(s_child, depth - 1, mode, angle, max_depth)


def _draw_square_turtle_recursive(size: float, color: str, fill: bool = True) -> None:
    """
    Допоміжна функція для малювання квадрата через turtle (рекурсивний режим).
    
    Як у temp.py - після малювання turtle залишається на верхній стороні.
    
    Args:
        size: Розмір квадрата
        color: Колір для малювання
        fill: Чи робити заливку (True) або тільки контур (False)
    """
    turtle.pendown()
    
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    else:
        turtle.color(color)
        turtle.pensize(1)
    
    turtle.forward(size / 2)  # права половина нижньої сторони
    turtle.left(90)
    turtle.forward(size)  # права сторона
    turtle.left(90)
    turtle.forward(size)  # верхня сторона
    turtle.left(90)
    turtle.forward(size)  # ліва сторона
    turtle.left(90)
    turtle.forward(size / 2)  # ліва половина нижньої сторони
    
    if fill:
        turtle.end_fill()
    
    turtle.penup()
    
    # Переходимо до верхньої сторони (як у temp.py)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)


def _draw_triangle_turtle_recursive(size: float, color: str, fill: bool = True) -> None:
    """
    Допоміжна функція для малювання трикутника через turtle (рекурсивний режим).
    
    Як у temp.py - малює трикутник, коли turtle знаходиться на верхній стороні квадрата.
    
    Args:
        size: Розмір трикутника
        color: Колір для малювання
        fill: Чи робити заливку (True) або тільки контур (False)
    """
    turtle.pendown()
    
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    else:
        turtle.color(color)
        turtle.pensize(1)
    
    turtle.forward(size / 2)  # права половина нижньої сторони
    turtle.left(180 - 45)
    turtle.forward(size / np.sqrt(2))  # права сторона
    turtle.left(180 - 90)
    turtle.forward(size / np.sqrt(2))  # ліва сторона
    turtle.left(180 - 45)
    turtle.forward(size / 2)  # ліва половина нижньої сторони
    
    if fill:
        turtle.end_fill()
    
    turtle.penup()