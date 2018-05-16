######################################################
########## FUNCTIONS NEEDED FOR EXERCICE 4 ###########
######################################################
# --- CONTAINS :
# generateGaussianHandle          define gaussian function h.
# generateGaussianSamplingHandle  define sampling handle
#
# --- PROTOTYPES : 
# def generateGaussianHandle(mu, sigma): 
#      f (function handle)
# def generateGaussianSamplingHandle(mu, sigma): 
#      samplef (function handle) 
#
# --- REQUIRES : 
# numpy             as np
######################################################
import numpy as np 
import random as rdm 
from scipy.stats import norm 

print('Loaded functions of exercice 3')

def generateGaussianHandle(mu, sigma): 
    def f(x): 
        return 1/np.sqrt(2*np.pi*(sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
    return f

def generateGaussianSamplingHandle(mu, sigma): 
    def samplef(): 
        u = rdm.random()
        return norm.ppf(u)
    return samplef
