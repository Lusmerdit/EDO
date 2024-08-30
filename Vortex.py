#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import sys
import Schemas as Sc
import random
random.seed(0)

 # Une liste de points-vortex. Les vortex auto similaires : np.array([[1.,sqrt(2),-1.],[-1.,0.,2.],[1.,0.,2.]]) 
global Vor
Vor=[]

def addVortex(x=0.,y=0.,a=0., rand_position=-1, rand_circulation=-1):
    if rand_position>0:
        x=random.uniform(-rand_position,rand_position)
        y=random.gauss(-rand_position,rand_position)
    if rand_circulation>0:
        a=random.gauss(0.,rand_circulation)
    Vor.append(np.array([x,y,a]))
    
def NormSquare(v, epsilon=0.): # Le carre de la norme d'un vortex

    return v[0]**2+v[1]**2+epsilon

def J(v): # La rotation d'angle pi/2
    return np.array([-v[1],v[0],0.])

def F(t,Vor):
    Number=len(Vor)
    VorVel=np.array([[0.,0.,0.] for i in range(Number)])
    for i in range(Number):
        for j in range(i):
            DistSquare=NormSquare(Vor[i]-Vor[j],0.1)
            VorVel[i]+=Vor[j][2]*(J(Vor[i]-Vor[j]))/DistSquare
            VorVel[j]+=Vor[i][2]*(J(Vor[j]-Vor[i]))/DistSquare
    return VorVel

def SaveScreenShots(t,Vort,N=-1): # Save N screenshots of the dynamics
    if N==-1:
        for k in range(len(t)):
            if True:
                cla()
                ax = plt.gca()
                ax.set_aspect('equal')
                xlim(-3,3)
                ylim(-3,3)
                for i in range(len(Vor)):
                    plot([Vort[k][i][0]],[Vort[k][i][1]],'.k')
                savefig('Screen-'+str(k))
                
for k in range(300):
    addVortex(0.,0.,0.,2.,1.)
for k in range(5000):
    addVortex(0.,0.,0.,4.,-1.)
                
dt=0.02
T=200*dt

t, Vort = Sc.RK4(F,0,dt,T,Vor)

print("Saving screen shots")
SaveScreenShots(t,Vort)

sys.exit()
# Plot the orbits :
cla()
ax = plt.gca()
ax.set_aspect('equal')
xlim(-10,10)
ylim(-10,10)
plot([Vort[k][0][0] for k in range(len(t))],[Vort[k][0][1] for k in range(len(t))],'r')
plot([Vort[k][1][0] for k in range(len(t))],[Vort[k][1][1] for k in range(len(t))],'g')
plot([Vort[k][2][0] for k in range(len(t))],[Vort[k][2][1] for k in range(len(t))],'b')