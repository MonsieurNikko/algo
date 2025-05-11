#exo 4
def isChain(graph, listNodes):
    """
    Vérifie si listNodes forme une chaîne dans le graphe.
    :param graph: dictionnaire représentant le graphe {noeud: [voisins]}
    :param listNodes: liste ordonnée des noeuds [n1, n2, ..., nk]
    :return: True si c'est une chaîne, False sinon
    """
    for i in range(len(listNodes) - 1):
        u = listNodes[i]
        v = listNodes[i + 1]
        if u in graph:
            voisins = graph[u]
        else:
            voisins = []

        if v not in voisins:
            return False
    return True


def isChainSimple(graph, listNodes):
    """
    Vérifie si listNodes forme une chaîne simple (pas de répétition) dans le graphe.
    :param graph: dict représentant le graphe {noeud: [voisins]}
    :param listNodes: liste de noeuds
    :return: True si c'est une chaîne simple, False sinon
    """
    # Étape 1 : vérifier que c'est une chaîne
    if not isChain(graph, listNodes):
        return False

    # Étape 2 : vérifier qu'il n'y a pas de doublons
    return len(listNodes) == len(set(listNodes))

def isChainElementary(graph, listNodes):
    """
    Vérifie si listNodes forme une chaîne élémentaire dans un graphe non orienté.
    :param graph: dict représentant le graphe {noeud: [voisins]}
    :param listNodes: liste ordonnée des noeuds
    :return: True si c'est une chaîne élémentaire, False sinon
    """
    if not isChain(graph, listNodes):
        return False

    if len(listNodes) != len(set(listNodes)):
        return False

    seen_edges = set()

    for i in range(len(listNodes) - 1):
        u = listNodes[i]
        v = listNodes[i + 1]
        edge = tuple(sorted((u, v)))  # pour éviter (A,B) et (B,A) doublon
        if edge in seen_edges:
            return False
        seen_edges.add(edge)

    return True

def chainElementary(graph, node):
    """
    Retourne toutes les chaînes élémentaires partant de `node`
    :param graph: dict représentant le graphe {noeud: [voisins]}
    :param node: sommet de départ
    :return: liste de chaînes élémentaires (chaque chaîne = liste de noeuds)
    """
    chains = []

    def dfs(path, used_edges):
        current = path[-1]
        chains.append(path[:])  # ajoute une copie de la chaîne actuelle

        for neighbor in graph.get(current, []):
            edge = tuple(sorted((current, neighbor)))
            if neighbor not in path and edge not in used_edges:
                used_edges.add(edge)
                dfs(path + [neighbor], used_edges)
                used_edges.remove(edge)

    dfs([node], set())
    return chains


def isCycle(graph, listNodes):
    """
    Vérifie si listNodes forme un cycle dans un graphe non orienté.
    :param graph: dictionnaire {noeud: [voisins]}
    :param listNodes: liste de noeuds formant un chemin
    :return: True si c’est un cycle, sinon False
    """
    if len(listNodes) < 4:
        return False  # besoin de 3 sommets distincts + retour au départ

    if listNodes[0] != listNodes[-1]:
        return False  # doit revenir au point de départ

    # vérifier que toutes les arêtes sont valides
    for i in range(len(listNodes) - 1):
        u = listNodes[i]
        v = listNodes[i + 1]
        if v not in graph.get(u, []):
            return False

    # vérifier qu'il n’y a pas de sommet répété sauf début/fin
    inner_nodes = listNodes[:-1]  # enlever le dernier car il est égal au premier
    if len(inner_nodes) != len(set(inner_nodes)):
        return False

    # vérifier que les arêtes ne sont pas répétées
    used_edges = set()
    for i in range(len(listNodes) - 1):
        edge = tuple(sorted((listNodes[i], listNodes[i+1])))
        if edge in used_edges:
            return False
        used_edges.add(edge)

    return True

def isconnex(graph):
    """
    Vérifie si un graphe non orienté est connexe.
    Un graphe est connexe si chaque paire de sommets est reliée par un chemin.
    C'est-à-dire qu'il n'y a pas de sommet isolé.
    Par exemple, le graphe suivant est connexe:
    A -- B
    :param graph: dict {noeud: [voisins]}
    :return: True si connexe, False sinon
    """
    if not graph:
        return True

    visited = set()

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)

    start = next(iter(graph))  # prendre un nœud quelconque
    dfs(start)

    return len(visited) == len(graph)

def compConnexe(graph):
    """
    Retourne la liste des composantes connexes du graphe.
    Chaque composante est une liste de sommets connectés entre eux.
    """
    visited = set()
    composants = []

    def dfs(u, composant):
        visited.add(u)
        composant.append(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v, composant)

    for sommet in graph:
        if sommet not in visited:
            composant = []
            dfs(sommet, composant)
            composants.append(composant)

    return composants