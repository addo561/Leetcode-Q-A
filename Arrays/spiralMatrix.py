link = 'https://leetcode.com/problems/spiral-matrix/'


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L,R= 0,len(matrix[0]) 
        T,B = 0, len(matrix)
        merged = []
        while L < R  and T < B:
            for i in range(L,R):
                merged.append(matrix[T][i])
            T += 1

            for i in range(T,B):
                merged.append(matrix[i][R-1])
            R -= 1

            if not (L < R and T < B):
                break

            for i in range(R-1,L-1,-1): 
                merged.append(matrix[B-1][i])
            B -= 1   
            for i in range(B-1,T-1,-1):
                merged.append(matrix[i][L])
            L += 1
        return merged    


                