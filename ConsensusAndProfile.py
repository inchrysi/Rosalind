def readFASTA(txtfile):
    nomieseq = {}
    
    with open(txtfile, 'r') as input:
        for riga in input:
            f = riga.strip()
            
            if riga.startswith('>'):
                chiave = f[1:]
                nomieseq[chiave] = ''
            else:
                nomieseq[chiave] 