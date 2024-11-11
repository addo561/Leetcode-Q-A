link = 'https://leetcode.com/problems/first-letter-to-appear-twice/description/'

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                return c    