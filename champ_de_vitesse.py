#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 09:19:45 2025

@author: lgcadillac
"""

from Schemas import *
import matplotlib.pyplot as plt
import numpy as np
from sys import exit

ax = plt.figure().add_subplot(projection='3d')

# Make the direction data for the arrows
x, y, z = np.meshgrid(np.arange(0., 1., 0.1),
                      np.arange(0., 1., 0.1),
                      np.arange(0., 1., 0.1))

u = -y
v = x
w = -z

def f(x,y,z):
    return [-y,x,1+0.2*z]



ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, color = 'k')

plt.show()
