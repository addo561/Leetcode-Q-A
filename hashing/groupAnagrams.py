link = 'https://leetcode.com/problems/group-anagrams/'
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # n
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())


        
