"""
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
Use the tuple of indices approach as hashmap doesn't scale well.
Construct list of tuples of non zero places and use two pointers to iterate
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.sparse = []
        for i in range(self.size):
            if nums[i] != 0:
                self.sparse.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        one, two = self.sparse, vec.sparse
        if len(one) == 0 or len(two) == 0:
            return 0
        else:
            if one[-1][0] < two[-1][0]:
                one, two = two, one
        # one ends further than two
        i, j = 0, 0
        summ = 0
        while (j < len(two)):
            idx_1 = one[i][0]
            idx_2 = two[j][0]
            if idx_1 == idx_2:
                summ += one[i][1] * two[j][1]
                i += 1
                j += 1
            elif idx_1 < idx_2:
                # advance 1
                i += 1
            else:
                # advance 2
                j += 1
        return summ

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)