def pointMutations(seq1, seq2):
    mutCount = 0
    
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutCount+=1
    
    return mutCount
