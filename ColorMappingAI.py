## Visualization

# Importations
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import anything

# Parameters
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'),('A', 'C'),('B', 'C'),('C', 'D'),('D', 'F'),('D', 'E'),('E', 'F')]


# Create the corresponding graph
G = nx.Graph()
G.add_nodes_from(nodes, color='white') # White is considered as a non-affected color propriety
G.add_edges_from(edges)

# Plot the graph
nx.draw(G, with_labels = True, node_color='white', node_size=800)# initial graph
plt.show()


## Color attributions
color = np.random.choice(['red','green','blue'], size=len(G.nodes))

nx.set_node_attributes(G, dict(zip(G.nodes(), color)), 'color')
nx.draw(G, with_labels = True, node_size=800, node_color=color)
plt.show()

#G.nodes['A']['color'] = 'red'



## Resolving functions


def Find_More_Constraint():
    maximum = 0
    winner = 0
    for node in G.nodes():
        count = len(G.edges(node)) # Number of edges corresponding to the node
        if maximum < count:
            maximum = count
            winner = node
    return winner

def Find_Possibilities(node):
    possibilities = ['red', 'green', 'blue']

    for border in G.edges(node):
        node, neighbour = border
        usedColor = G.nodes[neighbour]['color']
        if usedColor != 'white' and usedColor in possibilities:
            possibilities.remove(usedColor)

    return possibilities





