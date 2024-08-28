#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import sys
import Schemas as Sc

Vor=np.array([[1.,sqrt(2),-1.],
              [-1.,0.,2.],
              [1.,0.,2.]]) # Une liste de points-vortex

def NormSquare(v): # Le carre de la norme d'un vortex

    return v[0]**2+v[1]**2

def J(v): # La rotation d'angle pi/2
    return np.array([-v[1],v[0],0.])

def F(t,Vor):
    Number=Vor.shape[0]
    VorVel=np.array([[0.,0.,0.] for i in range(Number)])
    for i in range(Number):
        for j in range(i):
            DistSquare=NormSquare(Vor[i]-Vor[j])
            VorVel[i]+=Vor[j][2]*(J(Vor[i]-Vor[j]))/DistSquare
            VorVel[j]+=Vor[i][2]*(J(Vor[j]-Vor[i]))/DistSquare
    return VorVel

def SaveScreenShots(t,Vort,N=-1): # Save N screenshots of the dynamics
    if N==-1:
        for k in range(len(t)):
            if k%2==0:
                cla()
                ax = plt.gca()
                ax.set_aspect('equal')
                xlim(-3,3)
                ylim(-3,3)
                for i in range(len(Vor)):
                    plot([Vort[k][i][0]],[Vort[k][i][1]],'.k')
                savefig('Screen-'+str(k))
                
dt=0.0001
T=21400*dt

t, Vort = Sc.RK4(F,0,dt,T,Vor)

#SaveScreenShots(t,Vort)
cla()
ax = plt.gca()
ax.set_aspect('equal')
xlim(-2,2)
ylim(-2,2)
plot([Vort[k][0][0] for k in range(len(t))],[Vort[k][0][1] for k in range(len(t))],'r')
plot([Vort[k][1][0] for k in range(len(t))],[Vort[k][1][1] for k in range(len(t))],'g')
plot([Vort[k][2][0] for k in range(len(t))],[Vort[k][2][1] for k in range(len(t))],'b')