import random as rdm
import numpy as np 

def generateData(n, m):
    c = []
    p = []
    for i in range(0, n):
        # class apartemance
        c.append(np.ceil(m*rdm.random()))
        # class probability 
        p.append(rdm.random())

    # count number of people
    ni = []
    for i in range(0, n): 
        ni.append(c.count(i+1))

    # generate x 
    x = []
    for i in range(0, n): 


    data = [(x[i], c[i]) for i in range(0, n)]
    return c

n = 100
m = 4
c = generateData(n, m)

