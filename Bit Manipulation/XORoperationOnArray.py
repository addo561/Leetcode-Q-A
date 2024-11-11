link = 'https://leetcode.com/problems/xor-operation-in-an-array/description/'

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        array = []
        for  i in range(n):
            array.append(start + 2 * i)
        num = start
        for i in range(1,n):
            num ^= array[i]  
        return num