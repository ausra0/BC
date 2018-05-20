# --- IMPORTS : 
# basic
import numpy as np 
import numpy.random as rdm 
# data
from TestTrain import * # dtrain, dtest 

# --- DEFINE IMPORTANT FUNCTIONS : 
mean = np.zeros((2, 1))
S = np.eye(2)

def prior(x):
	return np.exp(-0.5*(x-mean)@K@(x-mean))

def sampleP(): 
	return rdm.multicariate_normal(mean, S)

def cond(x, indx): 
	return 

inc = 0
samples = []
while(inc<n):
	theta = sampleh()
	u = rdm.random()
	if u <= (f(theta)/(K*h(theta))):
		samples.append(theta)
		inc = inc + 1

	exp =  sum(S(samples))/len(samples)
	var = 1.96*(sum((S(samples) - exp)**2)/(len(samples)-1))/np.sqrt(n)

