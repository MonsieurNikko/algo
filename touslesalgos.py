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

# Exemple d'utilisation de la fonction bfs avec un graphe orienté
graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

arbre_bfs = bfs(graphe, 'A')
print(arbre_bfs) # résultat attendu : [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]

# BFS graphe orienté
graphe_oriente = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
arbre_bfs_oriente = bfs(graphe_oriente, 'A')
print(arbre_bfs_oriente) # résultat attendu : [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]


#===============================================================================================================================#

# DFS (Depth First Search)
def dfs(graphe, sommet):
    visited = {}  # Dictionnaire pour suivre les sommets visités

    # Initialisation : tous les sommets sont marqués comme non visités
    for u in graphe:
        visited[u] = False

    T = []        # Liste des arêtes parcourues (arbre DFS)
    pile = []     # Pile LIFO pour DFS
    pile.append(sommet)  # On commence avec le sommet donné

    while pile:
        u = pile.pop()  # On dépile le sommet courant
        if not visited[u]:  # ⚠️ Vérifie si on ne l’a pas encore visité
            visited[u] = True  # Maintenant on le marque comme visité
            for voisin in graphe[u]:
                if not visited[voisin]:
                    pile.append(voisin)       # On empile les voisins non visités
                    T.append((u, voisin))     # On enregistre l’arête parcourue

    return T  # Retourne les arêtes du parcours en profondeur


def dfs_recursive(graphe, sommet):
    visited = {}  # Dictionnaire pour suivre les sommets visités

    # Initialisation : tous les sommets sont marqués comme non visités
    for u in graphe:
        visited[u] = False

    T = []  # Liste des arêtes parcourues (arbre DFS)

    def dfs_helper(u):
        visited[u] = True  # Marque le sommet comme visité
        for voisin in graphe[u]:
            if not visited[voisin]:
                T.append((u, voisin))  # Enregistre l’arête parcourue
                dfs_helper(voisin)  # Appel récursif sur le voisin

    dfs_helper(sommet)  # Démarre la recherche à partir du sommet donné
    return T  # Retourne les arêtes du parcours en profondeur

# Exemple d'utilisation de la fonction dfs avec un graphe orienté
graphe_oriente = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
arbre_dfs = dfs(graphe_oriente, 'A')
print(arbre_dfs) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]

# DFS graphe orienté avec appel récursif
graphe_oriente = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
arbre_dfs_recursive = dfs_recursive(graphe_oriente, 'A')
print(arbre_dfs_recursive) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]


# DFS graphe non orienté
graphe_non_oriente = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
arbre_dfs_non_oriente = dfs(graphe_non_oriente, 'A')
print(arbre_dfs_non_oriente) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]

# DFS graphe non orienté avec appel récursif
graphe_non_oriente = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
arbre_dfs_recursive_non_oriente = dfs_recursive(graphe_non_oriente, 'A')
print(arbre_dfs_recursive_non_oriente) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]