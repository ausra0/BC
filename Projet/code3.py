# coding: utf-8

import numpy as np
from scipy.stats import pareto, norm, multivariate_normal
from TestTrain import * 

mu = np.array([-6, 4])
K = np.eye(2)
# the target pdf
def post(theta):
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

num_samples = 100000

# sample normal values as stepsize for the updates
# important: g is symmetric, so we don't have to use it in the calculation of alpha below
steps = np.random.normal(0, 1, (num_samples, 2))

# with some bookkeeping, I only have to call the pdf of f once per loop iteration
# that is initialized here
x = np.zeros((2,))
x_next = x + np.random.normal(0, 2, 2)  # TODO: you can introduce a different stepsize by scaling these

current_prob = post(x)
next_prob = post(x_next)

x_chosen = np.zeros((num_samples,2))

for i in range(num_samples):

    # to account for cases where the pdf is 0
    # it would be good to avoid them by having a sensible starting point for x
    # they can also occur if the stepsize is so huge that our samples run out of domain
    # so this is a security measure
    if current_prob == 0:
        # we always accept the next sample
        alpha = 1
    elif next_prob == 0:
        # we never accept the next sample accept the next sample
        alpha = 0
    else:
        # this is the normal MH alpha calculation
        alpha = next_prob / current_prob

    if np.random.rand() < alpha:
        x = x_next
        current_prob = next_prob

    x_next = x + steps[i]
    next_prob = post(x_next)

    x_chosen[i] = x

burn_in = 10000
x_final = x_chosen[burn_in:]

print("mean is {}".format(x_final.mean(axis=0)))
print("standard deviation is {}".format(np.cov(x_final.T)))
