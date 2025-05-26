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

def consAndProf(txtfile):
    collection = readFASTA(txtfile)
    
    seqs = []
    
    
    for key in collection:
        item = collection.get(key)
        seqs.append(item)
    
    apparition = []
    
    for x in seqs:
        A = []
        C = []
        G = []
        T = []
        
        for i in x:
            if i == 'A':
                A.append(1)
            if i == 'C':
                C.append(1)
            if i == 'G':
                G.append(1)
            if i == 'T':
                T.append(1)
        apparition.append(A)
        apparition.append(C)
        apparition.append(G)
        apparition.append(T)
            
    return apparition
'''
            if i == 'A':
                A+= 1
            if i == 'C':
                C+= 1
            if i == 'G':
                G+= 1
            if i == 'T':
                T+= 1
'''