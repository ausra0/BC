from S7methods import GVA
from Tools import *
import numpy as np 

mu = np.zeros((3, 1))
sig = np.eye(3)

phi = logNormal(mu, sig)
gradphi = gradLogNormal(mu, sig)
hessphi = hessLogNormal(mu, sig)

mu0 = np.ones((3, 1))
L0 = np.ones((3, 3))

eps = 0.01
maxiter = 100

mut, sigt = GVA(phi, gradphi, hessphi, mu0, L0, eps, maxiter)
