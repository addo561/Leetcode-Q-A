link = 'https://leetcode.com/problems/longest-common-prefix/'
# use Binary search

def LCP_with_binary_search(strs):
    if not strs:
        return ''#checks if list of strings is empty
    minlen = min(len(x) for x in strs)# This line calculates the length of the shortest string in the list strs. This is important because the longest possible common prefix cannot be longer than the shortest string in the list
    low,high = 1,minlen

    while low <= high :
        mid = low + (high - low)//2# prevent overflow instead of  middle = (low + high) // 2
        if isCommonPrefix(strs,mid):
            low = mid + 1
        high = mid - 1    

    return  strs[0][:mid]# After the binary search loop is done, the longest valid prefix length is mid, so we return the substring from the first string (strs[0]) that has this length.

    #This helper function checks if all strings in the list strs share a common prefix of a given length l.
def isCommonPrefix(strs,l):
    str1 = strs[0][:l]

    for string in strs[1:]:
        if not string.startswith(str1):
            return False

    return  True         

strs = ["flower", "flow", "flight"]
print(LCP_with_binary_search(strs))  # Output: "fl"


#soln 2 

def LCP(strs):
    n = len(strs)
    min_length = float('inf')
    i =  0
    for s in strs:
       if len(s) < min_length:
           min_length = len(s)
    
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i +=1
    return strs[0][:i]                