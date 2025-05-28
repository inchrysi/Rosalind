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

def overlap(txtfile):
    collection = readFASTA(txtfile)
    seqOverlaps = []
    chiavi = []
    
    for x in collection.keys():
        chiavi.append(x)
    
    #3 parametri: uno che scorra per ogni chiave, uno che prenda l'estremo sx, l'altro che prende estremo dx
    for i in range(len(collection)):
        item1 = collection.get(chiavi[i])
        
        for j in range(len(collection) + 1):
            while j < len(collection):
                item2 = collection.get(chiavi[j])
                
                for k in range(0, int(len(item1))):
                    if item1[0 : k] == item2[0 : k]:
                        seqOverlaps.append(item1[0 : k])
    
    return seqOverlaps

        
'''
for i in range(0, len(item)):
    if item1[0, i] == item2[0,i]
'''
    
    
        
