# --- IMPORTS
# ------ EXT. MODULES : 
import numpy as npdfh
# ------ OWN FUNCTIONS : 
from TransformData import * # import data and feature creation
from Prior import defPrior # function handle for f(a)
from CondDist import defCondDist # function hangle for f(d|a)
from Methods1.py import AR # Acceptance-rejection 
from Methods2.py import IS # Importance-sampling

# --- ASSUMPTIONS ON THE MODEL : 
# xi are iid


# --- HANDLE EXTERNAL INPUTS 
# FEATURE TO COME 


# --- MAIN()
# f(a|d) ~ f(d|a)*f(a) 

# parameters of our model (internal to the program)
priorFlag = 77
condFlag = 1
N = 1000 # number of samples 

# redeem conditional distribution function 
fcond = defCondDist(condlfag)
# redeem prior function 
fprior = defPrior(priorFlag)
fsample = sampleFromPrior(priorFlag)

# Sample to approximate posterior
thetah, CI = AR(fprior, fsample, fprior, 1, fcond, N)

# display results 
print("mean : "+str(thetah)+" +/-"+str(CI))
# compute training error and credible interval (should be small)

# Test the model 
