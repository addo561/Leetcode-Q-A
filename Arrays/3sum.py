from typing import List


link = 'https://leetcode.com/problems/3sum/description/'

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #using hashmap
        hashm = {}
        n = len(nums)
        s = set()  
        for i, num in enumerate(nums): 
            if num not in hashm: 
                hashm[num] = [] 
            hashm[num].append(i) 
        for i in range(n): 
            for j in range(i + 1, n): 
                desired = -nums[i] - nums[j] 
                if desired in hashm: 
                    for k in hashm[desired]: 
                        if k != i and k != j: 
                            s.add(tuple(sorted([nums[i], nums[j], desired]))) 
                            break
        #return list(triplet for triplet in s)  
             
        #two-pointer
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
        
        return answer