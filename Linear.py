# -*- coding: utf-8 -*-

from pylab import *
from Schemas import *
import sys

mu =1.

# Le choix du champ de vitesse F :
def F(t,x):
    return -3*mu*x+2*mu*sin(9*t)


# Le calcul de sa derivee (pour Newton) :
def dF(t,x):
    return -3*mu

# Solution exacte de l'EDO
def Solution(t,x_0):
    return (((3*mu*mu+27)*x_0+6*mu)*exp(-3*mu*t)+2*mu*mu*sin(9*t)-6*mu*cos(9*t))/(3*mu*mu+27)


# Choix du schéma numérique : EE, EI, CN, Heun, RK3, RK4, AB2, PMI
solve = EI

# Paramètres pour l'intégration numérique
dt=1
T=20.
x_0=1.
N=int(ceil(T/dt))
dt=T/N

# Resolution numérique de l'équation :
t,x=solve(F,dF,dt,T,x_0) # solution numérique

t_sol=[n*1e-2 for n in range(int(ceil(1e2*T)))]
x_sol=[Solution(n*1e-2,x_0) for n in range(int(ceil(1e2*T)))] #solution exacte
plot(t_sol,x_sol,'0.5') #tracé de la solution exacte
#cla()
plot(t,x,'.k') #tracé de la solution numérique
savefig('plot.png',dpi=200)

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

