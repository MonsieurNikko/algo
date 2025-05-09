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
print("BFS graphe orienté : ", arbre_bfs) # résultat attendu : [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]

# BFS graphe orienté
graphe_oriente = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
arbre_bfs_oriente = bfs(graphe_oriente, 'A')
print("BFS graphe orienté : ", arbre_bfs_oriente) # résultat attendu : [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]


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
print("DFS graphe orienté : ", arbre_dfs) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]

# DFS graphe orienté avec appel récursif
graphe_oriente = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
arbre_dfs_recursive = dfs_recursive(graphe_oriente, 'A')
print("DFS graphe orienté avec appel récursif : ", arbre_dfs_recursive) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]


# DFS graphe non orienté
graphe_non_oriente = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
arbre_dfs_non_oriente = dfs(graphe_non_oriente, 'A')
print("DFS graphe non orienté : ", arbre_dfs_non_oriente) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]

# DFS graphe non orienté avec appel récursif
graphe_non_oriente = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
arbre_dfs_recursive_non_oriente = dfs_recursive(graphe_non_oriente, 'A')
print("DFS graphe non orienté avec appel récursif : ", arbre_dfs_recursive_non_oriente) # résultat attendu : [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'E')]

#===============================================================================================================================#
# StrongConnectedComponents (SCC) : Algorithme de Kosaraju
def kosaraju(graphe):
    visited = {}     # Pour marquer les sommets visités
    stack = []       # Pour stocker l’ordre de fin de visite
    scc = []         # Liste des composantes fortement connexes

    # Étape 1 : Marquer tous les sommets comme non visités
    for sommet in graphe.keys():
        visited[sommet] = False

    # Étape 2 : Première passe DFS pour remplir la pile (ordre de terminaison)
    def dfs_first_pass(sommet):
        visited[sommet] = True
        for voisin in graphe[sommet]:
            if not visited[voisin]:
                dfs_first_pass(voisin)
        stack.append(sommet)  # Empile après avoir visité tous les voisins

    # Lancer DFS pour tous les sommets non encore visités
    for sommet in graphe.keys():
        if not visited[sommet]:
            dfs_first_pass(sommet)

    # Étape 3 : Transposer le graphe (inverser les arcs)
    graphe_transpose = {}
    for sommet in graphe.keys():
        graphe_transpose[sommet] = []  # Initialise les listes vides

    for sommet in graphe.keys():
        for voisin in graphe[sommet]:
            graphe_transpose[voisin].append(sommet)

    # Étape 4 : Réinitialiser les visites pour la 2e passe
    for sommet in graphe.keys():
        visited[sommet] = False

    # Étape 5 : Deuxième passe DFS sur le graphe transposé
    def dfs_second_pass(sommet, composante):
        visited[sommet] = True
        composante.append(sommet)
        for voisin in graphe_transpose[sommet]:
            if not visited[voisin]:
                dfs_second_pass(voisin, composante)

    while stack:
        sommet = stack.pop()
        if not visited[sommet]:
            composante = []
            dfs_second_pass(sommet, composante)
            scc.append(composante)

    return scc



graphe = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['E'],
    'E': ['F'],
    'F': ['D'],
    'G': ['F', 'H'],
    'H': ['I'],
    'I': ['G']
}

print("Composantes fortement connexes (Kosaraju) :", kosaraju(graphe)) # résultat attendu : [['A', 'C', 'B'], ['D', 'F', 'E'], ['G', 'I', 'H']]

#StrongConnectedComponents (SCC) : Algorithme de Tarjan
def tarjan(graphe):
    visited = {}  # Pour marquer les sommets visités
    stack = []    # Pour stocker l’ordre de fin de visite
    scc = []      # Liste des composantes fortement connexes

    # Étape 1 : Marquer tous les sommets comme non visités
    for sommet in graphe.keys():
        visited[sommet] = False

    # Étape 2 : Première passe DFS pour remplir la pile (ordre de terminaison)
    def dfs_first_pass(sommet):
        visited[sommet] = True
        for voisin in graphe[sommet]:
            if not visited[voisin]:
                dfs_first_pass(voisin)
        stack.append(sommet)  # Empile après avoir visité tous les voisins

    # Lancer DFS pour tous les sommets non encore visités
    for sommet in graphe.keys():
        if not visited[sommet]:
            dfs_first_pass(sommet)

    # Étape 3 : Transposer le graphe (inverser les arcs)
    graphe_transpose = {}
    for sommet in graphe.keys():
        graphe_transpose[sommet] = []  # Initialise les listes vides

    for sommet in graphe.keys():
        for voisin in graphe[sommet]:
            graphe_transpose[voisin].append(sommet)

    # Étape 4 : Réinitialiser les visites pour la 2e passe
    for sommet in graphe.keys():
        visited[sommet] = False

    # Étape 5 : Deuxième passe DFS sur le graphe transposé
    def dfs_second_pass(sommet, composante):
        visited[sommet] = True
        composante.append(sommet)
        for voisin in graphe_transpose[sommet]:
            if not visited[voisin]:
                dfs_second_pass(voisin, composante)

    while stack:
        sommet = stack.pop()
        if not visited[sommet]:
            composante = []
            dfs_second_pass(sommet, composante)
            scc.append(composante)

    return scc

print("Composantes fortement connexes (Tarjan) :", tarjan(graphe)) # résultat attendu : [['A', 'C', 'B'], ['D', 'F', 'E'], ['G', 'I', 'H']]

#===============================================================================================================================#

"""matrice d'adjacence est une représentation d'un graphe sous forme de tableau où chaque case (i, j) indique s'il y a une arête entre le sommet i et le sommet j.
   Par exemple, si la case (i, j) contient 1, cela signifie qu'il y a une arête entre le sommet i et le sommet j. Si elle contient 0, il n'y a pas d'arête entre ces deux sommets."""
def adjency_matrix(graphe):
    # Récupérer tous les sommets du graphe
    sommets = list(graphe.keys())
    n = len(sommets)  # Nombre de sommets

    # Créer une matrice d'adjacence n x n initialisée à 0
    matrice = []
    for i in range(n):
        ligne = []  # On crée une nouvelle ligne vide
        for j in range(n):
            ligne.append(0)  # On ajoute un zéro à la ligne
        matrice.append(ligne)  # On ajoute la ligne complète à la matrice

    # Remplir la matrice d'adjacence
    for i in range(n):
        for voisin in graphe[sommets[i]]:
            j = sommets.index(voisin)  # Trouver l'indice du voisin
            matrice[i][j] = 1  # Marquer l'arête dans la matrice

    return matrice

"""Isomorphisme entre deux graphes : Deux graphes sont dits isomorphes s'ils ont la même structure, c'est-à-dire qu'il existe une correspondance entre leurs sommets et leurs arêtes.
   En d'autres termes, on peut transformer l'un des graphes en l'autre en renommant ses sommets sans changer la structure des connexions entre eux."""
def isomorphisme(graphe1, graphe2):
    # Vérifier si les deux graphes ont le même nombre de sommets
    if len(graphe1) != len(graphe2):
        return False

    # Créer les matrices d'adjacence pour les deux graphes
    matrice1 = adjency_matrix(graphe1)
    matrice2 = adjency_matrix(graphe2)

    # Vérifier si les matrices d'adjacence sont identiques
    for i in range(len(matrice1)):
        for j in range(len(matrice1)):
            if matrice1[i][j] != matrice2[i][j]:
                return False  # Si une valeur diffère, les graphes ne sont pas isomorphes

    return True  # Les graphes sont isomorphes


"""Chain : Un graphe est une chaîne si tous ses sommets ont au plus 2 voisins."""
def isChain(graphe):
    # Vérifier si le graphe est une chaîne
    for sommet in graphe:
        if len(graphe[sommet]) > 2:  # Si un sommet a plus de 2 voisins, ce n'est pas une chaîne
            return False
    return True  # Tous les sommets ont au plus 2 voisins, donc c'est une chaîne


"""Cycle : Un graphe est un cycle si tous ses sommets ont exactement 2 voisins."""
def isCycle(graphe):
    # Vérifier si le graphe est un cycle
    for sommet in graphe:
        if len(graphe[sommet]) != 2:  # Si un sommet n'a pas exactement 2 voisins, ce n'est pas un cycle
            return False
    return True  # Tous les sommets ont exactement 2 voisins, donc c'est un cycle


"""Complet : Un graphe est complet si chaque sommet est connecté à tous les autres sommets."""
def isComplete(graphe):
    # Vérifier si le graphe est complet
    n = len(graphe)  # Nombre de sommets
    for sommet in graphe:
        if len(graphe[sommet]) != n - 1:  # Si un sommet n'a pas n-1 voisins, ce n'est pas complet
            return False
    return True  # Tous les sommets ont n-1 voisins, donc c'est complet


"""Elementaire : Un graphe est élémentaire si tous ses sommets ont un degré de 1."""
def elementaire(graphe):
    # Vérifier si le graphe est élémentaire (tous les sommets ont un degré de 1)
    for sommet in graphe:
        if len(graphe[sommet]) != 1:  # Si un sommet n'a pas exactement 1 voisin, ce n'est pas élémentaire
            return False
    return True  # Tous les sommets ont exactement 1 voisin, donc c'est élémentaire

"""Connexe : Un graphe est connexe si tous ses sommets sont accessibles à partir de n'importe quel autre sommet."""
def isConnexe(graphe):
    # Vérifier si le graphe est connexe (il existe un chemin entre chaque paire de sommets)
    visited = {}  # Dictionnaire pour savoir quels sommets ont déjà été visités

    # On marque tous les sommets comme "non visités" au début
    for u in graphe:
        visited[u] = False

    # On commence le parcours depuis le premier sommet
    def dfs(sommet):
        visited[sommet] = True  # Marque le sommet comme visité
        for voisin in graphe[sommet]:
            if not visited[voisin]:  # Si le voisin n'est pas encore visité
                dfs(voisin)  # On l'explore

    # Lancer DFS à partir du premier sommet
    dfs(list(graphe.keys())[0])

    # Vérifier si tous les sommets ont été visités
    for u in graphe:
        if not visited[u]:
            return False  # Si un sommet n'a pas été visité, le graphe n'est pas connexe

    return True  # Tous les sommets ont été visités, donc le graphe est connexe


"""Composantes connexes : Un graphe est composé de plusieurs composantes connexes si on peut le diviser en sous-graphes où chaque sous-graphe est connexe."""
def TousLesComposantesConnexes(graphe):
    # Trouver toutes les composantes connexes du graphe
    visited = {}  # Dictionnaire pour savoir quels sommets ont déjà été visités
    composantes = []  # Liste pour stocker les composantes connexes

    # On marque tous les sommets comme "non visités" au début
    for u in graphe:
        visited[u] = False

    def dfs(sommet, composante):
        visited[sommet] = True  # Marque le sommet comme visité
        composante.append(sommet)  # Ajoute le sommet à la composante courante
        for voisin in graphe[sommet]:
            if not visited[voisin]:  # Si le voisin n'est pas encore visité
                dfs(voisin, composante)  # On l'explore

    for sommet in graphe:
        if not visited[sommet]:  # Si le sommet n'a pas été visité
            composante = []  # Crée une nouvelle composante
            dfs(sommet, composante)  # Lance DFS pour cette composante
            composantes.append(composante)  # Ajoute la composante à la liste des composantes

    return composantes  # Retourne toutes les composantes connexes trouvées


"""Planaire : Un graphe est planaire s'il peut être dessiné sur un plan sans que ses arêtes se croisent."""
def planaire(graphe):
    # Vérifier si le graphe est planaire (peut être dessiné sur un plan sans intersections)
    # Pour simplifier, on va juste vérifier si le graphe est complet ou non
    return not isComplete(graphe)  # Si ce n'est pas complet, on le considère comme planaire pour cet exemple


"""Full : Un graphe est plein si chaque sommet est connecté à tous les autres sommets."""
def isFull(graphe):
    # Vérifier si le graphe est plein (tous les sommets sont connectés entre eux)
    for sommet in graphe:
        if len(graphe[sommet]) != len(graphe) - 1:  # Si un sommet n'a pas n-1 voisins, ce n'est pas plein
            return False
    return True  # Tous les sommets ont n-1 voisins, donc c'est plein


"""Biparti : Un graphe est biparti s'il peut être colorié avec deux couleurs de manière à ce que deux sommets adjacents n'aient pas la même couleur."""
def isBiparti(graphe):
    # Vérifier si le graphe est biparti (peut être divisé en deux ensembles sans arêtes entre eux)
    couleurs = {}  # Dictionnaire pour stocker les couleurs des sommets

    def dfs(sommet, couleur):
        couleurs[sommet] = couleur  # Colorie le sommet
        for voisin in graphe[sommet]:
            if voisin not in couleurs:  # Si le voisin n'est pas encore colorié
                if not dfs(voisin, 1 - couleur):  # On lui donne la couleur opposée
                    return False
            elif couleurs[voisin] == couleur:  # Si le voisin a la même couleur, ce n'est pas biparti
                return False
        return True

    for sommet in graphe:
        if sommet not in couleurs:  # Si le sommet n'est pas encore colorié
            if not dfs(sommet, 0):  # On commence avec la couleur 0
                return False

    return True  # Le graphe est biparti si on a pu colorier tous les sommets sans conflit


"""Structure : La structure d'un graphe est la manière dont ses sommets et arêtes sont organisés."""
def showStructure(graphe):
    # Afficher la structure du graphe
    for sommet, voisins in graphe.items():
        print(f"{sommet}: {', '.join(voisins)}")  # Affiche le sommet et ses voisins

