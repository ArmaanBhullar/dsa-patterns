"""
https://leetcode.com/problems/zigzag-conversion/description/
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (len(s) < numRows) or (numRows == 1):
            return s

        rows = [[] for i in range(numRows)]
        for i in range(numRows):
            first_step = 2 * (numRows - 1 - i)
            second_step = 2 * i
            # print(f"Row = {i}")
            # build each row
            row = [i]
            summer = i
            counter = 0
            while summer < len(s) and counter <= len(s):
                step = (counter % 2) * (second_step) + ((counter + 1) % 2) * (first_step)
                # print(f"Summer = {summer}, step = {step}, counter = {counter}, fs={first_step}, ss = {second_step}")
                counter += 1
                summer += step
                if summer != row[-1] and summer < len(s):
                    row.append(summer)
            rows[i] = row
        # print(rows)
        indices = itertools.chain(*rows)
        return "".join([s[idx] for idx in indices])

