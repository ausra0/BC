# --- IMPORTS : 
import numpy as np 
import numpy.random as rdm 


def defPrior(flag):
# DEFPRIOR returns a function that defines the chosen prior
	# UNNORMALIZED NORMAL PRIOR
    if(flag==1): 
		# define parameters proper to the function 
		mean = np.zeros((2, 1)) 
		var = np.eye(2) # inverse of covariance matrix
		# define prior
		def prior(x):
			return np.exp(-0.5*(x-mean)@var@(x-mean))
	# OTHER PRIOR
    if(flag==2):


def sampleFromPrior(flag): 
	if flag==1: 
		mean = np.zeros((2, 1))
		var = np.eye(2)
		def sample(): 
			return rdm.normal(mean, var)
