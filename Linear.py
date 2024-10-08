# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:35:18 2024

@author: lgcadillac
"""

from pylab import *
from Schemas import *

# Le choix du champ de vitesse F :
def F(t,x):
    return -3*x+2*sin(9*t)


# Le calcul de sa derivee (pour Newton) :
def dF(t,x):
    return -3

# Solution exacte de l'EDO
def Solution(t,x_0):
    return (x_0+1./5)*exp(-3.*t)+sin(9.*t)/15-cos(9*t)/5


# Trace le graphe de la solution obtenue :
dt=0.03
T=5.
x_0=1.
N=int(ceil(T/dt))
dt=T/N
t,x=RK4(F,dF,dt,T,x_0) # solution numérique
t_sol=[n*1e-4 for n in range(int(ceil(1e4*T)))]
x_sol=[Solution(n*1e-4,x_0) for n in range(int(ceil(1e4*T)))] #solution exacte
plot(t_sol,x_sol,'r')
cla()
plot(t,x,'.b')
savefig('plot.png')

for i in range(100):
    cla()
    xlim(0.,5.)
    ylim(-0.4,1.)
    plot(t_sol,x_sol,'r')
    plot(t[:2*i],x[:2*i],'.b')
    savefig('plot-'+str(i)+'.png')

print(ErreurTotale(Solution,x, dt,T,x_0))

print(ErreurEmpirique(RK4(F,2e-1,1.,1.)[1],RK4(F,1.e-1,1.,1.)[1]))