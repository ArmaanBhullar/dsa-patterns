class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # at each point expand or contract the sliding window and store result on right side
        n = len(s)
        char_pos = {}
        ans = 0
        for j in range(n):
            if s[j] in char_pos:
                i = char_pos[s[j]] + 1
            char_pos[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans



    def lengthOfLongestSubstring(self, s: str) -> int:
            # at each point expand or contract the sliding window and store result on right side
            n = len(s)
            ans = [1 for i in range(len(s))]
            i, j = 0, 0
            run_dict = defaultdict(int)
            while j < n:
                while run_dict[s[j]] != 0:
                    print(i, j)
                    run_dict[s[i]] -= 1
                    i += 1
                run_dict[s[j]] += 1
                ans[j] = len([val for val in run_dict.values() if val == 1 ])
                j += 1
            if len(ans) > 0:
                return max(ans)
            return 0


    def lengthOfLongestSubstring2(self, s: str) -> int:
        # at each point what's the answer including this char, then take max
        ans = []
        for i in range(len(s)):
            ans_set = set([s[i]])
            for j in range(i-1, -1, -1):
                if s[j] not in ans_set:
                    ans_set.add(s[j])
                else:
                    break
            ans.append(len(ans_set))
        if ans:
            return max(ans)
        return 0