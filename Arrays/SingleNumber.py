link = 'https://leetcode.com/problems/single-number/description/'

#bitwise operation
def SingleNumber(nums):
    xor = 0
    for num in nums:
        xor^=num
    return xor    
'''
xor = 0 initializes a variable xor to 0.
The loop for num in nums: iterates over each element in the list nums.
Inside the loop, xor ^= num performs a bitwise XOR operation between the current value of xor and num, then assigns the result back to xor.
After the loop, the final XOR value is returned.  

xor is commutaive and associative
a xor a = 0
a xor 0 = a
'''  