import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from colour import Color
from collections import deque

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, font_color='white', labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# *********************************************************************************************************************

heap = []

def preorder_traversal(root):
    if root:
        heap.append(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

preorder_traversal(root)
heapq.heapify(heap)

def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(value) for value in heap]

    for i in range(len(heap)):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(heap):
            nodes[i].left = nodes[left_i]

        if right_i < len(heap):
            nodes[i].right = nodes[right_i]

    return nodes[0]


def colors_for_nodes(order, color="#1296F0"):
    base = Color(color)

    colors = []
    
    for i in range(len(order)):
        c = Color(base.hex)
        c.luminance = 0.1 + i * 0.08
        colors.append(c.hex)

    for i, node in enumerate(order):
        node.color = colors[i]


root2 = build_heap_tree(heap)

def dfs(root):
    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order

def bfs(root):
    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order

draw_tree(root2)
dfs_order = dfs(root2)
colors_for_nodes(dfs_order)
draw_tree(root2)
bfs_order = bfs(root2)
colors_for_nodes(bfs_order)
draw_tree(root2)

# ***********************************************************************************************************
# Відображення дерева
# draw_tree(root)