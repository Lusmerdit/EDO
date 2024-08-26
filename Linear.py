# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:35:18 2024

@author: lgcadillac
"""

from pylab import *
from Schemas.py import *

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
dt=0.2
T=1.
x_0=1.
N=int(ceil(T/dt))
dt=T/N
t,x=RK3(F,dF,dt,T,x_0) # solution numérique
t_sol=[n*1e-4 for n in range(int(ceil(1e4*T)))]
x_sol=[Solution(n*1e-4,x_0) for n in range(int(ceil(1e4*T)))] #solution exacte
plot(t_sol,x_sol,'r')
plot(t,x,'.b')

#print(ErreurEmpirique(RK4(F,2e-4,1.,1.)[1],RK4(F,1.e-4,1.,1.)[1]))