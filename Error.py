# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:54:03 2024

@author: lgcadillac
"""

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

exact=True

if exact :

    dt, e_ee, e_ei, e_cn, e_rk4, e_h, e_ab2, e_rk3 = TraceErreur(F,dF,Solution)
            
    #tracé échelle log-log choix couleurs : 'b','c','g','k','m','r','y','w'
    #loglog(dt,e_ee,'.b')
    loglog(dt,e_ei,'x-k')
    #loglog(dt,e_cn,'.g')
    loglog(dt,e_h,'o-k')
    loglog(dt,e_ab2,'s-k')
    loglog(dt,e_rk3,'-k')
    #loglog(dt,e_rk4,'.m')
    savefig("save.png")

else :
    dt, e_ee, e_ei, e_cn, e_rk4, e_h, e_ab2, e_rk3 =TraceErreurApprox(F,dF)
            
            
    loglog(dt,e_ee,'.b')
    loglog(dt,e_ei,'.r')
    loglog(dt,e_cn,'.g')
    loglog(dt,e_rk4,'.m')
    loglog(dt,e_h,'.y')
    loglog(dt,e_ab2,'.c')
    loglog(dt,e_rk3,'.b')