def tarjan(graph):
    index = 0
    S = []                   # Stack
    onStack = set()          # Pour vérifier si un sommet est dans la pile
    indices = {}             # v.index
    lowlinks = {}            # v.lowlink
    sccs = []                # Résultat final : liste des SCC

    def strongconnect(v):
        nonlocal index

        # Affecter index et lowlink
        indices[v] = index
        lowlinks[v] = index
        index += 1

        S.append(v)
        onStack.add(v)

        # Considérer les successeurs de v
        for w in graph.get(v, []):
            if w not in indices:
                # w pas encore visité
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in onStack:
                # w est dans la pile, donc fait partie de la SCC actuelle
                lowlinks[v] = min(lowlinks[v], indices[w])

        # Si v est une racine d'une SCC
        if lowlinks[v] == indices[v]:
            # Extraire la composante fortement connexe
            scc = []
            while True:
                w = S.pop()
                onStack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    # Parcourir tous les sommets du graphe
    for v in graph:
        if v not in indices:
            strongconnect(v)

    return sccs


def main():
    graph = {
        0: [1, 7],
        1: [2, 6],
        2: [1, 3],
        3: [],
        4: [9],
        5: [2, 6],
        6: [1],
        7: [6],
        8: [5, 9],
        9: [8]
    }

    sccs = tarjan(graph)
    print("SCCs trouvées :", sccs)

if __name__ == "__main__":
    main()
