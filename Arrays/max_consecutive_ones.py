from typing import List


link = 'https://leetcode.com/problems/max-consecutive-ones-iii/'

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = curr = ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                curr += 1
            while curr > k:
                if nums[l] == 0:
                    curr -= 1
                l  += 1
            ans = max(ans,r-l+1)   
        return ans          