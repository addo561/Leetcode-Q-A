link = 'https://leetcode.com/problems/majority-element/description/'

def maj(nums):
    n = len(nums)
    for num in range(n):
        if nums.count(num)>(n//2):
            return num