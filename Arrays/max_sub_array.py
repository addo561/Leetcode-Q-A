link = 'https://leetcode.com/problems/maximum-average-subarray-i/description/'

class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k , len(nums)):
            curr_sum += nums[i] - nums[i - k]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum/float(k)        