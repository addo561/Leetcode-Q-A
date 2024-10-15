link = 'https://leetcode.com/problems/search-insert-position/submissions/1403309188/'



class Solution(object):
    def searchInsert(self, nums, target):
        f,l = 0,len(nums)-1

        while f<=l:
            mid = f + (l - f)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                f = mid + 1
            else:
                l = mid - 1
        return f    
        