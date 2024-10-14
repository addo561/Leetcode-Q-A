def Anagram(s,t):
    hashT = {}
    for c in s:
        if c in hashT:
            hashT[c] +=1 # if letter already in counter ,increase counter by 1
        else:
            hashT[c] = 1    
        
    for ch in t:
        if ch not in hashT or hashT[ch]==0:
            return False
        hashT[ch] -=1

    return all(values == 0 for values in hashT.values())                
