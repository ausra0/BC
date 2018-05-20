################################################
######## USEFUL FUNCTIONS FOR SESSION 2 ########
################################################

import numpy as np 

def normal1d(mu, sigma):
    """ 
    NORMAL1D computes the normal distribution in 1D 
    :param mu: (scalar) mean 
    :param sigma: (scalar) standard deviation 
    :return: f (function handle) normal dist. 
    """ 
    def f(x): 
        return np.exp(-0.5*((x-mu)**2)/(sigma**2))
    return f

def gamma1d(alpha, beta): 
    """ 
    GAMMA1D computes the gamma distribution with 
    parameters alpha, beta in 1D 
    :param alpha: (scalar) dist. param.
    :param beta: (scalar) dist. param.
    :return: f (function handle) gamma dist. 
    """ 
    def f(x): 
        return (x**(alpha -1))*np.exp(-beta*x)
    return f
