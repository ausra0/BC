import numpy.random as rdm
import numpy as np

def MH1(theta0, maxiter, f):
    """
    M-H Metropolis algorithm
    :param theta0: (col. vector) initial guess 
    :param maxiter: (scalar) max nb. of iterations
    :param f: (function handle) dist. from which we want to know statistics

    :return: theta (list of vectors) from which we can compute statistics
    """
    theta = [theta0] 
    n = theta0.shape[0]
    accept = 0 
    for i in range(0, maxiter): 
        th = theta[len(theta)-1]
        thetap = th + rdm.normal(0, 1, n).reshape(-1, 1)
        p = min(f(thetap)/f(th), 1)
        if rdm.binomial(1, p):
            accept += 1
            theta.append(thetap)
        else: 
            theta.append(th)
    
    print("Acceptance rate :")
    acc = accept/maxiter # should be between 10-50%
    print(acc)
            
    return theta, acc



def MH2(theta0, lamb, maxiter, f):
    """
    M-H Metropolis algorithm
    :param theta0: (col. vector) initial guess 
    :param lamb: (scalar) step length (should be far from 0 and inf)
    :param maxiter: (scalar) max nb. of iterations
    :param f: (function handle) dist. from which we want to know statistics

    :return: theta (list of vectors) from which we can compute statistics
    """
    theta = [theta0] 
    n = theta0.shape[0]
    accept = 0 
    for i in range(0, maxiter): 
        th = theta[len(theta)-1]
        thetap = th + lamb*rdm.normal(0, 1, n).reshape(-1, 1)
        p = min(f(thetap)/f(th), 1)
        if rdm.binomial(1, p):
            accept += 1
            theta.append(thetap)
        else: 
            theta.append(th)
    
    print("Acceptance rate :")
    acc = accept/maxiter # should be between 10-50%
    print(acc)
            
    return theta, acc



def proc(theta, maxiter, theta0):
    """
    processes output of M-H function 
    :param theta: (matrix) (maxiter + 1)xsize(theta0)
    :param maxiter: (scalar) param. from M-H
    :param theta0: (vector) initial guess from M-H

    :return: mean and covariance
    """
    # process list theta 
    theta = np.array(theta)[:, :, 0]

    assert theta.shape==(maxiter + 1, theta0.shape[0]), "Dimension missmatch"

    # compute empirical mean 
    mean = np.mean(theta, 0)
    print("Empirical mean :")
    print(mean)

    # compute empirical covariance 
    cov = 1/(maxiter-1) * np.transpose(theta-mean).dot(theta-mean)
    print("Empirical covariance :")
    print(cov)

    return mean, cov


# CODE FOR LIGHT TESTING PURPOSES : 
# define toy exemple
theta0 = np.zeros((2, 1))
maxiter = 1000
lamb = 2
def f(x): 
    sig = np.eye(2)
    mu = np.zeros((2, 1))
    return np.exp(-0.5*np.transpose(x-mu)@sig@(x-mu))

"""
# call function and process it ---------------------------------------
theta, acc = MH2(theta0, lamb, maxiter , f)
mean, cov = proc(theta, maxiter, theta0)
# --------------------------------------------------------------------
"""
# --- FIND FOR WHICH STEP SIZE DO WE GET CORRECT ACCEPTION RATE (10-50%)
import matplotlib.pyplot as plt 

lamb_list = np.linspace(0.1, 100, 10) # define step sizes
acc_list = np.zeros(len(lamb_list)) # vector for keeping the rates
trials = 10

for j in range(0, trials): 
    for i in range(0, len(lamb_list)) : 
        # run M-H
        chain, r = MH2(theta0, lamb, maxiter, f)
        # keep the rate in memory
        acc_list[i] += r

# display the results
plt.plot(lamb_list, acc_list/trials)
plt.show()
# -------------------------------------------------------------------
