# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
# data (X)
from TestTrain import * # dtrain, dtest 
from Mod31 import *
from Methods4 import *

# parameters for laplace
n = len(mu)

# Run Laplace 
theta0 = np.array([0, 0])
mul, sigl = laplace(theta0, logpost, gradlogpost, hesslogpost, n, 1, 0)

# Sanity checks 
print("Proceding to sanity checks")
assert npl.det(sigl)>0
print("done.")

# --- PRINT OUTPUT : 
print("Theta_hat = "+str(mul))

# --- EXPORT VARIABLES : (X)
with open("./output/M3.dat", "wb") as file:
    pickle.dump([mul, sigl], file)
