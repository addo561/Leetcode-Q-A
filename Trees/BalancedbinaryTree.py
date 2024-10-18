from typing import Optional
from invertTree import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            right_h = helper(node.right)  
            left_h = helper(node.left)

            if right_h == -1 or left_h == -1 or abs(left_h - right_h) > 1:
                return -1
            return 1 + max(left_h,right_h)   
        helper(root)
        return helper(root) != -1       

        