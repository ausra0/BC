# --- IMPORTS  
import numpy as np  
import numpy.random as rdm 

def SampleLogit(theta): 
    u = rdm.random()
    y = 1/theta *np.log(np.exp(theta*u)-1)
    return y

# --- SANITY CHECK 
n = 1000 #number of samples 
mem = []
theta = -1

for i in range(0, n):
    mem.append(SampleLogit(theta))

import matplotlib.pyplot as plt 

bins = np.linspace(min(mem), max(mem), 50)
plt.hist(mem, bins, alpha=0.7)
plt.show()
