"""
https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150
"""

class LRUCache:
    import heapq
    def __init__(self, capacity: int):
        self.n = capacity
        self.dict = {}  # stores key: (val, idx)
        self.idx = 0
        self.heap = []

    def get(self, key: int) -> int:
        # print(self.dict)
        if key in self.dict:
            val = self.dict[key][0]
            self.dict[key] = (val, self.idx)
            heapq.heappush(self.heap, (self.idx, key))
            self.idx += 1
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.dict) >= self.n and (key not in self.dict):
            # print("entered for ", key, value, self.dict)
            # get the least recently used from the heap and delete it's key, val first before adding
            old_idx, old_key = heapq.heappop(self.heap)
            while old_idx != self.dict[old_key][1]:
                # keep popping till you reach the most up to date value
                old_idx, old_key = heapq.heappop(self.heap)
            # now delete the old key
            del self.dict[old_key]
        self.dict[key] = (value, self.idx)
        # add in heap also
        heapq.heappush(self.heap, (self.idx, key))
        self.idx += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


######################
# Linked List based solution
#####################
class DListNode:
    def __init__(self, val: int = 0, key: int = 0, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class DList:
    def __init__(self):
        self.pre_head = DListNode()
        self.post_tail = DListNode()
        self.pre_head.next = self.post_tail
        self.post_tail.prev = self.pre_head

    def insert(self, node):
        # connect to pre tail
        pre = self.post_tail.prev
        pre.next = node
        node.prev = pre
        # connect to tail
        node.next = self.post_tail
        self.post_tail.prev = node
        return node

    def delete(self, node):
        # print(node.val, node.prev, node.next)
        # delete this node from the list
        # disconnect from pre
        pre = node.prev
        post = node.next
        # link pre and post
        pre.next = post
        post.prev = pre
        node.next = None
        node.prev = None
        return node

    def delete_head(self) -> None:
        post = self.pre_head.next
        self.delete(post)
        return post

    def __str__(self):
        values = []
        start = self.pre_head
        while start:
            values.append(str(start.val))
            start = start.next
        return ",".join(values)


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}  # key -> DListNode
        self.n = capacity
        self.ll = DList()

    def get(self, key: int) -> int:
        # print("Get", key)
        # new or existing
        if key not in self.dict:
            return -1
        else:
            # get val and update ll
            val_node = self.dict[key]
            # print(self.ll)
            self.ll.delete(val_node)
            self.ll.insert(val_node)
            # print(self.ll)
            return val_node.val

    def put(self, key: int, value: int) -> None:
        # print("Put", key, value)
        # print(self.ll)
        # case 1 it's an update
        if key in self.dict:
            val_node = self.dict[key]
            val_node.val = value
            val_node = self.ll.delete(val_node)
            val_node = self.ll.insert(val_node)
            self.dict[key] = val_node
        # case 2 - new and over capacity
        else:
            if len(self.dict) == self.n:
                # remove first node from ll and insert
                deleted_node = self.ll.delete_head()
                del self.dict[deleted_node.key]
            new_node = DListNode(val=value, key=key)
            self.dict[key] = self.ll.insert(new_node)
        # print(self.ll)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)