######################################################
###### SAMPLING METHODS III
######################################################
# --- CONTAINS : 
# MHRW			Metropolis-Hastings 
# MHRW			Metropolis-Hastings with burn-in
#####################################################
import numpy as np 
import numpy.random as rdm
 
def MHRW(theta0, maxiter, lamb, f, rando, display): 
    """
    MHRW is the implementation of the Metropolis-Hastings sampling with random walk
    :param theta0: (scalar) initial step 
    :param maxiter: (scalar) maximum number of iterations 
    :param lamb: (scalar) one step size parameter
    :param f: (function handle) our distribution 
    :param rando: (0, 1) 0-unif error, 1-normal error
    :param display: (bool) if to display covariance and mean

    :return:
    """
    theta = theta0 
    chain = []
    chain.append(theta0)
    n = len(theta0)
    acc_ratio = 0

    for i in range(0, maxiter): 
        # generate new step
        if(rando==0): 
            theta_prop = theta + lamb*rdm.uniform(-1, 1, n)
        elif(rando==1): 
            theta_prop = theta + lamb*rdm.normal(0, 1, n)
        else: 
            print("error")
            return

        # compute acceptance probability 
        p = min(1, f(theta_prop)/f(chain[len(chain)-1]))

        # accept-reject step 
        if(rdm.binomial(1, p)): 
            acc_ratio += 1
            chain.append(theta_prop)
        else: 
            chain_prev = chain[len(chain)-1]
            chain.append(chain_prev)
    
    if(display):
        # compute empirical mean 
        mean = np.mean(np.array(chain), 0)
        print("Empirical mean :")
        print(mean)

        # compute empirical covariance 
        cov = 1/(maxiter-1) * np.transpose(chain-mean)@(chain-mean)
        print("Empirical covariance :")
        print(cov)

    # return 
    return chain, acc_ratio/maxiter

def MHRWp(theta0, maxiter, lamb0, f, rando, display):
    """
    MHRWp is the implementation of the Metropolis-Hastings sampling with random walk
    :param theta0: (scalar) initial step 
    :param maxiter: (scalar) maximum number of iterations 
    :param lamb0: (scalar) one step size parameter
    :param f: (function handle) our distribution 
    :param rando: (0, 1) 0-unif error, 1-normal error

    :return:
    """

    lamb = lamb0
    # prerun
    r = 0
    while((r<0.1) or (r>0.5)):
        print("running prerun ...")
        c, r = MHRW(theta0, 100, lamb, f, rando, 0)
        lamb = 2*lamb
    
    # continue running
    ch, rh = MHRW(c[len(c)-1], maxiter -100, lamb/2, f, rando, display)
    
    # return 
    return c + ch, rh
