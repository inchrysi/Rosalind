def offspring(a, b, c, d, e, f):
    offsprings = 0
    
    #AA-AA
    AAAA = 2*a
    
    #AA-Aa
    AAAa = 2*b
    
    #AA-aa
    AAaa = 2*c
    
    #Aa-Aa
    AaAa = 2*d * 3/4
    
    #Aa-aa
    Aaaa = 2*e * 1/2
    
    offsprings = AAAA + AAAa + AAaa + AaAa + Aaaa
    
    return offsprings