##########################################################
### HELPFUL FUNCTIONS FOR SESSION 8 ###########
##########################################################
# --- IMPORTS : 
import numpy as np 
import random as rdm 

def model1(mu, sig): 
    """ 
    MODEL1 is a pure location-scale model : yi = mu + sig*ei
    where ei ~N(0, 1) iid. 
    :param mu: mean 
    :param sig: std div

    :return: f (function handle) for generating observations from model1   
    """ 
    
    def f(x): 
        """ 
        :param x: numpy array st. each row is an observation 
        """
        n = x.shape[0]
        y = []
        for i in range(0, n): 
            ni = rdm.normal()
            y.append(mu + sig*ni)
        return np.array(y)
    return f 

def model2(mu, a, sig, Ex, Vx): 
    """ 
    MODEL2 is a linear regression model : yi = mu + a(xi - E(x)) + sig*ni, ni~N(0,1)
    :param mu: 
    ...
    :return: f (function handle) generates observations from model2 
    """
    def f(x): 
        """
        :param x: numpy array st. each row is an observation 
        """ 
        n = x.shape[0]
        y = []
        for i in range(0, n): 
            ni = rdm.normal() 
            y.append(mu + a*(x[i]-Ex)+ sig*ni)
        return np.array(y)
    return f 

def generateX(Ex, Vx, n): 
    """ 
    GENERATEX generates the dataset of n points xi st. xi~N(Ex, sqrt(Vx))
    :param Ex: (scalar) expectance of x 
    :param Vx: (scalar) variance of x
    :param n: (scalar) number of wanted samples

    :return: 
    """
    y = []
    for i in range(0, n): 
        y.append(rdm.normal(Ex, np.sqrt(Vx)))
    return np.array(y)
