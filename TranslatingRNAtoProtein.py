
def translate(s): #w/o dict
    triplets = []
    x = 0
    myProtein = ''
    
    proteins = {('UUU', 'UUC') : 'F', ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG') : 'L', ('UCU', 'UCC', 'UCA', 'UCG') : 'S', ('UAU', 'UAC') : 'Y', ('UGU', 'UGC') : 'C', 'UGG' : 'G', ('CCU', 'CCC', 'CCG') : 'P', ('CAU', 'CAC') : 'H', ('CAA', 'CAG') : 'G', ('CGU', 'CGC', 'CGA', 'CGG') : 'R', ('AUU', 'AUC', 'AUA') : 'I', 'AUG' : 'M', ('ACU', 'ACC', 'ACA') : 'T', ('AAU', 'AAC') : 'N', ('AAA', 'AAG') : 'K', ('AGU', 'AGC') : 'S', ('AGA', 'AGG') : 'R', ('GUU', 'GUC', 'GUA', 'GUG') : 'V', ('GCU', 'GCC', 'GCA', 'GCG') : 'A', ('GAU', 'GAC') : 'D', ('GAA', 'GAG') : 'E', ('GGU', 'GGC', 'GGA', 'GGG') : 'G'}
    stopCodons = ['UUA', 'UAG', 'UGA']
    
    for i in range(len(s)):
        while x != len(s):
            codone = s[x : x + 3]
            triplets.append(codone)
            x+= 3
    
    for x in triplets:
        for i in proteins.keys():
            if x in i:
                translation = proteins.get(i)
                myProtein+= translation
            if x in stopCodons:
                myProtein+= ''
        
    return myProtein