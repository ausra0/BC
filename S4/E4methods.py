######################################################
################# SAMPLING METHODS I #################
######################################################
# --- CONTAINS :
# IS        Importance Sampling 
# AR        Acceptance-Rejection 
#
# --- PROTOTYPES : 
# def IS(h, sampleh, f, S, n):
#   return expf, var
# def AR(h, sampleh, f, K, S, n):
#   return exp, var
######################################################
import random as rdm 
import numpy as np

def IS(h, sampleh, f, S, n): 
"""
IS is the implementation of the Importance Sampling method
:param h: (function handle) proposal distribution 
:param sampleh: (function handle) function that samples from proposal
:param f: (function handle) target distribution
:param S: (function handle) we want : E[S(theta)]
:param n: (scalar) number of samples wanted

:return: expf, var 
"""
    weight = 0
    exp = 0
    samples = []
    for i in range(0, n): 
        theta = sampleh()
        wi = f(theta)/h(theta)
        samples.append(wi*theta)
        weight += wi
        exp += wi*S(theta)
    
    samples = [samples[i]/weight for i in range(0, n)]
    expf = exp/weight
    var = 1.95*sum((samples - expf)**2)/(n*np.sqrt(n))

    return expf, var

def AR(h, sampleh, f, K, S, n):
"""
 AR is the implementation of Acceptance-Rejection Sampling technique 
:param h: (function handle) proposal distribution 
:param sampleh: (function handle) function that samples from proposal
:param f: (function handle) target distribution 
:param K: (scalar) constant st f(theta|d) <=K*h(theta)
:param S: (function handle) we want E[S(theta)]
:param n: (scalar) number of samples wanted 

:return: 
"""
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
    return exp, var 
