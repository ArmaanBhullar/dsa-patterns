"""
https://leetcode.com/problems/find-and-replace-in-string/description/
"""
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # build soln, assume indices are sorted
        # sort indices
        sorted_indices = [ x[0] for x in sorted(enumerate(indices), key = lambda x: x[1])]
        indices = [indices[i] for i in sorted_indices]
        sources = [sources[i] for i in sorted_indices]
        targets = [targets[i] for i in sorted_indices]
        # print(indices, sources, targets)
        new_s = s[:indices[0]]
        k = len(indices)
        for i in range(k):
            idx = indices[i]
            source = sources[i]
            target = targets[i]
            # what if does not match?
            if s[idx: idx + len(source)] == source:
                new_s += target
                idx += len(source)
            # fill remaining till next
            if i < k-1:
                next_idx = indices[i+1]
            else:
                next_idx = len(s)
            new_s += s[idx: next_idx]
        return new_s