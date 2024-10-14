from typing import Optional

from Linkedlist.Linkedlist_cycle import ListNode # using listnode from linkedlist cycle proplem


link = 'https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head 
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next   
        return head  