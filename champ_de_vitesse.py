#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:19:45 2025

@author: lgcadillac
"""

from Schemas import *
import matplotlib.pyplot as plt
import numpy as np

# Le choix du champ de vitesse F :
def F(t,V):
    return np.array([(1-4*(V[0]+V[1])**2)/sqrt((1-4*(V[0]+V[1])**2)**2+(1+2*(V[0]-V[1]))**2+0.1), 
                     (1+2*(V[0]-V[1]))/sqrt((1-4*(V[0]+V[1])**2)**2+(1+2*(V[0]-V[1]))**2+0.1)])

# Le calcul de sa derivee (pour Newton) :
def dF(t,X):
    return 0

X, Y = np.meshgrid(np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1))
U, V = np.meshgrid(np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1))

for i in range(len(X)):
    for j in range(len(X[i])):
        U[i][j] = F(0,[X[i][j],Y[i][j]])[0]
        V[i][j] = F(0,[X[i][j],Y[i][j]])[1]
        
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V, pivot='mid', scale =25)

plt.cla()
# Choix du schéma numérique : EE, EI, CN, Heun, RK3, RK4, AB2, PMI
solve = RK4

# Paramètres pour l'intégration numérique
dt=0.01
T=5.
x_0=np.array([0.12,-1.])
N=int(ceil(T/dt))
dt=T/N

# Resolution numérique de l'équation :
t,V=solve(F,dF,dt,T,x_0) # solution numérique
    
A=[I[0] for I in V]
B=[I[1] for I in V]

plot(A, B, '-r')
plt.xlim(-1,1)
plt.ylim(-1,1)

plt.show()