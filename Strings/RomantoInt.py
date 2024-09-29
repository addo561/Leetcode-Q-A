link = 'https://leetcode.com/problems/roman-to-integer/description/'




def R_to_Int(s):
    numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    s = s.replace('IV','IIII').replace('IX','VIIII')# I can be placed before V (5) and X (10) to make 4 and 9. 
    s = s.replace('XL','XXXX').replace('XC','LXXXX')# X can be placed before L (50) and C (100) to make 40 and 90.
    s = s.replace('CD','CCCC').replace('CM','DCCCC')# C can be placed before D (500) and M (1000) to make 400 and 900.
    for char in s:
        ans += numeral[s]
    return ans    