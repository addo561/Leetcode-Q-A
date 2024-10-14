def ransom(ransomNote,magazine):
    counter = {}# introduce a counter
    for c in magazine:
        if c in counter:
            counter[c] +=1 # if letter already in counter ,increase counter by 1
        else:
            counter[c] = 1    #if counter is not in magazine count of letter =1

    for c in ransomNote:
        if c not in counter :# if no counter from runsome in magazine return false
            return False
        elif counter[c]==1:
            del counter[c]# remove counter and if c of  runsome can be found
        counter -=1# decrease counter if c of rumsom can be found

    return True        