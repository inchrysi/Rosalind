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

def restrictionSite(s):
    collection = readFASTA(s)
    posLen = {}
    
    seq = ''
    
    for key in collection:
        item = collection.get(key)
        seq = item
        
    l = len(seq)
    
    pal = []
    
    for i in range(l - 3):
        j = 4
        antiseq = ''
        p3 = ''
        analyze = seq[i : i + j]
        half = len(analyze) / 2
        if len(analyze) % 2 == 0:
            p1 = seq[i : int(half)]
            p2 = seq[int(half) + 1 : (i + j)] #TGCA 
            antiseq = p2[::-1]
            for x in antiseq:
                if x == 'A':
                    p3+='T'
                elif x == 'T':
                    p3+='A'
                elif x == 'C':
                    p3+='G'
                elif x == 'C':
                    p3+='G'
            if p1 == p3:
                pal.append(analyze)
                   
        else:
            p1 = seq[i : int(half - 1)]
            p2 = seq[int(half+1) : (i + j)]
            antiseq = p2[::-1]
            for x in antiseq:
                if x == 'A':
                    p3+='T'
                elif x == 'T':
                    p3+='A'
                elif x == 'C':
                    p3+='G'
                elif x == 'C':
                    p3+='G'
            if p1 == p3:
                pal.append(analyze)
                    
                
    return pal

def complementary(s1, s2): #stessa lunghezza
    antiseq = ''
    
    for x in s1:
        if x == 'A':
            antiseq+='T'
        elif x == 'T':
            antiseq+='A'
        elif x == 'C':
            antiseq+='G'
        elif x == 'G':
            antiseq+='C'
    
    if antiseq == s2:
        return True
        

def restrictionSite1(s): #doesn't function w/ odds
    collection = readFASTA(s)
    
    seq = ''
    
    for key in collection:
        item = collection.get(key)
        seq = item
        
    l = len(seq)
    pal = []
    pos = []
    antiseq = ''
    
    for x in seq:
        if x == 'A':
            antiseq+='T'
        elif x == 'T':
            antiseq+='A'
        elif x == 'C':
            antiseq+='G'
        elif x == 'G':
            antiseq+='C'
    
    for i in range(l): 
        for j in range(4,13):
            if i + j <= l:
                pospal = antiseq[i : i + j]
                robo = seq[i : i + j]
                if robo == pospal[::-1]:
                    pal.append((i+1, j))
                    
    for x, y in pal:
        print(x, y)
        
    return 

"""
    for i in range(1, l + 1):
        antiseq+= seq[-i]
        
    possible = []
    
    for i in range(l):
        if seq[i] == 'A' and antiseq[i] == 'T' or seq[i] == 'T' and antiseq[i] == 'A':
            possible.append(i)
        if seq[i] == 'C' and antiseq[i] == 'G' or seq[i] == 'G' and antiseq[i] == 'C':
            possible.append(i)
    
    for i in range(l - 3):#with palindromes long 4
        pal4 = 4
        half = (i + 4) / 2
        antiseq = ''
        if half % 2 == 0:
            p1 = seq[i : int(half - 1)]
            p2 = seq[int(half) : (i + 3)]
            for x in range(1, 2):
                antiseq+= p2[-x]
            if p1 == antiseq:
                pal.append(p1 + p2)
                print(p1, p2)
        else:
            p1 = seq[i : int(half - 1)]
            p2 = seq[int(half+1) : (i + 3)]
            for x in range(1, 2):
                antiseq+= p2[-x]
            if p1 == antiseq:
                pal.append(p1 + p2)
                print(p1, p2)
        
"""