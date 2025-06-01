def mendel(k, m, n):
    
    population = k + m + n
    
    posCouple = (population * (population - 1)) / 2
    
    #k = AA
    #m = Aa
    #n = aa
    
    #m + n = 50%
    #m + m = 25%
    #all other possible couples = 100%
    
    #probDom = somma di tutti i possibili figli con almeno allele dominante
    
    km = k*m / posCouple
    mn = m*n / posCouple * 1/2
    kn = k*n / posCouple
    kk = k*(k-1)/2 / posCouple
    mm = m*(m-1)/2 / posCouple * 3/4
    
    probDom = kk + mm + mn + km + kn
    
    return probDom