def FASTAinStr(coso):
    sequenza = ""
    with coso as f:
        for riga in f:
            if not riga.startswith(">"):
                sequenza += riga.strip()
    return sequenza



def GCcontent(seq):
    G = seq.count('G')
    C = seq.count('C')
    
    GC = G + C
    
    content = 100 * GC /len(seq)
    
    return content

def mostGC(*seq):
    maggiore = ''
    
    for i in range(seq):
        if GCcontent(maggiore) < GCcontent(seq):
            maggiore = seq
    
    return maggiore