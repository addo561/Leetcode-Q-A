#link
'https://leetcode.com/problems/binary-search/description/'


#Solution
def BinarySearch(nums,target):
    firstIndex = 0
    lastIndex = len(nums)-1
    while firstIndex<=lastIndex:
        middleIndex = (firstIndex + lastIndex) //2
        if nums[middleIndex] ==target:
            return middleIndex
        elif nums[middleIndex] < target:
            firstIndex = middleIndex + 1
        lastIndex = middleIndex - 1 
    return -1       
