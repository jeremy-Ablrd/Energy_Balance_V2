#AVOIR UN CODE POUR AFFICHER UN GRADIENT DE COULEUR AVEC CMAP

#SI NECESSAIRE REGARDER LA VIDEO MACHINE LEARNIA, SUR LES CHROMOSOMES (POUR SEPARER LES DIFFERENTS OBJETS)

#IMPLEMENTER DAN LE CODE POUR AVOIR UN DIAGRAMME AVEC COULEUR DEGRADER.

#utilisation éventuelle de meshgrid

import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('test1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
i_range = img.shape[0]
j_range = img.shape[1]

for i in range(i_range):
    #boucle de l'axe des x
    for j in range(j_range):
        #Stocker chaque valeur RVB
        R, G, B = img[i, j]
        #Obtenez uniquement les coordonnées qui s'appliquent à la couleur du graphique
        if (230 <= R <= 255) and (0 <= G <= 30) and (130 <= B <= 160):
                graph_coordinate.append([i, j, img[i, j]])
                x_list.append(j)

#print(plt.gca().get_xaxis())
#print(plt.gca().get_yaxis())
#print(plt.axis())
