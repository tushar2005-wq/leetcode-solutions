# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        curr = head
        length = 1
        
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        k = k % length
        steps = length - k
        
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        