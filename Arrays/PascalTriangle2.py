from typing import List


link = 'https://leetcode.com/problems/pascals-triangle-ii/description/'


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numrows = rowIndex + 1
        res = [[1]]
        for i in range(numrows-1):
            row = []
            temp = [0] + res[-1] + [0]
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res[-1]        

