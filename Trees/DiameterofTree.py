from typing import Optional
from invertTree import TreeNode

link = 'https://leetcode.com/problems/diameter-of-binary-tree/'

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def helper(node):
            if not node:
                return 0
            right_h = helper(node.right)  
            left_h = helper(node.left)
            self.diameter = max(self.diameter,left_h + right_h)
            return 1 + max(left_h , right_h )  
        
        helper(root)
        return   self.diameter     
