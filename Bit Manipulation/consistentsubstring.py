from typing import List


link = 'https://leetcode.com/problems/count-the-number-of-consistent-strings/description/'

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for s in words:
            for c in s:
                if c not in allowed:
                    break
            else:
                count += 1    
        return count            