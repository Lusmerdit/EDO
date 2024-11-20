# -*- coding: utf-8 -*-
from pylab import *
from Schemas import *
from time import *

# Le choix du champ de vitesse F :
def F(t,x):
    return -3*x+2*sin(9*t)


# Le calcul de sa derivee (pour Newton) :
def dF(t,x):
    return -3

# Solution exacte de l'EDO
def Solution(t,x_0):
    return (x_0+1./5)*exp(-3.*t)+sin(9.*t)/15-cos(9*t)/5

# Choix du schéma numérique : EE, EI, CN, Heun, RK3, RK4, AB2, PMI
solve = EE

# Paramètres pour l'intégration numérique
dt=2.e-6
T=1.
x_0=1.
N=int(ceil(T/dt))
dt=T/N

# Départ du chronomètre
start = time()

# Resolution numérique de l'équation :
t,x=solve(F,dF,dt,T,x_0) # solution numérique

# Fin du chronométre
end = time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.3}s')
