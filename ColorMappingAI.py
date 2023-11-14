## Visualization

# Create Random Graph
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx

# Parameters
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'),('A', 'C'),('B', 'C'),('C', 'D'),('D', 'F'),('D', 'E'),('E', 'F')]


# Create the corresponding graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)


# Plot the graph
plt.figure(figsize=(8,8))
nx.draw(G, with_labels = True)
plt.show()

##

zones = ["A", "B", "C", "D"]
constraints = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]
soluce = ['n', 'n', 'n', 'n']

def Resolve(tab_soluce):
    bool = True
    for i in range(len(tab_soluce)):
        if tab_soluce[i] == 'n':
            bool = False
    return bool



#def Found_More_Constraint(tab_constraint)
#    counts = []





