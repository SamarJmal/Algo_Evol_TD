### 
Exercice 2 : problème de transport (recherche taboue)
Énoncé: Deux dépôts (D1 : 8 containers, D2 : 9 containers) livrent trois magasins (demandes : 4, 5 et 8 containers). On cherche la répartition qui minimise le coût total de transport.
<img width="1919" height="1022" alt="Execution Ex2" src="https://github.com/user-attachments/assets/5f0f19f2-be3b-417f-9407-eac28eda0ebd" />

Exercice 3 : voyageur de commerce (8 villes)
Énoncé: Trouver le circuit le plus court qui passe une fois par chacune des 8 villes et revient à la ville 1. Un « - » dans le tableau signifie qu'il n'y a pas de route directe (pénalité de 1000 dans le code)

Solution initiale imposée : 1-2-3-4-5-6-7-8-1, de longueur 103.
1) Recherche taboue
<img width="1919" height="758" alt="Execution Ex3_Rech Tabou" src="https://github.com/user-attachments/assets/317a3c09-bd0a-44e9-9c93-55797d83f425" />

Résultat : circuit 1-2-4-5-6-7-3-8-1, longueur 98.

2) Recuit simulé
<img width="1919" height="738" alt="Execution Ex3_Recuit Simulé" src="https://github.com/user-attachments/assets/c4638427-9bb1-44e1-bbc1-829a91054cfc" />

3) Algorithme génétique
<img width="1919" height="1022" alt="Execution Ex3_Algo Genetique" src="https://github.com/user-attachments/assets/aa2cd639-3984-4029-89ea-b3385f830577" />
