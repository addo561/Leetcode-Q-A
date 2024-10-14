link = 'https://leetcode.com/problems/valid-parentheses/'

class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')':'(', 
            '}':'{', 
            ']':'['
            }
        stack = []

        for p in s:
            if p not in hashMap:
                stack.append(p)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() != hashMap[p]:
                        return False 

        return not stack