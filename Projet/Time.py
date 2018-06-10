import sys, os
import numpy as np 
import pickle 

n = 20
t = np.zeros(n)

for i in range(0, n): 
    # run the file 
    os.system('python '+filename+'.py')

    # get time from dump file 
    with open("./times/M3.dat", "rb") as file:
        t[i] = pickle.load(file)

tim  = mean(t)
print('Benchmark for '+filename)
print(tim)
