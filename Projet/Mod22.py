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
n = len(list(tr)) # dimension 
theta0 = np.array([0, 0]) # initial guess
print("post at theta0 :")
print(post(theta0, flag))
maxiter = 400
lamb = 1

# --- Metropolis-Hastings Call
mchain, ratio, exp = MH(theta0, maxiter, lamb, post, flag)

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
