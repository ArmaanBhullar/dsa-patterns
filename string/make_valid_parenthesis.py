"""

"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # store positions of all parenthesis
        n = len(s)
        new_ls = list(s)
        ls = []  # list of tuple - (id, index, left or right pren)
        id_ = 0
        for i in range(n):
            if s[i] == '(':
                ls.append([id_, i, '('])
                id_ += 1
            elif s[i] == ')':
                ls.append([id_, i, ')'])
                id_ += 1
            else:
                pass
        stack = []
        for element in ls:
            # print(stack, element)
            # if matches, then destroy, else add
            if element[2] == ')':
                if (len(stack) > 0) and (stack[-1][2] == '('):
                    stack.pop()
                else:
                    stack.append(element)
            else:
                stack.append(element)
        # now go over remaining stack elements and remove them from original string
        # print(stack)
        while len(stack) > 0:
            cur = stack.pop()
            idx = cur[1]
            # remove this id_ element from the list
            del new_ls[idx]
        return ''.join(new_ls)
