"""
https://leetcode.com/problems/reorder-list/description/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        if head.next is None:
            return head
        tail = head
        ls = []
        while tail is not None:
            ls.append(tail)
            tail = tail.next
        n = len(ls)
        num_nodes = 1
        new_head = head
        while (1):
            tos = ls.pop()
            next_head = head.next
            # now change pointers 2 at a time
            head.next = tos
            num_nodes += 1
            if num_nodes == n:
                tos.next = None # mark ll as complete
                break
            tos.next = next_head
            num_nodes += 1
            if num_nodes == n:
                next_head.next = None # mark ll as complete
                break

            head = next_head
        return new_head