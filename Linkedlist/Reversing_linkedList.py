link = 'https://leetcode.com/problems/reverse-linked-list/description/'


class ListNode:
    def __init__(self,val=0,next=None):
        self.data =data
        self.next = next


class solution:
    def reverse_linkedlist(self,head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next # store next element in next_node
            curr.next = prev  # reverse list / remove pointer 
            prev = curr # move prev forward
            curr = next_node #move curr forward

        return prev    # e.i last element of list
