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
G.add_nodes_from(nodes, color='white', possibilities=None, previous=None) # White is considered as a non-affected color propriety
G.add_edges_from(edges)

for node in G.nodes():
    G.nodes[node]['possibilities']=['red','green','blue']

# Plot the graph
nx.draw(G, with_labels = True, node_color='white', node_size=800)# initial graph
plt.show()

## Main program

node = Find_More_Constraint(G.nodes)#First of all
G.nodes[node]['previous'] = "First"
memory = "First"
limite = len(G.nodes())

#while not Is_Finished():
while Color_Is_Possible(node):
    Choose_Color(node)
    G.nodes[node]['previous'] = memory
    memory = node
    if Find_Uncolored_Neighbours(node)!=[]:
        node = Find_More_Constraint(Find_Uncolored_Neighbours(node))
    limite -=1

Visualize()

## Resolving functions

# def Find_More_Constraint():
#     maximum = 0
#     winner = 0
#     for node in ListOfNodes:
#         count = len(G.edges(node)) # Number of edges corresponding to the node
#         if maximum < count:
#             maximum = count
#             winner = node
#     return

def Find_Neighbours(node):
    neighbours = []
    for border in G.edges(node):
        node, neighbour = border
        neighbours.append(neighbour)
    return neighbours

def Find_Uncolored_Neighbours(node):
    neighbours = Find_Neighbours(node)
    neighbours = [neighbours[i] for i in range(len(neighbours)) if G.nodes[neighbours[i]]['color']=='white']
    return neighbours

def Find_Possibilities(node):
    possibles = G.nodes[node]['possibilities']
    for neighbour in Find_Neighbours(node):
        usedColor = G.nodes[neighbour]['color']
        if usedColor != 'white' and usedColor in possibles:
            G.nodes[node]['possibilities'].remove(usedColor)
    return possibles

def Colore_A_Path(node):
    if Color_Is_Possible(node):
        Choose_Color(node)

    if Find_Uncolored_Neighbours(node)!=[]:
        node = Find_More_Constraint(Find_Uncolored_Neighbours(node))

def Color_Is_Possible(node):
    isPossible = G.nodes[node]['possibilities']!=[]
    return isPossible


def Choose_Color(node):
    possibilities = Find_Possibilities(node)
    #color = np.random.choice(possibilities)
    color = G.nodes[node]['possibilities'][0] # On garde toujours le même ordre de priorité
    G.nodes[node]['color'] = color
    G.nodes[node]['possibilities'].remove(color)
    return


def Visualize():
    plt.close()
    plt.figure
    colorList = [G.nodes[node]['color'] for node in G.nodes()]
    nx.draw(G, with_labels = True, node_size=800, node_color=colorList)
    plt.show()
    return

def Is_Finished():
    for node in G.nodes():
        if G.nodes[node]['color'] == 'white':
            return False
    return True


# Choisir aléatoirement dans les possibilités + gérer le cas pas de possibilité
# Pour ça, définir les noeuds ouverts et fermés
# Répéter les instructions tant que le graphe n'est pas complet
# Afficher si possible à chaque étape
# Généraliser à des cas randoms
# Chercher des assertions qui permettent de déduire rapidement qu'un problème est insoluble


def Find_More_Constraint(listOfNodes):
    maximum = 0
    winner = 0
    for node in listOfNodes:
        count = len(G.edges(node)) # Number of edges corresponding to the node
        if maximum < count:
            maximum = count
            winner = node
    return winner

