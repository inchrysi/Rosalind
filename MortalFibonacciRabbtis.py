def mortalRabbits(n, k, m):
    fibo = [0, 1, 1]
    monthCounter = 0
    
    for i in range(2, n):
        a = fibo[i]
        b = k * (fibo [i - 1])
        coso = a + b
        monthCounter+= 1
        if monthCounter == m + 1:
            coso = coso - fibo[i - m]
            monthCounter = 0
        fibo.append(coso)
        
    print(fibo, fibo[n])
    
#n -> months
#k  ->litter of pairs
#m -> lifetime
    
#this already considers pairs