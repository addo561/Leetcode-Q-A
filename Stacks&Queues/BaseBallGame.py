from typing import List


link = 'https://leetcode.com/problems/baseball-game/'

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for value in operations:
            if value.isdigit() or (value[0]=='-' and value[1:].isdigit()):
                record.append(int(value))
            elif value == '+':
                record.append(sum(record[-2:]))
            elif value == 'D':
                record.append(2 * (record[-1]))
            elif value == 'C':
                record.pop()

        return sum(record)                    