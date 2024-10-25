from typing import List


link = 'https://leetcode.com/problems/permutations/description/'

def permute( nums: List[int]) -> List[List[int]]:
    result = []  # To store all permutations

    def permuteR(n, idx):
        if idx == len(n) - 1:
            result.append(n[:])  # Add a copy of the current permutation to the result
            return
        
        for i in range(idx, len(n)):
            n[idx], n[i] = n[i], n[idx]  # Step 1: Swap elements to create a new permutation
            
            permuteR(n, idx + 1)         # Step 2: Recurse with the new arrangement
            
            n[idx], n[i] = n[i], n[idx]  # Step 3: Undo the swap to restore original state(BACKTRACKING)

    permuteR(nums, 0)
    return result
