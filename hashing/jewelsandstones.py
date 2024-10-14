#soln

def numJewelsInStones(self, jewels, stones):
    hashsj = set(jewels)
    count = 0
    for stone in stones:
        if stone in hashsj:
            count +=1
    return count        