import random, math, itertools

INF = 1000
aretes = {(1,2):14,(1,3):15,(1,8):17,
          (2,3):13,(2,4):14,(2,5):20,(2,8):21,
          (3,4):11,(3,5):21,(3,6):17,(3,7):9,(3,8):9,
          (4,5):11,(4,6):10,(4,7):8,(4,8):20,
          (5,6):15,(5,7):18,
          (6,7):9,(7,8):13}
def d(a, b):
    return aretes.get((a, b), aretes.get((b, a), INF))

def longueur(t):
    return sum(d(t[i], t[(i + 1) % len(t)]) for i in range(len(t)))

def echange(t, i, j):
    u = t[:]; u[i], u[j] = u[j], u[i]; return u

def inversion(t, i, j):
    return t[:i] + t[i:j + 1][::-1] + t[j + 1:]

init = [1, 2, 3, 4, 5, 6, 7, 8]
print("Solution initiale", init, "-> longueur", longueur(init))


print("\n1) RECHERCHE TABOUE ")
cour, best, f_best, tabou = init[:], init[:], longueur(init), []
for it in range(1, 6):
    cands = []
    for i, j in itertools.combinations(range(1, 8), 2):       # 21 voisins
        v = inversion(cour, i, j); f = longueur(v)
        pair = (cour[i], cour[j])
        if pair not in tabou and pair[::-1] not in tabou or f < f_best:
            cands.append((f, v, pair))
    f, cour, pair = min(cands, key=lambda c: c[0])
    tabou.append(pair); tabou = tabou[-3:]
    if f < f_best: best, f_best = cour[:], f
    print(f"It {it}: inversion {pair} -> {cour}  f = {f} | tabou = {tabou} | meilleur = {f_best}")


print("\n2) RECUIT SIMULÉ ")
random.seed(3)
cour, T = init[:], 20.0
f_cour = longueur(cour)
for it in range(1, 6):
    i, j = sorted(random.sample(range(1, 8), 2))
    v = echange(cour, i, j); f_v = longueur(v)
    delta = f_v - f_cour
    if delta <= 0:
        ok, info = True, "meilleur -> accepté"
    else:
        p = math.exp(-delta / T); r = random.random()
        ok = r < p; info = f"p = {p:.3f}, r = {r:.3f} -> {'accepté' if ok else 'refusé'}"
    print(f"It {it}: T = {T:5.2f} | voisin {v} f = {f_v} | delta = {delta:+d} | {info}")
    if ok: cour, f_cour = v, f_v
    T *= 0.8
print("Solution finale :", cour, "f =", f_cour)


print("\n3) ALGORITHME GÉNÉTIQUE ")
random.seed(5)
def hasard():
    p = list(range(2, 9)); random.shuffle(p); return [1] + p
def croisement_OX(p1, p2):
    a, b = sorted(random.sample(range(1, 8), 2))
    enfant = [None] * 8; enfant[0] = 1
    enfant[a:b + 1] = p1[a:b + 1]
    reste = [v for v in p2 if v not in enfant]
    for k in range(8):
        if enfant[k] is None: enfant[k] = reste.pop(0)
    return enfant
def mutation(t):
    i, j = random.sample(range(1, 8), 2); return echange(t, i, j)

pop = [init] + [hasard() for _ in range(5)]
for gen in range(1, 4):
    pop.sort(key=longueur)
    print(f"Génération {gen} :", [(p, longueur(p)) for p in pop[:3]], "...")
    parents = pop[:3]
    enfants = []
    for _ in range(3):
        p1, p2 = random.sample(parents, 2)
        e = croisement_OX(p1, p2)
        if random.random() < 0.3: e = mutation(e)
        enfants.append(e)
    pop = parents + enfants
pop.sort(key=longueur)
print("Meilleur individu final :", pop[0], "longueur =", longueur(pop[0]))

opt = min(([1] + list(p) for p in itertools.permutations(range(2, 9))), key=longueur)
print("\nOptimum exact (force brute) :", opt, "longueur =", longueur(opt))