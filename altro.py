sasso = 'ATGATTAGGCCCACCCAGACGAGATTAGTGATGCAGTGACAGACACAGATTATATGTGTCAAATACGCGGAATGTCTCGCCTAAGTCTAGGGTCACAGTTCGGATCGCGGCGTCAATATGGGTACCGATCATTTTCCCCTCGCCGATGCGCTCGTAGTTTGTCGCGTAAGTTCAAACCGCTTTTTGAAGCGGCCAGGGGCTCCAACAGTGACAGGCCGGAATAAAGAGCGACGTTCTAAGTGATGACTACGCTAGTCCTTTAGCGCTATGTAGCTCCCGCAATGTTCTGAAGTATTGACCAAGGCCGTAGCATAAATTAATTCAAATATGATCAATAAAGATGGTAGCGTACCTCTTCTGTTCGTTCTACACCCTTTGATAACAATCCTGCTGCGCAATAACACAAAAGAATAACCTTACCAAACTCGGGGCCTTGGATTTCAAGACAAGGCCAATAGTACCGCACGACCCCTCGCTGTCGGGAGATATTAAGGCCTGACGACCCAAATCTAAGCTAATGGTCATCGACCTTGGTACCTGCAGACGGCAGTACGCCGATGATCGGATACCCCGAAGTCATAATAATACGTCTCGGTAACTACTCGATTCAAGAGCACACCACGTCTGATCTATATAGGCTTGGGTTGCTTCCTCAGCCAAACCTTCGAAGTCTGGGGCGGTGCTTGTCCTGAACGCAAGGTCTGCATCTCTTCCCCTGACCGAGATATCGGTCTCCGTGTGCTTACATTCGCCCCTGATTTGCCCTCGCCTCCTGGCGTCAACTGATACGGCGCTAACGGGCTCTGATCATGTTAGATTCAGGCTCCTTTCTTAGCAACCGTTTGGTATGCCTAGATGCCCTCGATACTGTGGTCCCAGTTATCCCTACTGCTACACTTTTTTCTAGATGTAA'

newsasso = ''

for i in range(len(sasso)):
    if sasso[i] == 'A':
        newsasso = 'T'+ newsasso
    if sasso[i] == 'T':
        newsasso = 'A'+ newsasso
    if sasso[i] == 'G':
        newsasso = 'C'+ newsasso
    if sasso[i] == 'C':
        newsasso = 'G' + newsasso

print(newsasso)