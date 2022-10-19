"""
https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # maintain a heap of first elements of the sorted lists
        # initialize heap
        # while stuff on heap, pop the next item, note the list from where it's popped and add next element from that list on the heap
        import heapq
        heap = [] # (value, list_num)
        n = len(lists)
        for i in range(n):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        ls = []
        while len(heap) > 0:
            val, list_idx = heapq.heappop(heap)
            ls.append(val)
            if lists[list_idx] is not None:
                heapq.heappush(heap, (lists[list_idx].val, list_idx))
                lists[list_idx] = lists[list_idx].next

        if len(ls) == 0:
            return None
        else:
            head = ListNode(ls[0])
            tail = head
            for i in range(1, len(ls)):
                new_node = ListNode(ls[i])
                tail.next = new_node
                tail = tail.next
            return head



