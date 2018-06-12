######## Methods for Model 1
# --- IMPORTS : (X)
import numpy as np 
import numpy.linalg as npl
from TestTrain import *
from scipy.stats import norm
import matplotlib.pyplot as plt



# --- DEFINE VARIABLES FOR THE PROGRAM : 
n = 200 #number of samples 
lentr = len(list(tr)) # number of observations in train set

# Define mu matrix
if lentr==2: 
    mu = np.array([-6, 4])
elif lentr==3:
    mu = np.array([0, -5, 3])
else: 
    assert (lentr==3 or lentr==2)

# Define covariance matrix
if lentr==2: 
    Sig = np.eye(2) #+ np.ones((2, 2))
else: 
    # we have already asserted that len(list(tr))== 2 or 3
    Sig = np.eye(3)

# Define stiffness matrix
K = npl.inv(Sig)

# Add flag for choice of posterior 
flag = 0 # 0 = logit, 1 = probit 

# assert that variable definition went well 
assert len(mu)==lentr
assert Sig.shape[0]==lentr
assert Sig.shape[1]==lentr




# --- DEFINE IMPORTANT FUNCTIONS : 

# sampling distributions
def h(theta):
    C = 1/np.sqrt((1/npl.det(2*np.pi*npl.inv(K))))
    return C*np.exp(-0.5*(theta-mu)@K@(theta-mu))

def sampleh(): 
    if lentr==2: 
        return np.array([rdm.normal(mu[0], 1), rdm.normal(mu[1], 1)])
    elif lentr==3: 
        return np.array([rdm.normal(mu[0], 1), rdm.normal(mu[1], 1), rdm.normal(mu[2], 1)])
    else: 
        assert (lentr==3 or lentr==2)



# posterior
def post(theta, flag):
    assert len(theta)==len(list(tr))

    prod = 1
    for i in range(0, len(tr)): 
        # retrive data 
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
        prod = prod * ((p**y)*((1-p)**(1-y)))*1.24

    # add in prior
    return prod * np.exp(-0.5*(theta-mu)@K@(theta-mu))




# logistic likelihood
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




# --- DEFINE PLOTTING FUNCTIONS 
def GenerateSampleData(theta, flag):
    # used by visual
    n = 25
    cal = np.linspace(min(dft[list(tr)[0]]), max(dft[list(tr) [0]]), n)
    fat = np.linspace(min(dft[list(tr)[1]]), max(dft[list(tr)[1]]), n)

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
    points = pd.DataFrame(points, columns=['Brand', list(tr)[0], list(tr)[1]])
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
    plt.savefig("plots/error_mod11.png")
    plt.show()



