def rabbitsRecurrence(n, k, m):
    fibo = [0, 1, 1]
    
    for i in range(2, n):
        a = fibo[i]
        b = k * (fibo [i - 1])
        coso = a + b
        fibo.append(coso)
        
    print(fibo, fibo[n])
    
#n -> months
#k  ->litter of pairs
#m -> lifetime