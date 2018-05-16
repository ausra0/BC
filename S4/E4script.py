##################################################
############ MAIN SCRIPT OF SERIES 3 #############
##################################################

############### METHOD IMPORTATION ###############
# std stuff
import numpy as np
import matplotlib.pyplot as plt

from E4methods import * # sampling methods
    # PROTOTYPES : 

from E4functions import * # function definitions 
    # PROTOTYPES : 

##################### TO DO ######################

##################### MAIN #######################
print("1 : Sample from normal with normal")
print("2 : ")
print("3 : ")

choice = int(input("please choose a nb : "))

if choice == 1:
    muT = 0
    sigmaT = 1
    muP = 0
    sigmaP = 1
 
    n = 100

    f = generateGaussianHandle(muT, sigmaT)
    h = generateGaussianHandle(muP, sigmaP)
    sampleh = generateGaussianSamplingHandle(muP, sigmaP)

    x = np.linspace(-10, 10, 50)
    K = 1; 
    plt.plot(x, f(x), label ="target")
    plt.plot(x, K*h(x), label ="proposal")
    plt.show()

    def S(x): 
        return x

    yIS, varIS = IS(h, sampleh, f, S, n)
    yAR, varAR = AR(h, sampleh, f, K, S, n)

    print("Importance Sampling : " + str(yIS) + "     std : " + str(np.sqrt(varIS)))
    print("Acceptance-Rejection : " + str(yAR) + "     std : " + str(np.sqrt(varAR)))

    #plt.legend()
    #plt.show()

if choice == 2: 
    ### analysis of choice of lamba 
    sigma = np.array([[2, 0], [0, 1]])
    nrj1, grad1, hess1 = quadFunc(sigma)

    theta = [1, 1]
    n = 10
    lamb = np.linspace(0.1,0.6, n)
    epsi = 0.001
    maxiter = 1000
    beta = 0.5 
    alpha1 = 0.0001
    alpha2 = 0.9 

    itercount = np.zeros((4, n))

    for i in range(0, n):  
        # CG : 
        stepGD, funcGD = GD(theta, nrj1, grad1, lamb[i], epsi, maxiter) 

        # Line Search GD : 
        stepLSGD, funcLSGD = LSGD(theta, nrj1, grad1, lamb[i], beta, alpha1, alpha2, epsi, maxiter)

        # Newton-Raphson :
        stepNR, funcNR = NRM(theta, nrj1, grad1, hess1, beta, alpha1, alpha2, epsi, maxiter)

        # Stochastic GD :
        stepSGD, funcSGD = SGD(theta, nrj1, grad1, lamb[i], beta, alpha1, alpha2, epsi, maxiter)
        
        itercount[0, i] = len(stepGD)
        itercount[1, i] = len(stepLSGD)
        itercount[2, i] = len(stepNR) 
        itercount[3, i] = len(stepSGD)

    
    plt.plot(lamb, itercount[0, :], label = "CG")
    plt.plot(lamb, itercount[1, :], label = "LSCG") 
    plt.plot(lamb, itercount[2, :], label = "NR") 
    plt.plot(lamb, itercount[3, :], label = "SGD")
        
    plt.legend()
    plt.show()

if choice == 3:
    print('hello')
