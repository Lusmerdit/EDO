# -*- coding: utf-8 -*-
from Schemas import *
from time import *

start = time()

a=1.

for i in range(100000000):
        a /= (i+1)

end = time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.2}s')
