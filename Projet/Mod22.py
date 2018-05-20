# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
import pickle
# data  (X) 
from TestTrain import * # dtrain, dtest 
from Mod11 import *

# --- ACCEPTANCE-REJECTION ALGORITHM : 
inc = 0
samples = []
while(inc<n):
	theta = sampleP()
	u = rdm.random()
	if u<=1:
		samples.append(theta*cond(theta))
		inc = inc + 1

samples = np.array(samples)
exp =  sum(samples, 0)/n
IC = 1.96*(sum((samples - exp)**2, 0)/(n-1))/np.sqrt(n)

# --- PRINT OUTPUT : 
print("Theta_hat = "+str(exp)+" +/-"+str(IC))

# --- EXPORT VARIABLES : (X)
with open("./output/M2.dat", "wb") as file:
    pickle.dump([exp, IC], file)
