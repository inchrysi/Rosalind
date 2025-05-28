def readFASTA(txtfile):
    nomieseq = {}
    
    with open(txtfile, 'r') as input:
        for riga in input:
            f = riga.strip()
            
            if riga.startswith('>'):
                chiave = f[1:]
                nomieseq[chiave] = ''
            else:
                nomieseq[chiave]+= f
    
    return nomieseq

def consAndProf(txtfile): #if seqs have same lenght
    collection = readFASTA(txtfile)
    
    seqs = []
    
    for key in collection:
        item = collection.get(key)
        seqs.append(item)
    
    #to determine profile
    l = len(seqs[1])
    
    apparitionA = [0] * l
    apparitionC = [0] * l
    apparitionG = [0] * l
    apparitionT = [0] * l
    
    for x in seqs:
        for i in range(len(x)):
            if x[i] == 'A':
                apparitionA[i]+= 1
            if x[i] == 'C':
                apparitionC[i]+= 1
            if x[i] == 'G':
                apparitionG[i]+= 1
            if x[i] == 'T':
                apparitionT[i]+= 1
    ACGT = [apparitionA, apparitionC, apparitionG, apparitionT]
    
    print('A:', *apparitionA)
    print('C:', *apparitionC)
    print('G:', *apparitionG)
    print('T:', *apparitionT)

    #to determine consensus
    column = list(zip(*ACGT))
    
    consensus = ''
    
    for x in column:
        massimo = 0
        if x[0] > massimo:
            massimo = x[0]
        if x[1] > massimo:
            massimo = x[1]
        if x[2] > massimo:
            massimo = x[2]
        if x[3] > massimo:
            massimo = x[3]
        
        if massimo == x[0]:
            consensus+= 'A'
        elif massimo == x[1]:
            consensus+= 'C'
        elif massimo == x[2]:
            consensus+= 'G'
        elif massimo == x[3]:
            consensus+= 'T'
    
    return consensus
                
"""
    A = 0
    C = 0
    G = 0
    T = 0
    for x in seqs:
        for i in range(len(x)):
            if x[i] == 'A':
=======
    return apparition

            if i == 'A':
>>>>>>> Stashed changes
                A+= 1
            if x[i] == 'C':
                C+= 1
            if x[i] == 'G':
                G+= 1
            if x[i] == 'T':
                T+= 1
<<<<<<< Updated upstream
                
                
    massimo = 0
    
    for x in ACGT:
        for i in range(len(x)):
            if x[i] > massimo:
                massimo = x[i]
                
    for x in column:
        massimo = 0
        if column[0] > massimo:
            massimo = column[0]
        elif column[1] > massimo:
            massimo = column[1]
        elif column[2] > massimo:
            massimo = column[2]
        elif column[3] > massimo:
            massimo = column[3]
"""
