# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
# data (X)
from TestTrain import * # dtrain, dtest 
from Mod21 import *
from Methods2 import * # Metropolis-Hastings

# --- Define variables for Metropolis Hastings 
n = 2
theta0 = 6*np.ones(n)
maxiter = 1000
lamb = 2.4*(n**(-0.5))
# optimal lambda is given by 2.4*(n**(-0.5))*scale of target

# --- Metropolis-Hastings Call
mchain, ratio, exp = MH(theta0, maxiter, lamb, post)
"""
# --- Importance Sampling Call
exp, IC = IS(prior, sampleP, post, S, n) 
"""
"""
# --- COMPUTE IC : 
IC = 1.95*sum((samples - expf)**2)/(n*np.sqrt(n))
"""

# --- SANITIY CHECK : 
print("Acceptance ratio : "+str(ratio))
print("Running ratio sanity test...")
if (0.1<=ratio and ratio<=0.6):
    print("passed")
else: 
    print("failed")

# --- PRINT OUTPUT : 
#print("Theta_hat = "+str(exp)+" +/-"+str(IC))
print("Theta_hat = "+str(exp))

# --- EXPORT VARIABLES : (X)
with open("./output/M2.dat", "wb") as file:
    pickle.dump([exp], file)

# Plot 
import matplotlib.pyplot as plt
chainx = [mchain[i][0] for i in range(0, len(mchain))]
chainy = [mchain[i][1] for i in range(0, len(mchain))]

plt.plot(chainx, chainy)
plt.show()
