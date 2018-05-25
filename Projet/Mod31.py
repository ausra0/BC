######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
from TestTrain import *

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 300 #number of samples 
mean = np.array([2.5, 0])
K = 1/4*np.eye(2)

# --- TRIM TRAIN AND TEST SET : 
tr = dtrain[["Calories", "TransFat"]]
ts = dtest[["Calories", "TransFat"]]
dft = df[["Calories", "TransFat"]]

# --- DEFINE IMPORTANT FUNCTIONS : 
def prior(theta):
    C = 1/np.sqrt((1/npl.det(2*np.pi*npl.inv(K))))
    return C*np.exp(-0.5*(theta-mean)@K@(theta-mean))

def sampleP():
    return rdm.multivariate_normal(mean,npl.inv(K))

"""
def prior(x): 
    return 1

def sampleP():
    return 5*rdm.random(2)
"""
"""
def post(theta):
    prod = 1
    for i in range(0, len(tr)):
        x = np.array(dft.loc[i, :])
        prod = prod * 1/(1 + np.exp(-x.dot(theta)))
    return prod * np.exp(-0.5*(theta-mean)@K@(theta-mean))
"""
def post(theta):
    return np.exp(-0.5*(theta-mean+1)@K@(theta-mean+1))

def indcond(theta, i):
    x = np.array(dft.loc[i, :])
    return 1/(1+np.exp(-x.dot(theta)))

def S(theta): 
    return theta
