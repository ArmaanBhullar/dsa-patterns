# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:
            # returns reversed ll
            # create a stack
            ls = []
            while node:
                ls.append(node)
                node = node.next
            # now get nodes from stack one by one and join them
            pre_head = ListNode()
            head = pre_head
            while len(ls) > 0:
                cur = ls.pop()
                # make sure to fix the node properly
                cur.next = None
                head.next = cur
                head = head.next
            return pre_head.next, head

        idx = 1
        start_all = head
        start_reverse = None
        end_reverse = None
        pre_reverse = None
        start_non_reverse = None
        while head:
            if idx == left - 1:
                pre_reverse = head
            if idx == left:
                start_reverse = head
            if idx == right:
                tail_reverse = head
            if idx == right + 1:
                start_non_reverse = head
            idx += 1
            head = head.next
        # now we know what to reverse exactly
        # separate out the middle part
        if pre_reverse:
            pre_reverse.next = None
        tail_reverse.next = None
        start, end = reverse(start_reverse)
        # print(start, end, pre_reverse, start_non_reverse)
        # now join back
        if pre_reverse:
            pre_reverse.next = start

        if start_non_reverse:
            end.next = start_non_reverse
        # what to return?
        if left > 1:
            return start_all
        else:
            return start



