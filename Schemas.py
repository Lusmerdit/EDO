# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pylab import *

# La methode de Euler-Explicite dans une fonction :
def EE(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        x.append(x[k]+dt*F(t[k],x[k]))
        t.append(t[k]+dt)  
    return t,x


# La methode de Heun :
def Heun(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]           
    for k in range(N):
        p=x[k]+dt*F(t[k],x[k])   #Calcul du predicteur
        c=x[k]+dt*F(t[k]+dt,p)   #Calcul du correcteur
        x.append(0.5*(p+c))      #Le pas avec correction
        t.append(t[k]+dt)  
    return t,x

# La methode de Runge-Kutta 4:
def RK4(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        k1 = F(t[k], x[k])
        k2 = F(t[k]+dt/2, x[k]+dt*k1/2)
        k3 = F(t[k]+dt/2, x[k]+dt*k2/2)
        k4 = F(t[k]+dt, x[k]+dt*k3)
        x.append(x[k] + dt*(k1+2*k2+2*k3+k4)/6)
        t.append(t[k]+dt)  
    return t,x

# La methode de Runge-Kutta 3 (Heun 3):
def RK3(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        k1 = F(t[k], x[k])
        k2 = F(t[k]+dt/3, x[k]+dt*k1/3)
        k3 = F(t[k]+2*dt/3, x[k]+dt*2*k2/3)
        x.append(x[k] + dt*(k1+3*k3)/4)
        t.append(t[k]+dt)  
    return t,x


# La methode de Adams-Bashforth 2 dans une autre fonction.
# La donnee initiale est un vecteur de taille 2 avec x_0 et x_1 :
def AB2(F,dF,dt=0.01,T=1., x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N                         
    t,x=Heun(F,dF,dt,dt,x_0) # le premier pas de l'algorithme se fait avec Heun
    for k in range(1,N):
        x.append(x[k]+dt*(3.*F(t[k],x[k])/2.-F(t[k-1],x[k-1])/2.))
        t.append(t[k]+dt)
    return t,x

    
# l'algorithme de Newton prend en argument une fonction f, sa derivee df,
# une donnee initiale a et une erreur maximale e
def Newton(f,df,a,e):
    delta = 1
    while delta > e:
        x = -f(a)/df(a) + a
        delta = abs(x - a)
        a = x
    return x

# Euler Implicite avec la methode de Newton
def EI(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        f = lambda y : y-dt*F(t[k]+dt,y)-x[k]   # la fonction a inverser
        df = lambda z : 1-dt*dF(t[k]+dt,z)      # sa derivee
        x_init = x[k]+dt*F(t[k],x[k])           # initialise Newton
        x.append(Newton(f,df,x_init,1e-12))     # un pas de Euler implicite
        t.append(t[k]+dt)  
    return t,x

# Crank-Nicholson avec la methode de Newton
def CN(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        f = lambda y : y-dt*F(t[k]+dt,y)/2-x[k]-dt*F(t[k],x[k])/2   # la fonction a inverser
        df = lambda z : 1-dt*dF(t[k]+dt,z)/2    # sa derivee
        x_init = x[k]+dt*F(t[k],x[k])           # initialise Newton
        x.append(Newton(f,df,x_init,1.e-12))    # un pas de Crank-Nicolson
        t.append(t[k]+dt)  
    return t,x

# Point-Milieu implicite
def PMI(F,dF,dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    t=[0.]                          
    x=[x_0]                         
    for k in range(N):
        f = lambda y : y-dt*F(t[k]+dt/2.,(y-x[k])/2.)-x[k]      # la fonction a inverser
        df = lambda z : 1-dt*dF(t[k]+dt/2.,(z-x[k])/2.)/2.      # sa derivee
        x_init = x[k]+dt*F(t[k],x[k])                           # initialise Newton
        x.append(Newton(f,df,x_init,1e-12))                     # un pas de point-milieu implicite
        t.append(t[k]+dt)  
    return t,x

# Calcule l'erreur exacte d'un schema
def ErreurTotale(solution, x1=[], dt=0.01,T=1.,x_0=0.):
    N=int(ceil(T/dt))
    dt=T/N
    Error=0.
    for k in range(len(x1)):
        Error+=max(Error,abs(x1[k]-solution(k*dt,x_0)))
    return Error



# Trace les erreurs empiriques en fonction de Delta_t sur une échelle log-log
def TraceErreur(dt=1.,T=1.,K=18,x_0=1.):
    
    # Variables pour stocker les résultats de l'algorithme
    Dt=[]
    E_EE=[]
    E_EI=[]
    E_CN=[]
    E_RK4=[]
    E_H=[]
    E_AB2=[]
    E_RK3=[]
    
    for k in range(K):
        print(k)
                
        x_EE=EE(F,dF,dt,T,x_0)[1]
        x_EI=EI(F,dF,dt,T,x_0)[1]
        x_CN=CN(F,dF,dt,T,x_0)[1]
        x_RK4=RK4(F,dF,dt,T,x_0)[1]
        x_H=Heun(F,dF,dt,T,x_0)[1]
        x_AB2=AB2(F,dF,dt,T,x_0)[1]
        x_RK3=RK3(F,dF,dt,T,x_0)[1]
        
        E_EE.append(max(ErreurTotale(Solution,x_EE,dt,T,x_0),10e-12))
        E_EI.append(max(ErreurTotale(Solution,x_EI,dt,T,x_0),10e-12))
        E_CN.append(max(ErreurTotale(Solution,x_CN,dt,T,x_0),10e-12))
        E_RK4.append(max(ErreurTotale(Solution,x_RK4,dt,T,x_0),10e-12))
        E_H.append(max(ErreurTotale(Solution,x_H,dt,T,x_0),10e-12))
        E_AB2.append(max(ErreurTotale(Solution,x_AB2,dt,T,x_0),10e-12))
        E_RK3.append(max(ErreurTotale(Solution,x_RK3,dt,T,x_0),10e-12))
        
        Dt.append(dt)
        dt=dt/2.
    
    return Dt, E_EE, E_EI, E_CN, E_RK4, E_H, E_AB2, E_RK3
        
 
#Dt, E_EE, E_EI, E_CN, E_RK4, E_H, E_AB2, E_RK3 = TraceErreur()
        
# Tracé échelle log-log Choix couleurs : 'b','c','g','k','m','r','y','w'
#loglog(Dt,E_EE,'.b')
#loglog(Dt,E_EI,'.r')
#loglog(Dt,E_CN,'.g')
#loglog(Dt,E_H,'.y')
#loglog(Dt,E_AB2,'.c')
#loglog(Dt,E_RK3,'.b')
#loglog(Dt,E_RK4,'.m')

# Calcule l'erreur empirique d'un schema
def ErreurEmpirique(x1=[], x2=[]):
    Error=0.
    for k in range(len(x1)-1):
        Error+=max(Error,abs(x1[k]-x2[2*k]))
    return Error

# Trace les erreurs empiriques en fonction de Delta_t sur une échelle log-log
def TraceErreurApprox(dt=0.2,T=1.,K=15):
    
    # Initialisation avec le plus grand pas de temps
    x_EE=EE(F,dt,T,1.)[1]
    x_EI=EI(F,dF,dt,T,1.)[1]
    x_CN=CN(F,dF,dt,T,1.)[1]
    x_RK4=RK4(F,dt,T,1.)[1]
    x_H=Heun(F,dt,T,1.)[1]
    x_AB2=AB2(F,dt,T,1.)[1]
    
    # Variables pour stocker les résultats de l'algorithme
    Dt=[]
    E_EE=[]
    E_EI=[]
    E_CN=[]
    E_RK4=[]
    E_H=[]
    E_AB2=[]
    
    for k in range(K):
        print(k)
        # On divise le pas de temps par $2$
        Dt.append(dt)
        dt=dt/2.
        
        x_EE_2=EE(F,dt,T,1.)[1]
        x_EI_2=EI(F,dF,dt,T,1.)[1]
        x_CN_2=CN(F,dF,dt,T,1.)[1]
        x_RK4_2=RK4(F,dt,T,1.)[1]
        x_H_2=Heun(F,dt,T,1.)[1]
        x_AB2_2=AB2(F,dt,T,1.)[1]
        
        E_EE.append(ErreurEmpirique(x_EE,x_EE_2))
        E_EI.append(ErreurEmpirique(x_EI,x_EI_2))
        E_CN.append(ErreurEmpirique(x_CN,x_CN_2))
        E_RK4.append(ErreurEmpirique(x_RK4,x_RK4_2))
        E_H.append(ErreurEmpirique(x_H,x_H_2))
        E_AB2.append(ErreurEmpirique(x_AB2,x_AB2_2))  
        
        x_EE=x_EE_2
        x_EI=x_EI_2
        x_CN=x_CN_2
        x_RK4=x_RK4_2
        x_H=x_H_2
        x_AB2=x_AB2_2
    
    return Dt, E_EE, E_EI, E_CN, E_RK4, E_H, E_AB2
        
 
#Dt, E_EE, E_EI, E_CN, E_RK4, E_H, E_AB2=TraceErreurApprox()
        
        
# Tracé échelle log-log Choix couleurs : 'b','c','g','k','m','r','y','w'
#loglog(Dt,E_EE,'.b')
#loglog(Dt,E_EI,'.r')
#loglog(Dt,E_CN,'.g')
#loglog(Dt,E_RK4,'.m')
#loglog(Dt,E_H,'.y')
#loglog(Dt,E_AB2,'.c')
