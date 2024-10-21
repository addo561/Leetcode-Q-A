link = 'https://leetcode.com/problems/symmetric-tree/submissions/1429508493/'
from typing import Optional
from invertTree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and mirror(t1.right,t2.left)  and mirror(t1.left,t2.right)      
        
        return mirror(root,root)

        