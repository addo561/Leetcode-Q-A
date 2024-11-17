from typing import List


link = 'https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/'


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l]+numbers[r] > target:
                r -=1
            elif  numbers[l]+numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]  
        