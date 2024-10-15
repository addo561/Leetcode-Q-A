link = 'https://leetcode.com/problems/valid-perfect-square/'

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        l = 1 # use numbers instead if their index
        r = num//2 # use numbers instead if their index

        while l <= r:
            mid = l + (r - l)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                r = mid - 1
            else:
                l = mid + 1
        return False