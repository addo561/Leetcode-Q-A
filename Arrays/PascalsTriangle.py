#link
'https://leetcode.com/problems/pascals-triangle/description/'

def pascals(numRows):
    res = [[1]] #firstRow
    for i in range(numRows-1):# build all rows according to number of rows
        temp = [0] + res[-1] + [0] #build next row e.i: taking every last element in res list and build upon
        row = [] # every built row
        for j in range(len(res[-1])+1): #take last row list (new row to be built have an extra element)
            row.append(temp[j] +  temp[j + 1])# new row adding of the two elements of previous row
        res.append(row)
    return res        
