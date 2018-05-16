import numpy as np 
import numpy.random as nprdm
import math as m
import matplotlib.pyplot as plt 


def GenerateData !!! why does he add sum(X) to the alpha_h (alpha_star) ? 
#normal variance : ok
set(n, theta0):
    # n scalar number of points 
    # theta0 scalar in [0, 1]

    return nprdm.binomial(1, theta0, n)


def ComputePosterior(dataset, alpha, beta):
    # --- INPUT 
    # dataset vector our dataset
    # alpha scalar param. of dist. 
    # beta scalar param. of dist. 
    # --- OUTPUT 
    # post function for unnormalized posterior
    # C scalar value of normalization constant
    # a, b bounds of the 0.95 credible interval 
    
    alpha_h = alpha + sum(dataset)
    beta_h = beta + sum(1-dataset)

    # normalization constant 
    C = (m.gamma(alpha + beta)*m.gamma(alpha_h)*m.gamma(beta_h))/(m.gamma(alpha)*m.gamma(beta)*m.gamma(alpha_h + beta_h))

    # posterior function 
    def post(theta):
        Cn = m.gamma(alpha + beta)/(m.gamma(alpha)*m.gamma(beta))
        return (1-theta)**(beta_h -1)*theta**(alpha_h -1)*Cn

    # compute bounds of the 0.95 credible 
    e = 1.96*(alpha_h*beta_h/((alpha_h + beta_h)**2*(1+alpha_h + beta_h)))**2
    a = alpha_h/(alpha_h + beta_h) - e
    b = a + 2*e

    return(post, C, a, b)

#normal mean formula !!! why does he add sum(X) to the alpha_h (alpha_star) ? 
#normal variance : ok

def plotPosth(post):
    n = 30

    ft = np.zeros(n+1) 
    for i in range(0, n+1):
        ft[i] = post(i/n)

    plt.plot(ft)
    plt.show()
    
    return 0 


def plotPost(post, C, a, b, lab): 
    n = 30
    ft = np.zeros(n+1)
    for i in range(0, n+1): 
        ft[i] = post(i/(n+1))/C

    m = np.max(ft)

    plt.figure(1)
    plt.plot(np.linspace(0, 1, n+1), ft, label = lab)
    plotCI(a, b, m)
    #plt.show()

    return 0


def plotCI(a, b, m):
    n = 20
    
    #CI = (b-a)*np.array(range(0, n+1))/n + a
    li = np.ones(n+1)
    lo = m*np.array(range(0, n+1))/n

    plt.plot(a*li, lo, 'r')
    plt.plot(b*li, lo, 'r')

    return 0

def computeMeans(alpha, beta, dataset):
    alpha_h = alpha + sum(dataset)
    beta_h = beta + sum(1-dataset)
    
    n = len(dataset)
    
    freqMean = sum(dataset)/n 
    postMean = alpha_h/(alpha_h + beta_h)
    
    print('freq. mean :', freqMean)
    print('post. mean :', postMean)
    
    sig = np.sqrt(sum((dataset - freqMean)**2)/(n+1))
    
    aa = freqMean - 1.96*sig/np.sqrt(n)
    bb = aa + 2*1.96*sig/np.sqrt(n)
    
    return aa, bb

#----------------------------------------------------

np.random.seed(1000)

theta0 = 0.5
n = 30

dataset = GenerateDataset(n, theta0)

alpha = 1
beta = 2

post, C, a, b = ComputePosterior(dataset, alpha, beta)

#plotPosth(post)
plotPost(post, C, a, b, '')
plt.show()

# ---------------------------------------------

dataset1 = GenerateDataset(n, theta0)
dataset2 = GenerateDataset(n, theta0)
dataset3 = GenerateDataset(n, theta0)

alpha = 1
beta = 2

post1, C1, a1, b1 = ComputePosterior(dataset1, alpha, beta)
post2, C2, a2, b2 = ComputePosterior(dataset2, alpha, beta)
post3, C3, a3, b3 = ComputePosterior(dataset3, alpha, beta)

plotPost(post1, C1, a1, b1, 'd1')
plotPost(post2, C2, a2, b2, 'd2')
plotPost(post3, C3, a3, b3, 'd3')
plt.legend()
plt.show()

# --------------------------------------------

dataset1 = GenerateDataset(2, theta0)
dataset2 = GenerateDataset(10, theta0)
dataset3 = GenerateDataset(100, theta0)

alpha = 1
beta = 2

post1, C1, a1, b1 = ComputePosterior(dataset1, alpha, beta)
post2, C2, a2, b2 = ComputePosterior(dataset2, alpha, beta)
post3, C3, a3, b3 = ComputePosterior(dataset3, alpha, beta)

plotPost(post1, C1, a1, b1, 'd1')
plotPost(post2, C2, a2, b2, 'd2')
plotPost(post3, C3, a3, b3, 'd3')
plt.legend()
plt.show()

print('\nNORMALITATION CONSTANTS :')
print('c1 : ', C1)
print('c2 : ', C2) 
print('c3 : ', C3)

print('\nSIZE OF CREDIBLE INTERVAL :')
print('CI 1 : ', b1 - a1)
print('CI 2 : ', b2 - a2)
print('CI 3 : ', b3 - a3)

print('\nPOSTERIOR MEAN VS FREQUENTIST MEAN :')
print('dataset1 :')
aa1, bb1 = computeMeans(alpha, beta, dataset1)
print('dataset2 :')
aa2, bb2 = computeMeans(alpha, beta, dataset2)
print('dataset3 :')
aa3, bb3 = computeMeans(alpha, beta, dataset3)

print('\nSIZE OF CREDIBLE INTERVAL VS CONF INT :')
print('Cred. Int. d1 : ', a1, '\t\t', b1)
print('Conf. Int. d1 : ', aa1, '\t\t\t', bb1) 
print('Cred. Int. d2 : ', a2, '\t', b2)
print('Conf. Int. d2 : ', aa2, '\t', bb2) 
print('Cred. Int. d3 : ', a3, '\t', b3)
print('Conf. Int. d3 : ', aa3, '\t', bb3) 
