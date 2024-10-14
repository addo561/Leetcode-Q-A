link ='https://leetcode.com/problems/plus-one/submissions/'


def Plusone(digits):
    num = int(''.join(map(str,digits))) + 1
    return [int(digits) for digit in str(num)]