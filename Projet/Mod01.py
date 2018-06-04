######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
import pandas as pd
from TestTrain import *

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 200 #number of samples 
mean = np.array([-4, 3])
K = np.eye(2)

# --- DEFINE IMPORTANT FUNCTIONS : 

def h(theta):
    return np.exp(-0.5*(theta-mean)@K@(theta-mean))

def sampleh(): 
    return np.array([rdm.normal(mean[0], 1), rdm.normal(mean[1], 1)])

def prior(x): 
    return 1

def sampleP():
    return 10*rdm.random(2)-5

"""
def post(theta):
    prod = 1
    for i in range(0, len(tr)):
        x = np.array(dft.loc[i, :])
        prod = prod * 1/(1 + np.exp(-x.dot(theta)))
    return prod * np.exp(-0.5*(theta-mean)@K@(theta-mean))
"""
def post(theta):
    prod = 1
    for i in range(0, len(tr)): # 60
        x = np.array(tr.iloc[i])
        y = 0.5*(ytr.iloc[i] + 1)
        p = 1/(1 + np.exp(-x.dot(theta)))
        prod = prod * ((p**y)*((1-p)**(1-y)))*1.44
    return prod 

def samplePost(): 
    # sample from posterior to do CMC
    pass 

def indcond(theta, i):
    x = np.array(dft.loc[i, :])
    p = 1/(1+np.exp(-x.dot(theta)))
    return 2*rdm.binomial(1, p) - 1

def S(theta): 
    return theta

def GenerateSampleData(theta): 
    n = 25
    cal = np.linspace(-5, 5, n)
    fat = np.linspace(-5, 5, n) 

    points = []
    for i in range(0, n): 
        for j in range(0, n): 
            p = 1/(1 + np.exp(-np.array([cal[i], fat[j]]).dot(theta)))
            y = 2*rdm.binomial(1, p)-1
            points.append([y, cal[i], fat[j]])
    points = pd.DataFrame(points, columns=['Brand', 'Calories', 'TransFat'])
    return points 

# --- SANITY CHECK 
import matplotlib.pyplot as plt 

def visual(param1, param2, theta0):
    # group the data in the different categories
    groups = dat.groupby('Brand')

    # define companies dictionnary
    dic = {-1 : 'McDo', 1: 'Starbucks'}

    # do the plot
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(getattr(group, param1), getattr(group, param2), marker='o', linestyle='', ms=3, label=dic[name], alpha=0.5)
        ax.legend()

    # group 
    groups2 = df.groupby('Brand')

    # do plot
    for name, group in groups2: 
        ax.plot(getattr(group, param1), getattr(group, param2), marker='.', linestyle='', ms=3, label=dic[name])

    plt.suptitle(param1+' vs '+param2+' ('+str(theta0)+')')
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.show()


# export to parameters
param1 = 'Calories'
param2 = 'TransFat'

theta0 = [-2, 1]
#theta0 = [-5, 3]
# generate data
dat = GenerateSampleData(theta0)
"""
visual(param1, param2, theta0)
"""

# --- 3D PLOT OF POSTERIOR 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 15
xtheta = np.linspace(-10, 0, N)
ytheta = np.linspace(0, 10, N) 

z_post = np.zeros((N, N))
z_h = np.zeros((N, N))

for i in range(0, N): 
    for j in range(0, N): 
        z_post[i, j] = post([xtheta[i], ytheta[j]])
        z_h[i, j] = h([xtheta[i], ytheta[j]])
xtheta = np.array([xtheta]*N)
ytheta = (np.array([ytheta]*N)).transpose()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(xtheta, ytheta, z_post, color="blue")
ax.plot_wireframe(xtheta, ytheta, z_h, color="red")
plt.show()

