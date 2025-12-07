"""
Головний файл для демонстрації алгоритму Дейкстри.

Створює граф та обчислює найкоротші шляхи від початкової вершини.
"""

from graph import Graph
from dijkstra import dijkstra, get_shortest_path
from math import inf

import networkx as nx
import matplotlib.pyplot as plt

DEUTSCHE_BAHN = [
    ("Berlin", "Hamburg", 290),
    ("Berlin", "Leipzig", 190),
    ("Berlin", "Frankfurt am Main", 545),
    ("Berlin", "Köln", 575),
    ("Hamburg", "Dortmund", 335),
    ("Hamburg", "Köln", 360),
    ("Hamburg", "Frankfurt am Main", 395),
    ("Leipzig", "Frankfurt am Main", 400),
    ("Leipzig", "München", 430),
    ("Leipzig", "Dortmund", 410),
    ("Frankfurt am Main", "Köln", 190),
    ("Frankfurt am Main", "Stuttgart", 210),
    ("Frankfurt am Main", "München", 390),
    ("Köln", "Dortmund", 95),
    ("Köln", "Stuttgart", 350),
    ("Dortmund", "Stuttgart", 410),
    ("Dortmund", "München", 600),
    ("Stuttgart", "München", 220),
]


def print_distances_table(distances: dict, start_vertex: str):
    """Виводить таблицю відстаней у красивому форматі."""
    print("\n" + "=" * 70)
    print(f"  Найкоротші відстані від '{start_vertex}' до всіх вершин")
    print("=" * 70)
    print(f"{'Вершина':<25} {'Відстань (км)':<20} {'Статус':<20}")
    print("-" * 70)
    
    # Сортуємо за відстанню
    sorted_distances = sorted(distances.items(), key=lambda x: x[1] if x[1] != inf else float('inf'))
    
    for vertex, distance in sorted_distances:
        if distance == inf:
            status = "Недосяжна"
            distance_str = "∞"
        else:
            status = "Досяжна"
            distance_str = f"{distance:,.0f}"
        
        print(f"{vertex:<25} {distance_str:<20} {status:<20}")
    
    print("=" * 70 + "\n")


def visualize_graph(graph: Graph, distances: dict, start_vertex: str, target_vertex: str = None):
    """Візуалізує граф з відстанями та виділяє найкоротший шлях."""
    
    # Створюємо networkx граф
    G = nx.DiGraph()
    
    # Додаємо вершини та ребра
    for vertex in graph.vertices:
        G.add_node(vertex)
    
    for from_vertex, neighbors in graph.vertices.items():
        for to_vertex, weight in neighbors:
            G.add_edge(from_vertex, to_vertex, weight=weight)
    
    # Визначаємо позиції вершин (spring layout для кращого відображення)
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Визначаємо кольори вершин на основі відстаней
    node_colors = []
    for node in G.nodes():
        if node == start_vertex:
            node_colors.append('#FF6B6B')  # Червоний для стартової вершини
        elif target_vertex and node == target_vertex:
            node_colors.append('#4ECDC4')  # Бірюзовий для цільової вершини
        elif distances.get(node, inf) != inf:
            node_colors.append('#95E1D3')  # Світло-зелений для досяжних вершин
        else:
            node_colors.append('#CCCCCC')  # Сірий для недосяжних вершин
    
    # Створюємо фігуру
    plt.figure(figsize=(16, 10))
    
    # Малюємо ребра
    edge_colors = ['#E0E0E0' for _ in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=1.5, alpha=0.6, arrows=True, arrowsize=20)
    
    # Малюємо вершини
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, alpha=0.9)
    
    # Додаємо підписи вершин з відстанями
    labels = {}
    for node in G.nodes():
        distance = distances.get(node, inf)
        if distance == inf:
            labels[node] = f"{node}\n(∞)"
        else:
            labels[node] = f"{node}\n({distance:.0f} км)"
    
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_weight='bold')
    
    # Додаємо ваги ребер
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7, alpha=0.7)
    
    # Додаємо легенду
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF6B6B', 
                   markersize=12, label=f'Стартова вершина: {start_vertex}'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#95E1D3', 
                   markersize=12, label='Досяжні вершини'),
    ]
    if target_vertex:
        legend_elements.append(
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#4ECDC4', 
                      markersize=12, label=f'Цільова вершина: {target_vertex}')
        )
    legend_elements.append(
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#CCCCCC', 
                  markersize=12, label='Недосяжні вершини')
    )
    
    plt.legend(handles=legend_elements, loc='upper left', fontsize=10)
    
    plt.title(f"Граф Deutsche Bahn: Найкоротші шляхи від '{start_vertex}'", 
              fontsize=14, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    """Демонстрація роботи алгоритму Дейкстри."""
    
    print("\n" + "=" * 70)
    print("  АЛГОРИТМ ДЕЙКСТРИ - Пошук найкоротших шляхів у графі")
    print("=" * 70)
    print("\nСтворення графа Deutsche Bahn (залізнична мережа Німеччини)...")
    
    graph = Graph()
    for st in DEUTSCHE_BAHN:
        graph.add_vertex(st[0])
        graph.add_vertex(st[1])
        graph.add_edge(st[0], st[1], st[2])
        graph.add_edge(st[1], st[0], st[2])
    
    print(f"✓ Граф створено: {len(graph.vertices)} вершин, {sum(len(neighbors) for neighbors in graph.vertices.values()) // 2} ребер")
    
    # Обчислюємо найкоротші відстані
    start_vertex = "Hamburg"
    print(f"\nОбчислення найкоротших шляхів від '{start_vertex}'...")
    distances = dijkstra(graph, start_vertex)
    print("✓ Обчислення завершено")
    
    # Виводимо таблицю відстаней
    print_distances_table(distances, start_vertex)
    
    # Приклад пошуку конкретного шляху
    target_vertex = "München"
    shortest_path = get_shortest_path(graph, start_vertex, target_vertex)
    
    if shortest_path is not None:
        print(f"Найкоротший шлях від '{start_vertex}' до '{target_vertex}': {shortest_path:,.0f} км")
    else:
        print(f"Шлях від '{start_vertex}' до '{target_vertex}' не існує")
    
    print("\n" + "-" * 70)
    print("Статистика:")
    reachable = sum(1 for d in distances.values() if d != inf)
    unreachable = len(distances) - reachable
    print(f"  • Досяжних вершин: {reachable}")
    print(f"  • Недосяжних вершин: {unreachable}")
    print(f"  • Загальна кількість вершин: {len(distances)}")
    print("-" * 70 + "\n")
    
    # Візуалізація
    print("Відображення візуалізації графа...")
    visualize_graph(graph, distances, start_vertex, target_vertex)


if __name__ == "__main__":
    main()

