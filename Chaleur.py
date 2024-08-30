#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import sys
import Schemas as Sc


N=100
Cha=np.array([(i/N)*(1.-i/N)*(cos(7*i/N)**2+cos(3*i/N)**2) for i in range(N+1)])
X=np.array([i/N for i in range(N+1)])
        
def F(t,Cha,Lambda=1.):
    ChaVel=np.array([0. for i in range(len(Cha))])
    for i in range(1,N):
        ChaVel[i]+=Lambda*(Cha[i-1]+Cha[i+1]-2*Cha[i])
    return ChaVel
        
xlim(0.,1.)
ylim(0.,0.26)
plot(X, Cha, '.k')
savefig('chaleur-'+str(0)+'.png')

dt=0.5
T=1000*dt
t, Chat= Sc.RK4(F,0,dt,T,Cha)
plot(X, Chat[1000], '.r')


for i in range(100):
    cla()
    xlim(0.,1.)
    ylim(0.,0.26)
    plot(X,Chat[10*i],'.k')
    savefig('chaleur-'+str(i+1)+'.png')