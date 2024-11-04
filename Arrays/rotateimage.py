from typing import List


link = 'https://leetcode.com/problems/rotate-image/description/'

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lr = len(matrix)
        lc = len(matrix[0])  
        for i in range(lr):
            for j in range(i + 1,lc):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(lr):
            matrix[i].reverse()  