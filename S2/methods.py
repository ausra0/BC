#######################################################
############### QUADRATURE FORMULAS ###################
#######################################################
# -- CONTAINS : 
# 
#######################################################
import numpy as np

def quad1d(a, b, n, ft):
    """ 
    QUAD1D computes
    :param a: compute quadrature on [a, b]
    :param b: compute quadrature on {a, b}
    :param n: number of points on grid
    :param ft: unnormalized posterior
    :return: 
    """
    # define integration grid
    grid = np.linspace(a, b, n)
    
    # initialize 
    cst = 0 # constante de normalization 
    mu = 0 # moyenne
    var = 0 # variance 
    quatre = 0 # quatrième moment

    # apply quadrature 
    for i in range(0, n-1): 
        cst = cst + ft(grid[i])*(grid[i+1] - grid[i])
        mu = mu + ft(grid[i])*grid[i]*(grid[i+1] - grid[i])
    mu = mu/cst 
    for i in range(0, n-1):
        var = var + ft(grid[i])*((grid[i]-mu)**2)*(grid[i+1] - grid[i])
    var = var/cst
    for i in range(0, n-1): 
        quatre = quatre + ft(grid[i]*(((grid[i]-mu)/var)**4)*(grid[i+1] - grid[i]))
    return cst, mu, var, quatre/cst



def quad1dv2(a, b, n, ft):
    """ 
    QUAD1DV2 computes
    :param a: compute quadrature on [a, b]
    :param b: compute quadrature on {a, b}
    :param n: number of points on grid
    :param ft: unnormalized posterior
    :return: empirical normalization constant (cst), mean (mu), variance (var), mode (mode) 
    """
    # define integration grid
    grid = np.linspace(a, b, n)
    
    # initialize 
    cst = 0 # constante de normalization 
    mu = 0 # moyenne
    var = 0 # variance 
    mode = 0 # mode

    # apply quadrature 
    for i in range(0, n-1): 
        cst = cst + ft(grid[i])*(grid[i+1] - grid[i])
        mu = mu + ft(grid[i])*grid[i]*(grid[i+1] - grid[i])
        mode = max(mode, grid[i])
    mu = mu/cst 
    for i in range(0, n-1):
        var = var + ft(grid[i])*((grid[i]-mu)**2)*(grid[i+1] - grid[i])
    var = var/cst
    return cst, mu, var, mode
