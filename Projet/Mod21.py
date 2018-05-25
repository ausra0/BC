######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
from TestTrain import *

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 100 #number of samples 
mean = np.array([8, 8])
K = 0.25*np.eye(2)

# --- TRIM TRAIN AND TEST SET : 
tr = dtrain[["Calories", "TransFat"]]
ts = dtest[["Calories", "TransFat"]]
dft = df[["Calories", "TransFat"]]

# --- DEFINE IMPORTANT FUNCTIONS : 
def prior(theta):
    C = 1/np.sqrt((1/npl.det(2*np.pi*npl.inv(K))))
    return np.exp(-0.5*(theta-mean)@K@(theta-mean))
"""
def prior(theta): 
    theta1 = theta[0]
    theta2 = theta[1]
    return np.exp(-0.5*(theta-mean)**2*(K[0, 0]**2))*np.exp(-0.5*(theta-mean)**2*(K[1, 1]**2))
def sampleP():
    return rdm.multivariate_normal(mean,npl.inv(K))
"""
"""
def prior(x): 
    return 1

def sampleP():
    return 5*rdm.random(2)
"""
def post(theta):
    prod = 1
    for i in range(0, len(tr)):
        x = np.array(dft.loc[i, :])
        prod = prod * 1.1 * 1/(1 + np.exp(-x.dot(theta)))
    return prod * np.exp(-0.5*(theta-mean)@K@(theta-mean))

def indcond(theta, i):
    x = np.array(dft.loc[i, :])
    return 1/(1+np.exp(-x.dot(theta)))

def S(theta): 
    return theta

"""
# test posterior 
import numpy.random as rdm 
import matplotlib.pyplot as plt 
n = 100
r1 = []
a1 = np.linspace(0, 16, n)
a2 = np.linspace(0, 16, n)
for i in range(0, n): 
    theta = [a1[i], a2[i]]
    res = prior(theta)
    r1.append(res)

plt.plot(a1, r1)
plt.show()
"""
