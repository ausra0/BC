#####################################################
############### VARIATIONAL METHODS #################
#####################################################
# convergence not working .... 

# --- IMPORTS 
import numpy as np 
import scipy.linalg as sla # for matrix exp
import numpy.linalg as npl # for norm
import numpy.random as rdm 
#from Tools import * # gradLogNormal, hessLogNormal

# --- AUXILIARY FUNCTION 
def ELBO(l, eta, mu, L, phi): 
    # define and intialize
    d = len(mu)
    elbo = [0]*l 
    # precompute 
    eL = sla.expm(L)

    # simulation 
    for i in range(0, l): 
        elbo[i] = phi(mu + eL@eta[:, i])
    elbo = np.mean(elbo)
    elbo += d/2*np.log(2*np.pi*np.e) + np.trace(L)

    return elbo




def dmuELBO(l, eta, mu, L, gradphi):
    # intialize and precompute
    dmuelbo = []
    eL = sla.expm(L) 

    # simulate 
    for i in range(0, l):
        # make sure a is a 2D shape
        a = eta[:, i].reshape((-1, 1))

        dmuelbo.append(gradphi(mu + eL@a))
    dmuelbo = np.mean(dmuelbo, 0)

    return -dmuelbo 



def sym(A): 
    """ 
    SYM computes the symetrized
    :param A: (matrix) 
    :return: 
    """
    S = 0.5*(A + np.transpose(A))
    return S



def dLELBO(l, eta, mu, L, hessphi): 
    # initialize and precompute 
    dlelbo = []
    eL = sla.expm(L)

    #simulate
    for i in range(0, l): 
        dlelbo.append(hessphi(mu + eL@eta[:, i]))
    dlelbo = np.mean(dlelbo, 0)
    dlelbo = sla.expm(2*L)@dlelbo
    dlelbo = -sym(dlelbo) + np.eye(len(mu))

    return dlelbo



# --- FUNCTION DEFINITIONS
def GVA(phi, gradphi, hessphi, mu0, L0, eps, maxiter): 
    """
    GVA is the implementation of Gaussian Variational Approximation 
    :param phi: (function handle) st. f(x) = exp(-phi(x))
        phi(x) -log(f(x)f(d|x))
    :param gradphi: (function handle) gradient of f 
    :param hessphi: (function handle) hessian of f 
    :param mu0: initial guess for mean 
    :param L0: initial guess for cov^-1
    :param eps: (scalar) threshold 
    :param maxiter: (scalar) maximum number of iterations for the algorithm 

    :return:
    """

    # initialize parameters
    mu1 = mu0 # current step 
    L1 = L0
    mu2 = mu1 + 1 # previous step 
    L2 = L1 + 1

    k = 0 # iterator
    l = 40 # number of samples 
    d = len(mu0) # dimension
    lam = -0.1

    assert mu0.shape==(d, 1), "mu0 not 2D"
    assert mu2.shape==(d, 1), "mu2 not 2D"

    while((k<maxiter) or ( (npl.norm(mu2 - mu1)/npl.norm(mu2)>eps) and (npl.norm(L2 - L1)/npl.norm(L2)>eps) )):
        k = k + 1

        # generate mu~N(0, 1)
        eta = rdm.normal(size=(d, l))

        # compute ELBO's
        #elbo = ELBO(l, eta, mu1, L1, phi)
        dmuelbo = dmuELBO(l, eta, mu1, L1, gradphi)
        dlelbo = dLELBO(l, eta, mu1, L1, hessphi)

        assert dmuelbo.shape==(d, 1), "dmuelbo shape missmatch"
        assert dlelbo.shape==(d, d), "dlelbo shape missmatch"
        
        # SGD step 
        mu2 = mu1
        mu1 = mu1 - lam*dmuelbo 

        L2 = L1 
        L1 = L1 - lam*dlelbo

        assert mu1.shape==(d, 1), "mu1 shape missmatch"
        assert L1.shape==(d, d), "L1 shape missmatch"

    sig1 = sla.expm(L1)**2
    return mu1, sig1 

"""
from Tools import *

mu = np.ones((3, 1))
sig = 2*np.eye(3)

phi = logNormal(mu, sig)
gradphi = gradLogNormal(mu, sig)
hessphi = hessLogNormal(mu, sig)

mu0 = np.zeros((3, 1))
L0 = np.ones((3, 3))

eps = 0.001
maxiter = 100

mut, sigt = GVA(phi, gradphi, hessphi, mu0, L0, eps, maxiter)

print(mut)
print(npl.inv(sigt))
"""