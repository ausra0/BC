import math 

N = 10
n = 4

def contfunct(li): 
    n = len(li)
    frac = li[n-1]
    for i in range(n-2, -1, -1): 
        frac = li[i] + 1/frac
    return frac

def finda(N, n):
    # N the number from which we want to approx sqrt(N) 
    # n number of ai to find (precision of approximation) 

    # define useful stuff and prepare interation
    m = 0
    d = 1
    a = []
    approx = []
    
    # keep in memeory a0 and assoc. cont. funct. 
    a.append(math.floor(math.sqrt(N)))
    approx.append(contfunct(a))

    # iteration 
    for i in range(0, n): 
        m = d*a[len(a)-1] - m
        d = (N-m**2)/d
        a.append(math.floor((a[0] + m)/d))
        approx.append(contfunct(a))

        print('a', a[i])
        print('m', m) 
        print('d', d)
    return a, approx

a, approx = finda(N, n); 


