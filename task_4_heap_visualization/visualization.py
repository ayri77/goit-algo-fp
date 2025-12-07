"""
Візуалізація бінарної купи за допомогою networkx та matplotlib.

Базується на коді з завдання для побудови бінарних дерев.
"""

import networkx as nx
import matplotlib.pyplot as plt
try:
    from .binary_heap import Node
except ImportError:
    from binary_heap import Node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає ребра та вузли до графа для візуалізації.
    
    Args:
        graph: Граф networkx
        node: Поточний вузол дерева
        pos: Словник позицій вузлів
        x: Поточна x-координата
        y: Поточна y-координата
        layer: Поточний рівень дерева
        
    Returns:
        Оновлений граф
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root: Node):
    """
    Візуалізує бінарну купу.
    
    Args:
        heap_root: Корінь дерева купи (Node)
        
    Примітка:
        Функція повинна відображати структуру купи з мітками значень вузлів.
    """
    if heap_root is None:
        print("Купа порожня")
        return
    
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(tree, heap_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

