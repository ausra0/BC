#################################################
####### OPTIMIZATION TECHNIQUES FOR STATS #######
#################################################
# from S3
# ---  CONTAINS : 
# GD            Gradient Descent
# LSGD          Line-Search Gradient Descent
# NR            Newton-Raphson Method 
# SGD           Stochastic Gradient Descent 
#
# --- PROTOTYPES : 
# def GD(theta0, energy, grad, lamb, epsi, maxiter): 
#     return steps, func
# def LSGD(theta0, energy, grad, lamb, beta, alpha1, alpha2, epsi, maxiter): 
#     return steps, func
# def NRM(theta0, energy, grad, hessian, beta, alpha1, alpha2,  epsi, maxiter): 
#     return steps, func
# def SGD(theta0, energy, grad, lamb, beta, alpha1, alpha2,  epsi, maxiter): 
#     return steps, func
#################################################
import numpy as np

def GD(theta0, energy, grad, lamb, epsi, maxiter): 
    """
    Gradient Descent implementations 
    :param theta0: (vector) beggining point for our search 
    :param energy: (function handle) function we want to maximize
    :param grad: (function handle) it's gradient 
    :param lamb: (scalar) 
    :param epsi: (scalar) precision wanted 
    :param maxiter: (scalar) number of maximum iterations that CG can perform
    :return: func (vector) list of the energies at each step, 
             steps (vector) list of the thetas at each step 
    """
    print('running GD')

    func = [energy(theta0)]
    steps = [theta0]
    k = 0
    err = epsi + 1
    theta = theta0 

    while ((err>epsi) and (k<maxiter)):
        k = k + 1
        theta = theta - lamb*grad(theta)

        steps.append(theta)
        func.append(energy(theta))
        
        err = np.linalg.norm(grad(theta))
        
    # print some stats 
    print('Number of steps : ' + str(len(steps)-1))
    print('Number of iterations actually performed : ' + str(k))

    return steps, func 


def LSGD(theta0, energy, grad, lamb, beta, alpha1, alpha2, epsi, maxiter): 
    # Line-search Gradient Descent implementation 
    # --- OUT : 
    # func      list of the energies at each step 
    # steps     list of the thetas at each step 
    # -------------------------------------------
    print('Running LSGD')

    func = [energy(theta0)]
    steps = [theta0]
    k = 0
    err = epsi + 1
    theta = theta0 

    while ((err>epsi) and (k<maxiter)):
        k = k + 1
        # compute next step 
        theta_cand = theta - lamb*grad(theta)
        
        C1 = energy(theta_cand) <= energy(theta) - alpha1*lamb*(np.linalg.norm(theta)**2)
        C2 = -np.dot(grad(theta), grad(theta_cand)) <= -alpha2*(np.linalg.norm(theta)**2)
        # compute Wolfes conditions 
        if(C1 and C2): # if accepted
            theta = theta_cand
            steps.append(theta)
            func.append(energy(theta))
        else: # if rejected, reduce step
            lamb = beta*lamb
    
        err = np.linalg.norm(grad(theta))

    # print some stats 
    print('Number of steps : ' + str(len(steps)-1))
    print('Number of iterations actually performed : ' + str(k))

    return steps, func


def NRM(theta0, energy, grad, hess, beta, alpha1, alpha2,  epsi, maxiter): 
    # Newton-Raphson method implementation 
    # --- OUT : 
    # func      list of the energies at each step 
    # steps     list of the thetas at each step 
    # -------------------------------------------
    print('running N-R')

    func = [energy(theta0)]
    steps = [theta0]
    k = 0
    lamb = 1
    err = epsi + 1
    theta = theta0 

    while ((err>epsi) and (k<maxiter)):
        k = k + 1
        # precompute 
        H = np.linalg.inv(hess(theta))

        # compute next step 
        theta_cand = theta - lamb*H@grad(theta)
        
        # compute Wolfes conditions 
        C1 = energy(theta_cand) <= energy(theta) - alpha1*lamb*(np.dot(H@grad(theta),grad(theta)))
        C2 = -np.dot(H@grad(theta), grad(theta_cand)) <= -alpha2*(np.dot(H@grad(theta), grad(theta)))
        if(C1 or C2): # if accepted
            theta = theta_cand
            steps.append(theta)
            func.append(energy(theta))
        else: # if rejected, reduce step
            lamb = beta*lamb
    
        err = np.linalg.norm(grad(theta))

    # print some stats 
    print('Number of steps : ' + str(len(steps)-1))
    print('Number of iterations actually performed : ' + str(k))

    return steps, func


def SGD(theta0, energy, grad, lamb, beta, alpha1, alpha2,  epsi, maxiter): 
    # Stochastic Gradient Descent implementation
    # --- IN : 
    # lamb      function handle that discribes lamb as a function of k
    # grad      function handle with gradient decomposition
    # --- OUT : 
    # func      list of the energies at each step 
    # steps     list of the thetas at each step 
    # -------------------------------------------
    print('running SGD')

    func = [energy(theta0)]
    steps = [theta0]
    k = 0
    err = epsi + 1
    theta = theta0 

    while ((err>epsi) and (k<maxiter)):
        k = k + 1
        # compute next step 
        theta_cand = theta - lamb*grad(theta)
        
        # compute Wolfes conditions 
        C1 = energy(theta_cand) <= energy(theta) - alpha1*lamb*(np.linalg.norm(theta)**2)
        C2 = -np.dot(grad(theta), grad(theta_cand)) <= -alpha2*(np.linalg.norm(theta)**2)
        if(C1 and C2): # if accepted
            theta = theta_cand
            steps.append(theta)
            func.append(energy(theta))
        else: # if rejected, reduce step
            lamb = beta*lamb
    
        err = np.linalg.norm(grad(theta))

    # print some stats 
    print('Number of steps : ' + str(len(steps)-1))
    print('Number of iterations actually performed : ' + str(k))

    return steps, func
