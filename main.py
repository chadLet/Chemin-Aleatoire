# Importation des librairies.
import random
import matplotlib.pyplot as plt


chemin = []  # Liste qui définira notre chemin.
Right = 0  # Nombre de fois que l'on a tourné à droite.
Up = 0  # Nombre de fois que l'on a "tourné" vers le haut.

# Création du chemin qui a pour destination les coordonnées (8;7).
while Right != 8 or Up != 7:
    i = random.randint(0, 1)
    if i == 0:
        if Right == 8:
            pass
        else:
            chemin.append(i)
            Right += 1
    else:
        if Up == 7:
            pass
        else:
            chemin.append(i)
            Up += 1

coord = [0, 0]  # Coordonées des points qu'on crée.
coordList = []  # Liste des coordonnées des points créés.

# Créations des points et ajout de ces points dans la liste coordList.
for i in chemin:
    if i == 0:
        coord[0] += 1
        coordList.append((coord[0], coord[1]))
    else:
        coord[1] += 1
        coordList.append((coord[0], coord[1]))

x = [0]  # Liste des coordonnées x des points créés.
y = [0]  # Liste des coordonnées y des points créés.
i = 0  # Symbole utile à notre itération

# Remplissage des listes x et y.
while i < len(coordList):
    x.append(coordList[i][0])
    y.append(coordList[i][1])
    i += 1

# Création et affichage des chemins en utilisant les listes x et y.
plt.grid(visible=True, which='major', axis='both')
plt.plot(x, y, marker=".", markersize=20, markeredgecolor="red", markerfacecolor="black")
plt.savefig('chemin.png')
