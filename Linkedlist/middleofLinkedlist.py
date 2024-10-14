link = 'https://leetcode.com/problems/middle-of-the-linked-list/description/'

from typing import Optional
from Linkedlist.Linkedlist_cycle import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count +=1

        count2 = 0
        while head:
            if count//2 == count2:
                return head
            head = head.next
            count2 += 1
            
                    

