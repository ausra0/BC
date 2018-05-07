##################################################
################ Useful Utilties #################
##################################################
# Needs testing
# --- IMPORTS : 
import numpy as np 


def logNormal(mu, Sigma): 
    def f(x): 
        return 0.5*np.transpose(x-mu)@Sigma@(x-mu)
    return f

def gradLogNormal(mu, Sigma): 
    def f(x): 
        return Sigma@(x-mu)
    return f

def hessLogNormal(mu, Sigma): 
# Sigma is the inverse of the covariance
    def f(x):
        return Sigma
    return f
