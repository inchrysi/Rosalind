from itertools import permutations

def permutate(n):
    
    nums = []
    
    for i in range(1, n + 1):
        nums.append(i)
    
    perm = permutations(nums)
    
    a= 0
    for x in perm:
        print(x)
        a+=1
    return a

#Enumerating Oriented Genes
def enumaratingOGO(n):
    
    nums = []
    
    for i in range(1, n + 1):
        nums.append(i)
        nums.append(-i)
    
    perm = permutations(nums, n)
    
    a= 0
    
    with open('OGO.txt' , 'w') as input:
        for x in perm:
            for i in range(len(x) - 1):
                if i < len(x):
                    if abs(x[i]) != abs(x[i + 1]):
                        print(x)
                        a+=1

    return
#Enumetaing k-mers lexicographically
def enumerateKmers(simboli, n):
    
    perm = permutations(simboli, n)
    
    
    for x in perm:
        print(x)
        
    return 
