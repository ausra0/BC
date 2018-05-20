from S6methods import * 
import numpy as np 
import matplotlib.pyplot as plt 


# define function from which to sample
def f(theta): 
    sigma = np.eye(1) 
    return np.exp(-0.5*(np.dot(theta, sigma@theta)))

# define data 
theta0 = [2.5] # initial step  
maxiter = 10000 # number of maximum iterations
lamb = 8 #  step size
"""
# --- RUN THE NORMAL ALGORITHM --------------------------------------
# run the algorithm 
chain, r0 = MHRW(theta0, maxiter, lamb, f, 1, 1) # run the algorithm 
c0 = np.array(chain) # convert chain to array 

# print statistics of performance of the algorithm 
print("Acceptance rate :")
print(r0)
# should be in the range 10-50%
# -------------------------------------------------------------------
"""

#"""
# --- FIND FOR WHICH STEP SIZE DO WE GET CORRECT ACCEPTION RATE (10-50%)
lamb_list = np.linspace(3, 20, 20) # define step sizes
acc_list = [] # vector for keeping the rates
for i in range(0, len(lamb_list)) : 
    # run M-H
    chain, r = MHRW(theta0, maxiter, lamb, f, 0, 0)
    # keep the rate in memory
    acc_list.append(r)

# display the results
plt.plot(lamb_list, acc_list)
plt.show()
# -------------------------------------------------------------------
#"""

"""
# --- COMPUTING M-H WITH PRE-RUN ------------------------------------
cr, rr = MHRWp(theta0, maxiter, lamb/(2**5), f, 0, 0)
 
print("Burn in period observation :")
theta0 = [100, -100, 50]
maxiter = 10000
lamb = 455
cb, rb = MHRW(theta0, maxiter, lamb, f, 0, 1)
print(rb)

pp = np.zeros((1, len(cb)))
for i in range(0, len(cb)):
    pp[i] = np.log(f(cb[i]))

plt.plot(pp)
plt.show()
# -------------------------------------------------------------------
"""