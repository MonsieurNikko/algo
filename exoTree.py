def find(parent, sommet):
    while parent[sommet] != sommet:
        sommet = parent[sommet]
    return sommet

def union(parent, sommet, voisin):
    racineSommet = find(parent,sommet)
    racineVoisin = find(parent,voisin)
    if racineSommet != racineVoisin :
        parent[racineVoisin] = racineSommet
        return True
    return False

def kruskal(noeuds, aretes):
    parent = {}
    
    for sommet in noeuds:
        parent[sommet] = sommet
    
    aretes = sorted(aretes, key=lambda x: x[1])
    
    mst = []
    for sommet,voisin,poids in aretes:
        if union(parent,sommet,voisin):
            mst.append((sommet,voisin,poids))
        if len(mst) == len(noeuds):
            break
    return mst


def main():
    noeuds = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    aretes = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 6),
    (7, 8, 7)
]
    mst = kruskal(noeuds,aretes)

    print("Minimum Spanning Tree (MST) :")

    for u, v, w in mst:
        print(f"{u} - {v} : {w}")

if __name__ == "__main__":
    main()