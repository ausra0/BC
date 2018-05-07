# --- IMPORTS
# ------ EXT. MODULES : 
import numpy as np # check if necessary
# ------ OWN FUNCTIONS : 
from TransformData import * # import data and feature creation
from Prior import defPrior # function handle for f(a)
from CondDist import defCondDist # function hangle for f(d|a)

# --- ASSUMPTIONS ON THE MODEL : 
# xi are iid


# --- HANDLE EXTERNAL INPUTS 



# --- MAIN()
# f(a|d) ~ f(d|a)*f(a) 

# parameters of our model (internal to the program)
priorFlag = 1
condFlag = 1

# redeem conditional distribution function 
fcond = defCondDist(condlfag)

# redeem prior function 
fprior = defPrior(priorFlag)

# Sample to approximate posterior

# compute training error and credible interval (should be small)

# Test the model 
    # compute p(a|d) 
    # test if p(a|d)>0.5 corresponds to 1 (can we change 0.5 and in which case should we change it?)
