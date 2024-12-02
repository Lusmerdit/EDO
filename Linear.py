# -*- coding: utf-8 -*-

from pylab import *
from Schemas import *
import sys

mu =1.

# Le choix du champ de vitesse F :
def F(t,x):
    return -3*lam*x+2*lam*sin(9*t)


# Le calcul de sa derivee (pour Newton) :
def dF(t,x):
    return -3*lam

# Solution exacte de l'EDO
def Solution(t,x_0):
    return (x_0+1./5)*exp(-3.*t)+sin(9.*t)/15-cos(9*t)/5


# Choix du schéma numérique : EE, EI, CN, Heun, RK3, RK4, AB2, PMI
solve = AB2

# Paramètres pour l'intégration numérique
dt=2.e-2
T=1.
x_0=1.
N=int(ceil(T/dt))
dt=T/N

# Resolution numérique de l'équation :
t,x=solve(F,dF,dt,T,x_0) # solution numérique

t_sol=[n*1e-2 for n in range(int(ceil(1e2*T)))]
x_sol=[Solution(n*1e-2,x_0) for n in range(int(ceil(1e2*T)))] #solution exacte
plot(t_sol,x_sol,'r') #tracé de la solution exacte
#cla()
plot(t,x,'.b') #tracé de la solution numérique
savefig('plot.png')

sys.exit()


# Calcul de l'erreur exacte
print(ErreurTotale(Solution,x, dt,T,x_0))

# Calcul de l'erreur approchée
x2=solve(F,dF,dt/2.,1.,1.)[1]
print(ErreurEmpirique(x,x2))

# Calcul de l'ordre empirique approché
x4=solve(F,dF,dt/4.,1.,1.)[1]
print(log2(ErreurEmpirique(x,x2)/ErreurEmpirique(x2,x4)))

sys.exit()


for i in range(100):
    cla()
    xlim(0.,5.)
    ylim(-0.4,1.)
    plot(t_sol,x_sol,'r')
    plot(t[:2*i],x[:2*i],'.b')
    savefig('plot-'+str(i)+'.png')

