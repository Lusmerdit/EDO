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
solve = EI

# Paramètres pour l'intégration numérique
dt=2.e-5
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


t_sol=[n*1e-2 for n in range(int(ceil(1e2*T)))]
x_sol=[Solution(n*1e-2,x_0) for n in range(int(ceil(1e2*T)))] #solution exacte
plot(t_sol,x_sol,'0.5') #tracé de la solution exacte
#cla()
plot(t,x,'.k') #tracé de la solution numérique


print(f'Temps d\'exécution : {elapsed:.6}s')
