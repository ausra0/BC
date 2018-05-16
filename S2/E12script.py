########################################################
##################### SESSION 2 ########################
########################################################
# TODO :
########################################################
# --- IMPORTS 
import numpy as np 
import scipy.special as ss
import sys 
from functions import gamma1d 
from methods import quad1dv2

# --- MANAGE SCRIPT INPUT 
n = 100 # default nb. of quad. pts. 
if (len(sys.argv) == 2): 
    params = sys.argv 
    n = int(params[1]) # nb of pts for quadrature

# --- MAIN() 
# define quantities of interest 
#alpha >=1
alpha = 1
beta = 1
f = gamma1d(alpha, beta)

# compute values of interest 
cst = ss.gamma(alpha)/(beta**alpha)
mu = alpha/beta
var = alpha/(beta**2) 
mode = (alpha -1)/beta 

# define quadrature formula base on the fact : 
# XX contains 99.9% of the mass
nbstd = 3.5 
a = mu - nbstd*var**2 
b = mu + nbstd*var**2


# run quadrature to find empirical values
ncst, nmu, nvar, nmode  = quad1dv2(a, b, n, f)


# print output of function 
print("error on normalization constant : ")
print(abs(ncst - cst)) 

print("error on mean : ")
print(abs(nmu - mu))

print("error on variance : ")
print(abs(nvar - var))

print("error on mode : ")
print(abs(nmode - mode))
