"""
Візуалізація обходу бінарного дерева з кольоровим кодуванням.

Базується на коді з завдання 4 для побудови бінарних дерев.
"""

import networkx as nx
import matplotlib.pyplot as plt
try:
    from .binary_tree import Node
except ImportError:
    from binary_tree import Node


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


def draw_tree(tree_root: Node, title: str = "Binary Tree"):
    """
    Візуалізує бінарне дерево з кольоровим кодуванням.
    
    Args:
        tree_root: Корінь дерева
        title: Заголовок графіку
    """
    if tree_root is None:
        print("Дерево порожнє")
        return
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

