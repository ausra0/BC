######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
import pandas as pd
from TestTrain import *
from scipy.stats import norm 
import matplotlib.pyplot as plt

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 200 #number of samples 
mu = np.array([-4, 3])
Sig = np.eye(2)
K = npl.inv(Sig)
flag = 0 # 0 = logit, 1 = probit

# --- DEFINE IMPORTANT FUNCTIONS : 

# sampling distributions
def h(theta):
    return np.exp(-0.5*(theta-mu)@K@(theta-mu))

def sampleh(): 
    return np.array([rdm.normal(mu[0], 1), rdm.normal(mu[1], 1)])



# posterior
def post(theta, flag):
    assert len(theta)==len(list(tr))

    prod = 1
    for i in range(0, len(tr)): # 60
        # retrieve data 
        x = np.array(tr.iloc[i])
        y = 0.5*(ytr.iloc[i] + 1)

        # compute proba
        if flag==0: 
            p = 1/(1 + np.exp(-x.dot(theta)))
        elif flag==1: 
            p = norm.cdf(-x.dot(theta))
        else: 
            assert (flag==0 or flag==1)
        
        # compute likelihood
        if flag==0: 
            prod = prod * ((p**y)*((1-p)**(1-y)))*1.24
        else: 
            prod = prod *((p**y)*((1-p)**(1-y)))*1.35

    # add in prior
    return prod * np.exp(-0.5*(theta-mu)@K@(theta-mu))



# disjoint likelihood
def indcond(theta, i, flag):
    # retrieve data
    x = np.array(dft.loc[i, :])

    # compute proba 
    if flag==0: 
        p = 1/(1+np.exp(-x.dot(theta)))
    elif flag==1: 
        p = norm.cdf(-x.dot(theta))
    else:
        assert (flag==0 or flag==1)

    return 2*rdm.binomial(1, p) - 1



def S(theta): 
    return theta

def GenerateSampleData(theta): 
    n = 25
    cal = np.linspace(-2, 5, n)
    fat = np.linspace(-2, 5, n) 

    points = []
    for i in range(0, n): 
        for j in range(0, n): 
#            p = 1/(1 + np.exp(-np.array([cal[i], fat[j]]).dot(theta)))
            p = norm.cdf(-np.array([cal[i], fat[j]]).dot(theta))
            y = 2*rdm.binomial(1, p)-1
            points.append([y, cal[i], fat[j]])
    points = pd.DataFrame(points, columns=['Brand', list(tr)[0], list(tr)[1]])
    return points 

# --- SANITY CHECK 

# export to parameters
param1 = list(tr)[0]
param2 = list(tr)[1]
theta0 = [-1.84749715, 3.11570888]

print('post at theta0 :')
print(post(theta0, flag))

def visual(param1, param2, theta0):
    # generate the data 
    dat = GenerateSampleData(theta0)

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
    plt.savefig("./plots/classif_quality.png")
    plt.show()


# Visualize the data
"""
visual(param1, param2, theta0)
"""

# --- 3D PLOT OF POSTERIOR 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 30
if(flag==0):
    xtheta = np.linspace(-9, -2, N)#-10, 10, N)
    ytheta = np.linspace(2, 5, N)#-10, 10, N)
else: 
    xtheta = np.linspace(1, 4, N)
    ytheta = np.linspace(-5, 0, N)

z_post = np.zeros((N, N))
z_h = np.zeros((N, N))

for i in range(0, N): 
    for j in range(0, N): 
        z_post[i, j] = post([xtheta[i], ytheta[j]], flag)
        z_h[i, j] = h([xtheta[i], ytheta[j]])
xtheta = np.array([xtheta]*N)
ytheta = (np.array([ytheta]*N)).transpose()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(ytheta, xtheta, z_post.transpose(), color="blue")
#ax.plot_wireframe(ytheta, xtheta, z_h.transpose(), color="red")
plt.savefig("./plots/IS_post_plot.png")
plt.show()
