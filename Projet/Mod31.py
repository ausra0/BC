######## Methods for Model 3
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
import numpy.random as rdm 
import matplotlib.pyplot as plt
from TestTrain import *

# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 300 #number of samples 
mu = np.array([-4, 3])
Sig = np.eye(2)
K = npl.inv(Sig)
flag = 0

# --- DEFINE IMPORTANT FUNCTIONS : 

def logpost(theta):

    # prior
#    Z = np.sqrt(npl.det(2*np.pi*Sig))
#    post = -np.log(Z) - 0.5*(theta-mu)@K@(theta-mu)
    post = 0

    #likelihood
    for i in tr.index.values:
        # retrieve info 
        yi = 0.5*(ytr.loc[i] + 1)
        xi = np.array(tr.loc[i])
        # compute posterior
        post -= yi*np.log(1 + np.exp(-theta.dot(xi))) 
        post -= (1-yi)*np.log(1 + np.exp(theta.dot(xi)))

    return post



def gradlogpost(theta): 

    # prior
#    post = -K@(theta-mu)
    post = np.zeros(len(theta))

    #likelihood 
    for i in tr.index.values: 
        # retrive info 
        yi = 0.5*(ytr.loc[i]+1)
        xi = np.array(tr.loc[i])
        # compute grad post
        post += yi*xi/(1 + np.exp(theta.dot(xi)))
        post += (yi -1)*xi/(1 + np.exp(-theta.dot(xi)))

    return post 



def hesslogpost(theta): 

    # prior 
#    post = -K
    post = np.zeros((len(theta), len(theta)))

    # likelihood 
    for i in tr.index.values:
        # retieve info 
        yi = 0.5*(ytr.loc[i] + 1)
        xi = np.array(tr.loc[i])
        # compute hess post
        prod = theta.dot(xi)
        xx = np.outer(xi, xi)
        denom = (1 + np.exp(-prod))*(1 + np.exp(prod))
        post -= xx/denom 

    return post



def indcond(theta, i, flag):
    x = np.array(dft.loc[i, :])

    # compute proba
    if flag==0:
        p = 1/(1+np.exp(-x.dot(theta)))
    elif flag==1:
        p = norm.cdf(-x.dot(theta))
    else:
        assert (flag==0 or flag==1)

    return 2*rdm.binomial(1, p) - 1 

    p = 1/(1+np.exp(-x.dot(theta)))
    return rdm.binomial(1, p)



# --- DEFINE PLOTTING FUNCTIONS
def GenerateSampleData(theta, flag):
    # used by visual
    n = 25
    cal = np.linspace(min(dft[list(dft)[0]]), max(dft[list(dft)[0]]), n)
    fat = np.linspace(min(dft[list(dft)[1]]), max(dft[list(dft)[1]]), n)

    points = []
    for i in range(0, n):
        for j in range(0, n):
            # compute proba
            if flag==0:
                p = 1/(1 + np.exp(-np.array([cal[i], fat[j]]).dot(theta)))
            elif flag==1:
                p = norm.cdf(-np.array([cal[i], fat[j]]).dot(theta))
            else:
                assert (flag==0 or flag==1)

            # compute brand
            y = 2*rdm.binomial(1, p)-1

            # store data
            points.append([y, cal[i], fat[j]])

    # convert to dataframe
    points = pd.DataFrame(points, columns=['Brand', list(dft)[0], list(dft)[1]])
    return points



def visual(param1, param2, theta0):
    # group the data in the different categories
    dat=GenerateSampleData(theta0, flag)
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
    plt.savefig("plots/error_mod31.png")
    plt.show()


"""
# Simple testing 
theta = np.ones(2)
t1 = logpost(theta) 
t2 = hesslogpost(theta) 
t3 = gradlogpost(theta)

print(t1) 
print(t2) 
print(t3)
"""
