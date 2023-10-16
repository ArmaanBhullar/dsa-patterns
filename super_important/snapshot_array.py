"""
https://leetcode.com/problems/snapshot-array/description/
"""
class SnapshotArray:

    def __init__(self, length: int):
        # maintain a dict of ordereddict
        self.cache = defaultdict(OrderedDict)
        self.snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        # TODO add check for length
        self.cache[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx_history = self.cache[index]
        # now find entry for snap_id
        if snap_id in idx_history:
            return idx_history[snap_id]
        else:
            # will have to search, thanks to the ordered dict, we can do binary search
            keys = list(idx_history.keys())
            bisect_idx = bisect.bisect(keys, snap_id)
            if bisect_idx == 0:
                return 0
            else:
                return idx_history[keys[bisect_idx - 1]]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)