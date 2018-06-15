import numpy as np 
import numpy.random as rdm 
from TestTrain import * 
from Mod21 import * 

def MH(theta0, maxiter, lamb, post, flag): 
    
    k = 0
    steps = np.zeros((maxiter+1, len(theta0)))
    steps[0, :] = theta0
    theta = theta0

    for i in range(0, maxiter): 
        theta_prop = theta + lamb*rdm.multivariate_normal(np.zeros(len(theta0)), np.eye(len(theta0)))
        r = min(post(theta_prop, flag)/post(theta, flag), 1)
        if(rdm.uniform(0, 1)<= r): 
            k += 1 
            theta = theta_prop
            steps[i+1, :] = theta
        else: 
            steps[i+1, :] = theta

    return steps, k/maxiter, np.mean(steps, 0) 

# --- SANITY CHECK 
mu = np.array([-4, 3])
sig = np.eye(2)

def post(theta, flag): 
    assert len(theta)==len(list(tr))

    prod = 1
    for i in range(0, len(tr)):
        # retrive data
        x = np.array(tr.iloc[i])
        y = 0.5*(ytr.iloc[i] + 1)

        # compute proba
        p = 1/(1 + np.exp(-x.dot(theta)))

        # compute likelihood
        prod = prod * ((p**y)*((1-p)**(1-y)))*1.4

    # add in prior
    return prod * np.exp(-0.5*(theta-mu)@K@(theta-mu))


theta0 = np.zeros(2)
maxiter = 200
lamb = 0.5 
flag = 0

steps, acc_ratio, exp = MH(theta0, maxiter, lamb, post, flag)

import matplotlib.pyplot as plt 
plt.plot(steps[:, 0], steps[:, 1])
plt.show()
