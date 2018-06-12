import sys, os
import numpy as np 
import pickle 

n = 10
t = np.zeros(n)

filename = 'Mod12'

for i in range(0, n): 
    # run the file 
    os.system('python '+filename+'.py')

    # get time from dump file 
    with open("./times/"+filename+".dat", "rb") as file:
        t[i] = pickle.load(file)

tim  = np.mean(t)
print('Benchmark for '+filename)
print(tim)
