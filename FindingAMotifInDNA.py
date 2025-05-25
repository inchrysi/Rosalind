
def findingMotif(s, t):
    locations = []
    j = len(t)
    
    for i in range(len(s)):
        x = i + j
        if t in s[i : x]:
            locations.append(i + 1) #to make it 1-based

    return print(locations)
