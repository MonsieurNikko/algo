def euler(graphe):
    # Copie le graphe pour ne pas le modifier
    g = {}
    for sommet in graphe:
        g[sommet] = graphe[sommet][:]

    # Trouver un cycle initial à partir d’un sommet quelconque
    depart = next(iter(g))
    pile = [depart]
    cycle = []

    while pile:
        u = pile[-1]
        if g[u]:
            v = g[u].pop()
            g[v].remove(u)
            pile.append(v)
        else:
            cycle.append(pile.pop())

    cycle.reverse()
    return cycle


def main():
    graphe = {
        1: [2, 3],
        2: [1, 3, 4, 5],
        3 : [1, 2, 4, 5],
        4: [2, 3, 6, 7],
        5: [2, 3, 6, 7],
        6: [4, 5, 7, 8],
        7: [4, 5, 6, 8],
        8: [6, 7]
    }

    cycle = euler(graphe)
    print("Cycle Eulerien:", cycle)
    

if __name__ == "__main__":
    main()