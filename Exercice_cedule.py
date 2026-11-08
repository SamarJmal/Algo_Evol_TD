import random

capacites = [20, 15, 35, 40, 15, 15, 10]
demande = [80, 90, 65, 70]
TOTAL = sum(capacites)
NB_UNITES = len(capacites)

blocs_2_periodes = ["1100", "0110", "0011"]
blocs_1_periode = ["1000", "0100", "0010", "0001"]
possibles = [blocs_2_periodes, blocs_2_periodes] + [blocs_1_periode] * 5


def reserves(chromosome):
    res = []
    for p in range(4):
        perdue = 0
        for u in range(NB_UNITES):
            if chromosome[u][p] == "1":
                perdue += capacites[u]
        res.append(TOTAL - perdue - demande[p])
    return res


def performance(chromosome):
    pire = min(reserves(chromosome))
    return max(pire, 0)


def individu_aleatoire():
    return [random.choice(possibles[u]) for u in range(NB_UNITES)]

def selection(population, k=3):
    candidats = random.sample(population, k)
    return max(candidats, key=performance)


def croisement(p1, p2):
    point = random.randint(1, NB_UNITES - 1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]


def mutation(chromosome, proba=0.1):
    nouveau = chromosome[:]
    for u in range(NB_UNITES):
        if random.random() < proba:
            nouveau[u] = random.choice(possibles[u])
    return nouveau


def algo_genetique(taille_pop=49, generations=50, p_croisement=0.8, p_mutation=0.1):
    population = [individu_aleatoire() for _ in range(taille_pop)]
    for g in range(1, generations + 1):
        population.sort(key=performance, reverse=True)
        meilleur = population[0]
        if g == 1 or g % 10 == 0:
            print(f"Génération {g:3d}: meilleure performance= {performance(meilleur)}")

        nouvelle = [meilleur]
        while len(nouvelle) < taille_pop:
            p1, p2 = selection(population), selection(population)
            if random.random() < p_croisement:
                e1, e2 = croisement(p1, p2)
            else:
                e1, e2 = p1[:], p2[:]
            nouvelle += [mutation(e1, p_mutation), mutation(e2, p_mutation)]
        population = nouvelle[:taille_pop]

    population.sort(key=performance, reverse=True)
    return population[0]


exemple = ["0110", "0011", "0001", "1000", "0100", "0010", "1000"]
print("Exemple du cours:", exemple)
print("Réserves par période:", reserves(exemple), " performance =", performance(exemple))
print()

random.seed(1)
best = algo_genetique()
print("\nMeilleur planning trouvé:")
for u in range(NB_UNITES):
    periodes = [str(p + 1) for p in range(4) if best[u][p] == "1"]
    print(f"  Unité {u + 1} ({capacites[u]} MW): {best[u]}  maintenance aux périodes {', '.join(periodes)}")
print("Réserves par période:", reserves(best))
print("Performance (plus petite réserve) =", performance(best))


