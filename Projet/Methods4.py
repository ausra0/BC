########################################################
################ LAPLACE APPROXIMATION #################
########################################################
# from S3

# --- IMPORTS 
import numpy as np 
from S3methods import *

# --- ACCESSORY FUNCTIONS OF LAPLACE ------------------
def findmu(post, post1, flagmu): 
    """
    FINDMU accesory function for laplace (finding mu of approximation)
    :param post: (function handle) log posterior 
    :param post1: (function handle) gradient of log posterior
    :param flagmu: (scalar) flag for the method to use : 
                    0: Conjugate Gradient 

    :return: mu (vector of size of theta) approximate mean  
    """
    if flagmu==0:
        steps, func = GD(np.array([0]), f, f1, 1, 0.0001, 100)
    return steps[len(steps)-1] 

def findsig(mu, dist, flagsig):
    """
    FINDSIG accessory function for laplace (finding cov-1 of approx.)
    :param mu: (vector) mean given by Laplace approximation
    :param dist: (function handle) log-hessian or posterior depending on flagsig
    :param flagsig: (scalar) 0 : exact/ 1: approximate

    :return: sig (square matrix of size theta) approximate -log covariance^-1
    """
    if flagsig==0: # exact
        sig = dist(mu)
    if flagsig==1: # approximate
        print("sig approx. not implemented yet")
        return 
    return sig

# --- LAPLACE MAIN FUNCTION ---------------------------
def laplace(post, post1, post2, flagmu, flagsig): 
    """ 
    LAPLACE is the implementation of the laplace method
    ---------------------------------------------------
    /!\ NOTE : should work well for distributions that 
    tend to a normal distribution for n -> inf ie. 
    bernouilli, exponential, laplace, student. 
    ---------------------------------------------------
    :param post: (function handle) log posterior
    :param post1: (function handle) log gradient 
    :param post2: (function handle) -log-hessian-1 (pass 0 if unknown)
    :param flag1: (scalar) which method to use to find mu
    :param flag2: (scalar) which method to use to approximate sig

    :return: mu (vector) Laplace approx. of mean 
             sig (matrix) Laplace approx of stiff. matrix (cov^-1)
    """ 
    
    # search for mu = argmax_{theta}(log(f(theta|d))) 
    # one of the following methods : 
    # 0: GD 
    #   - 
    mu = findmu(post, post1, flagmu)
    
    # find covariance sig = -[log(f(mu|d))]''
    if flagsig==0:
        sig = findsig(mu, post2, 0)
    if flagsig==1:
        sig = findsig(mu, post, 1)

    # return Laplace approximation 
    return mu, sig

#######################################################
# /!\ NOTE :  TO SAMPLE FROM MULT. NORMAL USE : 
# numpy.random.multivariate_normal(mean, cov[, size, check_valid, tol])
# Keep in mind that sig = cov^-1
#######################################################

"""
# --- TOY EXEMPLE -------------------------------------------------
# For this toy exemple we use posterior as being a normal function.
# -----------------------------------------------------------------

# define parameters 
mu = np.array([20])
sig = np.array([5])

# generate post (log normal)
def genNormal(mu, sig): 
    def f(x): 
        return -0.5*np.dot(x-mu, sig@(x-mu))
    return f
f = genNormal(mu, sig)

# generate post1 (log gradient)
def genGrad(mu, sig): 
    def f(x): 
        return -sig@(x-mu)
    return f
f1 = genGrad(mu, sig)

# generate post2 (log hessian)
def genHess(mu, sig): 
    def f(x): 
        return sig # -(-sig)
    return f
f2 = genHess(mu, sig)

# do Laplace Approximation 
# flagmu, flagsig 
# flagmu = 0 CG
# flagsig :0 exact/:1 approx. 

mut, sigt = laplace(f, f1, f2, 0, 0)
print("mu : ")
print(mut)

print("sig : ") 
print(sigt)
"""
