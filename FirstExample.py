# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:59:37 2024

@author: lgcadillac
"""

from pylab import *             # Importation de la bibliotheque maths

dt=0.05                        # Le pas de temps
T=1.                            # Le temps final
N=int(ceil(T/dt))               # Le nombre d'iteration (entier)
dt=T/N                          # Petite correction pour avoir T=N*dt
x_0=1.                          # Donnee initiale

# Le choix du champ de vitesse F :
def F(t,x):
    return -3*x+2*sin(9*t)

# Initialisation de l'algorithme :
t=[0.]                          # La liste des temps
x=[x_0]                         # La liste des positions au cours du temps

# La methode de Euler-Explicite proprement dite :
for k in range(N):
    x_new=x[k]+dt*F(t[k],x[k])  # Nouvelle position par Euler explicite
    x.append(x_new)             # stockage des resultats
    t.append(t[k]+dt)  

# trace le graphe de la solution obtenue :
plot(t,x,'.k')