#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import sys
import Schemas as Sc

Vor=np.array([[1.,0.,2.],
              [-1.,0.,-1.],
              [-1.,0.2,-1.]]) # Une liste de points-vortex

def NormSquare(v): # Le carre de la norme d'un vortex
    return np.dot(v,v)

def J(v): # La rotation d'angle pi/2
    return np.array([-v[1],v[0],v[2]])

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
            cla()
            ax = plt.gca()
            ax.set_aspect('equal')
            xlim(-2.5,2.5)
            ylim(-2.5,2.5)
            for i in range(len(Vor)):
                plot([Vort[k][i][0]],[Vort[i][2][1]],'.k')
            savefig('Screen-'+str(k))

t, Vort = Sc.RK4(F,0,0.05,10.,Vor)
SaveScreenShots(t,Vort)
