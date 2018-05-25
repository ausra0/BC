# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
# data (X)
from TestTrain import * # dtrain, dtest 
from Mod11 import *
from Methods1 import *


# --- Importance Sampling Call
exp, IC = IS(prior, sampleP, prior, S, n)

# --- PRINT OUTPUT : 
print("Theta_hat = "+str(exp)+" +/-"+str(IC))

# --- EXPORT VARIABLES : (X)
with open("./output/M1.dat", "wb") as file:
    pickle.dump([exp, IC], file)
