"""
# --- ACCEPTANCE-REJECTION ALGORITHM : 
inc = 0
samples = []
while(inc<n):
    theta = sampleP()
    u = rdm.random()
    if u<=1:
        samples.append(theta*cond(theta))
        inc = inc + 1

samples = np.array(samples)
exp =  sum(samples, 0)/n
IC = 1.96*(sum((samples - exp)**2, 0)/(n-1))/np.sqrt(n)
"""
