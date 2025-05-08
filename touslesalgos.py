# Parcours en largeur (BFS = Breadth First Search)
def bfs(graphe, sommet):
    visited = {}  # Dictionnaire pour savoir quels sommets ont déjà été visités

    # On marque tous les sommets comme "non visités" au début
    for u in graphe:
        visited[u] = False

    T = []  # Arbres de parcours (ou liste d'arêtes parcourues)
    file = []  # On utilise une liste comme file d'attente (premier arrivé, premier sorti)
    file.append(sommet)  # On commence le parcours depuis le sommet donné
    visited[sommet] = True  # On marque ce sommet comme visité

    while file:  # Tant que la file n'est pas vide
        u = file.pop(0)  # On enlève le premier sommet de la file
        for voisin in graphe[u]:
            if not visited[voisin]: # Si le vistited[voisin] = false, on le visite
                visited[voisin] = True  # On marque le voisin comme visité
                file.append(voisin)
                T.append((u, voisin))  # On ajoute l'arête (u, voisin) à la liste des arêtes parcourues

    return T  # On retourne la liste des arêtes parcourues

# Exemple d'utilisation de la fonction bfs
graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

arbre_bfs = bfs(graphe, 'A')
print(arbre_bfs) # résultat attendu : [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]

#=========================================================================================#
# Parcours en profondeur (DFS = Depth First Search)
