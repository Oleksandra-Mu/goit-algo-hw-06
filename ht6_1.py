import networkx as nx
import matplotlib.pyplot as plt
import json

# Створюємо випадковий граф
G = nx.gnm_random_graph(7, 16)

# Зберігаємо граф у файл у форматі JSON
with open('random_graph.json', 'w') as f:
    json.dump(nx.node_link_data(G), f)

# Читаємо граф з файлу
with open('random_graph.json', 'r') as f:
    G_loaded = nx.node_link_graph(json.load(f))

def analyze_graph(G):
    print("Кількість вузлів:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    print("Зв'язний граф:", nx.is_connected(G))
    if nx.is_connected(G):
        print("Діаметр графа:", nx.diameter(G))
    print("Ступінь центральності:", nx.degree_centrality(G))
    print("Ступінь близкості вузла:", nx.closeness_centrality(G))
    print("Посередництво вузла:", nx.betweenness_centrality(G)) 
    print("Середня довжина шляху в графі:", nx.average_shortest_path_length(G))
    print("Середній ступінь вузла:", sum(dict(G.degree()).values()) / G.number_of_nodes())
    print("Щільність графа:", nx.density(G))
    print("Кількість зв'язних компонентів:", nx.number_connected_components(G))

# Візуалізація
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

# Виклик функції
analyze_graph(G)