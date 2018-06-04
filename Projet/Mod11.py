######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
from TestTrain import *

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 200 #number of samples 
mean = np.array([-5, 3])
Sig = np.eye(2) #+ np.ones((2, 2))
K = npl.inv(Sig)

# assert that variable definition went well 
assert len(mean)==len(list(tr))
assert Sig.shape[0]==len(list(tr))
assert Sig.shape[1]==len(list(tr))



# --- DEFINE IMPORTANT FUNCTIONS : 
"""
# multivariate normal prior
def prior(theta):
    C = 1/np.sqrt((1/npl.det(2*np.pi*npl.inv(K))))
    return C*np.exp(-0.5*(theta-mean)@K@(theta-mean))
"""
def h(theta):
    C = 1/np.sqrt((1/npl.det(2*np.pi*npl.inv(K))))
    return C*np.exp(-0.5*(theta-mean)@K@(theta-mean))

def sampleh(): 
    return np.array([rdm.normal(mean[0], 1), rdm.normal(mean[1], 1)])

def prior(theta): 
    return 1

def sampleP():
    return rdm.multivariate_normal(mean,npl.inv(K))

"""
def prior(x): 
    return 1

def sampleP():
    return 5*rdm.random(2)
"""

# iid logistic conditional 
def post(theta):
    assert len(theta)==len(list(tr))

    prod = 1
    for i in range(0, len(tr)): 
        x = np.array(tr.iloc[i])
        y = 0.5*(ytr.iloc[i] + 1)
        p = 1/(1 + np.exp(-x.dot(theta)))
        prod = prod * ((p**y)*((1-p)**(1-y)))*1.4
    return prod

"""
def post(theta):
    return np.exp(-0.5*(theta-mean)@K@(theta-mean))
"""
# logistic likelihood
def indcond(theta, i):
    x = np.array(dft.loc[i, :])
    return 2*rdm.binomial(1, 1/(1+np.exp(-x.dot(theta)))) - 1

def S(theta): 
    return theta
