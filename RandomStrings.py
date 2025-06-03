import math

def randomStr(seq, array):
    Prob = 1
    B=[]
    A=[]
    PCG = 0
    PAT = 0
    
    for x in array:
        PCG = x / 2
        PAT = (1 - x) / 2
        for y in seq:
            if y == 'A' or y == 'T':
                A.append(PAT)
            else:
                A.append(PCG)
        for z in A:
            Prob = Prob * z
        B.append(math.log10(Prob))
        PAT = 0
        PCG = 0
        Prob = 1
        A = []
        
    return B