def fnct1(alpha, beta):
    def fnct2(gamma):
        return gamma + alpha + beta

    return fnct2


alpha = 0
beta = 1

f = fnct1(alpha, beta) 

gamma = 2

print(f(gamma))

