#Problem link 
'https://leetcode.com/problems/two-sum/'


#Solution
def Twosum(nums,Target):
    n = len(nums)
    for i in range(n):# loop through indexes 
        complement = Target - nums[i] # create a complement variable (complement + num gives you the target)
        if complement in nums[i+1:]:# check for the complement number in nums
            return [i,nums.index(complement,i+1)] #return index of complement and num that sum up to target
