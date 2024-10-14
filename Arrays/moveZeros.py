link = 'https://leetcode.com/problems/move-zeroes/description/'

def move(nums):
    i = 0 # counter
    for num in nums:
        if num ==0:
            i+=1 # number of zeros
    nums[:] = [ele for ele in nums!=0] # Non zero numbers
    nums += [0] * i   #add zeros to nums     