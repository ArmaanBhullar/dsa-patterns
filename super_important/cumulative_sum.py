"""
https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # maintain a sum dict, where key is sum, value is # times that sum occurs
        # iterate over each sum and find if sum - k exists in the dict, if it does, add it's val to the counter
        # each sum - sum represents a subarray
        sum_dict = defaultdict(int)
        sum_dict[0] = 1 # 0 occurs once by default
        cum_sum = 0
        counter = 0
        for num in nums:
            cum_sum += num
            # print(sum_dict, cum_sum, cum_sum - k)
            if cum_sum - k in sum_dict:
                counter += sum_dict[cum_sum - k]
            sum_dict[cum_sum] += 1 # update dict after you're done searching in prev part
        return counter
