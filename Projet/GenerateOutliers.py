import numpy as np 
import pandas as pd 
import numpy.random as rdm 
from TestTrain import * 
import matplotlib.pyplot as plt 
import numpy.linalg as npl

rdm.seed(32)

def Outliers1(theta, xmin, xmax, n, flag):
    data = []
    t1 = theta[0]
    t2 = theta[1]

    for i in range(0,  n): 
        # generate x2
        x2 = rdm.uniform(xmin, xmax)
        # generate x1 
        x1 = -t2/t1 * x2 + rdm.normal(0, 0.1)
        # generate y
        if flag==0:
            y = np.sign(rdm.random() - 0.5)
        elif flag==1: 
            y = 1
        else: 
            y = 0
        data.append([y, x1, x2])
    
    data = pd.DataFrame(data, columns = ['Brand', list(tr)[0], list(tr)[1]])
    return data

def Outliers2(): 
    pass 


def FitLine(indx):
    n = len(tr[ytr==indx])

    # define matrix of system
    A = np.ones((n, 2))
    A[:, 0] = np.array(tr[ytr==indx].loc[:, list(tr)[0]])

    # define RHS
    b = np.array(tr[ytr==indx].loc[:, list(tr)[1]])

    # solve system 
    x = npl.inv(A.transpose()@A)@A.transpose()@b
    
    return x[0], x[1]




def Outliers3(indx, xmin, xmax, n, flag): 
    a, b = FitLine(indx)
    data = []

    for i in range(0,  n): 
        # generate x2
        x1 = rdm.uniform(xmin, xmax)
        # generate x1 
        x2 = a*x1 + b + rdm.normal(0, 0.1)
        # generate y
        if flag==0:
            y = np.sign(rdm.random() - 0.5)
        elif flag==1: 
            y = 1
        else: 
            y = 0
        data.append([y, x1, x2])
      
    data = pd.DataFrame(data, columns = ['Brand', list(tr)[0], list(tr)[1]])
    return data
 


indx = -1
dta = Outliers3(indx, -1, 20, 10, indx)
plt.scatter(dta[list(tr)[0]], dta[list(tr)[1]])
plt.scatter(tr[list(tr)[0]], tr[list(tr)[1]])
plt.show()
