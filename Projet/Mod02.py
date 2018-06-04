# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
# data (X)
from TestTrain import * # dtrain, dtest 
from Mod01 import *
#from Methods1 import *
from Methods2 import *

# --- Importance Sampling Call
#exp, IC = IS(h, sampleh, post, S, n)

# --- Define variables for M-H
theta0 = np.array([-4, 3])
maxiter = 1000
lamb = 1

# --- Metropolis-Hastings call 
mchain, ratio, exp = MH(theta0, maxiter, lamb, post)


# --- PRINT OUTPUT : 
#print("Theta_hat = "+str(exp)+" +/-"+str(IC))
print(ratio, exp)

# --- DO PLOT : 
import matplotlib.pyplot as plt 
plt.plot(np.array(mchain)[:, 0], np.array(mchain)[:, 1])
plt.show()

# --- EXPORT VARIABLES : (X)
with open("./output/M0.dat", "wb") as file:
    #pickle.dump([exp, IC], file)
    pickle.dump([mchain, ratio, exp], file)
