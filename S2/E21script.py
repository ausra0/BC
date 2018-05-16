########################################################
##################### SESSION 2 ########################
########################################################
# TODO :
# fix mean and kurtosis 
########################################################
# --- IMPORTS 
import numpy as np 
import sys 
from functions import normal1d 
from methods import quad1d

# --- MANAGE SCRIPT INPUT 
n = 100 # default nb. of quad. pts. 
if (len(sys.argv) == 2): 
    params = sys.argv 
    n = int(params[1]) # nb of pts for quadrature

# --- MAIN() 
# define quantities of interest 
mu = 3
sigma = 2
f = normal1d(mu, sigma)

# define quadrature formula base on the fact : 
# mu +/- 3.5*sigma contains 99.9% of the mass
nbstd = 3.5 
    # changing this value to 5 works well because nearly nearly all dist is in mu +/- 5*sigma
a = mu - nbstd*sigma 
b = mu + nbstd*sigma

# run quadrature to find normalization cst 
ncst, nmu, nvar, n4  = quad1d(a, b, n, f)

# compute fourth moment 
fourth = 3*sigma**4 

# print output of function 
print("error on normalization constant : ")
print(abs(ncst - np.sqrt(2*np.pi*(sigma**2)))) 

print("error on mean : ")
print(abs(nmu - mu))

print("error on variance : ")
print(abs(nvar - np.sqrt(sigma)))

print("error on fourth moment : ")
print(abs(n4 - fourth))
