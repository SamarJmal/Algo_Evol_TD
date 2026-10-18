import random, itertools

cout   = [[5, 3, 4],
          [6, 7, 2]]
offre  = [8, 9]
demande = [4, 5, 8]
ND, NM = 2, 3

def cout_total(x):
    return sum(cout[i][j] * x[i][j] for i in range(ND) for j in range(NM))

def coin_nord_ouest():
    o, d = offre[:], demande[:]
    x = [[0] * NM for _ in range(ND)]
    i = j = 0
    while i < ND and j < NM:
        q = min(o[i], d[j])
        x[i][j] = q
        o[i] -= q; d[j] -= q
        if o[i] == 0: i += 1
        else: j += 1
    return x

def voisins(x):
    res = []
    for i, k in itertools.combinations(range(ND), 2):
        for j, l in itertools.combinations(range(NM), 2):
            for s in (+1, -1):
                y = [r[:] for r in x]
                y[i][j] += s; y[k][l] += s
                y[i][l] -= s; y[k][j] -= s
                if all(v >= 0 for r in y for v in r):
                    res.append((y, (i, j, k, l, s)))
    return res

def taboue(max_iter=30, tenure=3):
    courant = coin_nord_ouest()
    meilleur, f_meilleur = courant, cout_total(courant)
    tabou = []
    print("Solution initiale :", courant, "coût =", f_meilleur)
    for it in range(1, max_iter + 1):
        candidats = []
        for y, mv in voisins(courant):
            inverse = (mv[0], mv[1], mv[2], mv[3], -mv[4])
            est_tabou = mv in tabou
            f = cout_total(y)
            if not est_tabou or f < f_meilleur:
                candidats.append((f, y, inverse))
        if not candidats:
            break
        f, courant, inverse = min(candidats, key=lambda c: c[0])
        tabou.append(inverse)
        if len(tabou) > tenure:
            tabou.pop(0)
        if f < f_meilleur:
            meilleur, f_meilleur = courant, f
        print(f"Itération {it:2d} : coût courant = {f:3d} | meilleur = {f_meilleur}")
    return meilleur, f_meilleur

if __name__ == "__main__":
    x, f = taboue()
    print("\nMeilleure solution (lignes = D1, D2 ; colonnes = M1, M2, M3) :")
    for i in range(ND):
        print(f"  D{i+1} :", x[i])
    print("Coût total minimal =", f)