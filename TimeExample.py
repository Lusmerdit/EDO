# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:43:29 2024

@author: lgcadillac
"""
from time import *

start = time()

a=1.
for i in range(100000000):
        a /= (i+1)

end = time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.3}s')