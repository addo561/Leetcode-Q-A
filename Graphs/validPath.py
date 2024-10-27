from ast import List
from collections import defaultdict


link = 'https://leetcode.com/problems/find-if-path-exists-in-graph/'

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        D = defaultdict(list)
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        
        seen = set()
        seen.add(source)
        def dfs(node):
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        dfs(source) 
                   
        return destination in seen 
