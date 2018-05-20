#################################################
############## SAMPLING METHODS II ##############
#################################################
# --- CONTAINS :
# GS            Gibbs Sampling 
# 
# --- PROTOTYPES : 
# 
# --- REQUIRES : 
# 
#################################################

import random as rdm
import math 
import numpy.random as nprdm
import numpy as np

def sample(d, k, sampleopt): 
# samples a random index from {1, ..., d}
# --- IN : 
# d             scalar          size of dimension (of theta)
# k             scalar          current step
# sampleopt     scalar          option for sampling 
#                               1) balanced rdm update 
#                               2) unbalanced rdm update 
#                               3) sequential updates
# --- OUT : 
# indx          scalar          the chosen index 
# ----------------------------------------------
    if(sampleopt==1): 
        indx = math.floor(rdm.random()*d)
    if(sampleopt==2): 
        indx = 0
    if(sampleopt==3): 
        indx = k%d        
    return indx



def fromconddist(indx, d, theta):
# FROMCONDDIST samples from some cond. distribution specified beneath
# --- IN: 
# indx          scalar          index which is not fixed in conditional dist. 
# d             scalar          dimension of theta
# --- OUT : 
# thetanew      scalar          sample from f(theta_indx|theta_-indx, d)
# ---------------------------------------------
    # problem definition (normal)
    B = np.eye(d)

    # deduce parameters for sampling 
    sigma = np.sqrt(1/B[indx, indx])
    mu = np.dot(B[indx, :], theta)
    
    # sample
    thetanew = nprdm.normal(mu, sigma, 1)

    return thetanew



def GS(theta0, samplopt, maxiter):
# GS is the implementation of Gibbs Sampling 
# -- IN : 
# theta0        list            chain initialisation
# samplopt      scalar          option for sampling 
#                               (cf. *sample* function)
# maxiter       scalar          maximum number of iterations 
# ----------------------------------------------
    theta = theta0
    thetamem = theta
    k = 0
    d = len(theta)
    while(k<maxiter): 
        k = k+1
        # choose update index: 
        indx = sample(d, k, samplopt)
        # sample from cond. dist. 
        newtheta = fromconddist(indx, d, theta)
        # update theta 
        theta[indx] = newtheta
        print(theta)
        # update the memory 
        thetamem = [thetamem[i] + theta[i] for i in range(0, d)]
    
    print(k)
    return [thetamem[i]/k for i in range(0, d)]
