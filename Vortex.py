#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pylab
import numpy as np
import sys

Vor=np.array([[1.,0.,1.],
              [-1.,0.,1.]]) # Une liste de points-vortex

def NormSquare(v): # le carre de la norme d'un vortex
    return np.dot(v,v)

def J(v): #la rotation d'angle pi/2
    return np.array([-v[1],v[0],v[2]])

def F(t,Vor):
    Number=Vor.shape[0]
    VorVel=np.array([[0.,0.,0.] for i in range(Number)])
    for i in range(Number):
        for j in range(i):
            VorVel[i]+=Vor[j][2]*(J(Vor[i]-Vor[j]))/NormSquare(Vor[i]-Vor[j])
            VorVel[j]+=Vor[i][2]*(J(Vor[j]-Vor[i]))/NormSquare(Vor[i]-Vor[j])
    return VorVel

print(F(0,Vor))