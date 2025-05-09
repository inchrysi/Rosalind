#n = 5
#k = 3

#def rabbitsRecurrence(n, k)

#def fibonacci(n):
    #F = int
    
    #coso = F[n - 1] - F[n-2]


def fibonacci(n):
    
    fibo = [0, 1, 1]
    
    for i in range(2, n):
        a = fibo[i]
        b = fibo[i - 1]
        coso = a + b
        fibo.append(coso)

    print(fibo, fibo[n])


def rabbitsRecurrence(n, k):
    fibo = [0, 1, 1]
    
    for i in range(2, n):
        a = fibo[i]
        b = k * (fibo [i - 1])
        coso = a + b
        fibo.append(coso)
        
    print(fibo, fibo[n])
    
    