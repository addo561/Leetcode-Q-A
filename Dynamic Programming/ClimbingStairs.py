link = 'https://leetcode.com/problems/climbing-stairs/description/'

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:0,1:1,2:2,3:3}
        def c(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = c(x-1) + c(x-2) 
                return memo[x]  
        return c(n)         
