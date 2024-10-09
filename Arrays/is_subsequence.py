link = 'https://leetcode.com/problems/is-subsequence/description/'


def is_subsequence(s,t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)        