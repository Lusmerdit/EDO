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

# Liste des schémas numériques
schemas = ["EE", "EI", "Heun","PMI", "CN", "AB2", "RK3", "RK4", ]

# Erreur attendue pour résoudre cette équation :
epsilon =1.e-9
print("Epsilon = ", epsilon)

# temps d'execution et autres paramètres
elapsed = 0.
dt=2.e-6
T=1.
x_0=1.
N=int(ceil(T/dt))
dt=T/N


# Ajustement du pas de temps optimal pour chaque schema
for schema in schemas:
    dt=1.
    error=1.
    while(error>=epsilon):
        dt/=10.
        solve = eval(schema)
        
        #resolution numérique de l'équation
        start = time()
        t,x=solve(F,dF,dt,T,x_0)
        stop = time()
        
        elapsed = stop - start
        error = ErreurTotale(Solution,x, dt,T,x_0)
    print("Schema = "+schema)
    print(f'Pas de temps opitmal = {dt:.1}')
    print(f'Temps d\'exécution = {elapsed:.6}s')    
    print()












sys.exit()


# Paramètres pour l'intégration numérique

# Départ du chronomètre
start = time()

# Resolution numérique de l'équation :
t,x=solve(F,dF,dt,T,x_0) # solution numérique

