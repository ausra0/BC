# GS for a high-dimensional Gaussian distribution 
from S5E1methods import * 

d = 5
theta0 = [1]*d
samplopt = 1
maxiter = 10

theta = GS(theta0, samplopt, maxiter)
print(theta)
