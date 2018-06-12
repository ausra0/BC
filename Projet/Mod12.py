# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
import time
# data (X)
from TestTrain import * # dtrain, dtest 
from Mod11 import *
from Methods1 import *

"""
theta0 = np.array([-4, 3])
print('post at theta0 :')
print(post(theta0, flag))
"""

# --- Importance Sampling Call
# prototype : def IS(h, sampleh, f, S, n)
t0 = time.time()
exp, IC = IS(h, sampleh, post, S, n, flag)
t = time.time() - t0

with open("./times/Mod12.dat", "wb") as file: 
    pickle.dump(t, file)

# --- PRINT OUTPUT : 
print("Theta_hat = "+str(exp)+" +/-"+str(IC))

# --- EXPORT VARIABLES : (X)
with open("./output/M1.dat", "wb") as file:
    pickle.dump([exp, IC], file)
