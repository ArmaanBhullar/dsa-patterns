"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/?page=2
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # maintain 2 pointers separated by n nodes, when right reaches end, switch on the left one and return
        left = head
        right = head
        # setup the right
        k = 0
        while k < n:
            right = right.next
            k += 1

        if right is None:
            head = head.next
            return head

        # now move both together till right reaches end
        while right.next is not None:
            left = left.next
            right = right.next

        if left.next is not None:
            # Now, change left parent to left
            left.next = left.next.next
        else:
            left.next = None

        return head

