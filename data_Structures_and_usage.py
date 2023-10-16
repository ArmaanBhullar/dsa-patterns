# Usage of queue
from collections import deque
q = deque([])
q.append(9)
q.append(8)
while q:
    print(q.popleft())

# Usage of stack
stack = []
stack.append(9)
stack.append(8)
while stack:
    print(stack.pop())

# Usage of heap
import heapq
heap = []
heapq.heappush(heap, (10, "oiu"))
heapq.heappush(heap, (3, "342"))
heapq.heappush(heap, (100, "675"))
while heap:
    print(heapq.heappop(heap))

# Usage of priority Queue


# Use of bisect module - returns i, if i==0, it's less than everything. If i == len(ls), it's greater than everything,
# else element is >= i-1 and < i
import bisect
ls = [4, 6, 90, 132]
print(bisect.bisect(ls, 90)) # returns 3
print(bisect.bisect(ls, 89)) # 2
print(bisect.bisect(ls, 9000)) # 4
print(bisect.bisect(ls,-10)) # 0

# OrderedDict
from collections import OrderedDict
d = OrderedDict()
d[5] = 90
d[-1] = 89
d[200] = 80
print(list(d.keys()))


Trie = {}
def add_word(word: str) -> None:
    # adds word to trie
    trie = Trie
    for char in word:
        if char in trie:
            trie = trie[char]
        else:
            trie[char] = {}
            trie = trie[char]
    # mark word as ended
    if '$' in trie:
        trie['$'] += 1
    else:
        trie['$'] = 1

add_word("abs")
add_word("abw")
add_word("abs")
add_word("yui")
add_word("yo")
print("Contents of Trie = ")
print(Trie)