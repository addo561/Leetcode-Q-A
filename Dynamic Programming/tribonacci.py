link = 'https://leetcode.com/problems/n-th-tribonacci-number/description/'

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0,1:1,2:1}
        def tri(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = tri(n-3) + tri(n-2) + tri(n-1)
                return memo[n]   
        return tri(n)        