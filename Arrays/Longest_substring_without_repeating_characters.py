link = 'https://leetcode.com/problems/longest-substring-without-repeating-characters/description/'

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        Set = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
            Set.add(s[r])

            max_length = max(max_length,r-l+1)
        return max_length    