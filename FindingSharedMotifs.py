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

def commonSub(s1, s2):
    
    common = ''
    commonsubs = []
    
    l = 0
    
    if len(s1) < len(s2):
        l = len(s1)
    else:
        l = len(s2)
    
    for i in range(l):
        if s1[i] == s2[i]:
            common+= s1[i]
            commonsubs.append(common)
        else:
            common = ''
    
    maxlen = 0
    for x in commonsubs:
        if len(x) > maxlen:
            maxlen = len(x)
    
    longestsubs = []
    
    for x in commonsubs:
        if len(x) >= maxlen:
            longestsubs.append(x)
    
    return commonsubs

def LCS(txtfile):
    
    nomieseq = readFASTA(txtfile)
    seqs = []
    
    for x in nomieseq:
        item = nomieseq.get(x)
        seqs.append(item)
    
    seq1 = seqs[0]
    commonsubs = set()
    maxlen = 0

    for i in range(len(seq1)):
        for j in range(i + 1, len(seq) + 1):
            substr = base_seq[i:j]
            if all(substr in seq for seq in seqs[1:]):
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    commonsubs = {substr}
                elif len(substr) == maxlen:
                    commonsubs.add(substr)

    return list(commonsubs)

            
            
                
        
"""
    for i in range(len(seqs)):
        for x in seqs[i]:
"""
#BLOCCO PER DEFINIRE LCS DI DUE STRINGHE AHAHAH ps funzionante================
def commonSub1(s1, s2):
    
    common = ''
    commonsubs = []
    
    
    if len(s1) == len(s2):
        common = ''
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                common+= s1[i]
                commonsubs.append(common)
            else:
                common = ''

    else:
        l = 0
        if len(s1) < len(s2):
            l = len(s1)
            diff = len(s2) - l
            for i in range(l):
                if s1[i] == s2[i]:
                    common+= s1[i]
                    commonsubs.append(common)
                else:
                    common = ''
            for i in range(l, l + diff):
                if s2[i] in s1:
                    common+= s2[i]
                    commonsubs.append(common)
                else:
                    common = ''
        
        else:
            l = len(s2)
            diff = len(s1) - l
        
            for i in range(l):
                if s1[i] == s2[i]:
                    common+= s1[i]
                    commonsubs.append(common)
                else:
                    common = ''
            for i in range(l, l + diff):
                if s1[i] in s2:
                    common+= s1[i]
                    commonsubs.append(common)
                else:
                    common = ''
            
    maxlen = 0
    for x in commonsubs:
        if len(x) > maxlen:
            maxlen = len(x)
    
    longestsubs = []
    
    for x in commonsubs:
        if len(x) >= maxlen:
            longestsubs.append(x)
        
    return commonsubs
        
            