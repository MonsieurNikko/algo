def welsh_powell(graph):
    """
    Colorie un graphe en utilisant l'algorithme de Welsh-Powell.
    :param graph: dict représentant le graphe {noeud: [voisins]}
    :return: dict représentant la coloration {noeud: couleur}
    """
    # Trier les sommets par degré décroissant
    sorted_nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)

    colors = {}  # Dictionnaire pour stocker les couleurs
    current_color = 1

    for node in sorted_nodes:
        if node not in colors:
            colors[node] = current_color
            for other_node in sorted_nodes:
                if other_node not in colors:
                    isValid = True
                    for neighbor in graph[other_node]:
                        if neighbor in colors and colors[neighbor] == current_color:
                            isValid = False
                            break
                    if isValid:
                        colors[other_node] = current_color
            current_color += 1

    return colors

def main():
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'C', 'D', 'F'],
        'C' : ['A', 'B', 'D', 'G'],
        'D' : ['B', 'C', 'E'],
        'E' : ['D', 'F', 'G'],
        'F' : ['B', 'E', 'G', 'H'],
        'G' : ['C', 'E', 'F', 'H'],
        'H' : ['F', 'G']
    }

    graph2 = {
        1 : [2, 3],
        2 : [1, 3],
        3 : [1, 2, 5],
        4 : [5, 6],
        5 : [4, 3],
        6 : [4],
    }

    welsh_powell_coloring = welsh_powell(graph)
    
    welsh_powell_coloring2 = welsh_powell(graph2)
    print("Coloration du graphe :")
    for node, color in welsh_powell_coloring.items():
        print(f"Noeud {node} : Couleur {color}")

    print("\nColoration du graphe 2 :")
    for node, color in welsh_powell_coloring2.items():
        print(f"Noeud {node} : Couleur {color}")

if __name__ == "__main__":
    main()