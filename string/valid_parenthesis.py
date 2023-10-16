"""
https://leetcode.com/problems/valid-parentheses/description/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for char in s:
            if char in ['(', '{', '[']:
                ls.append(char)
            else:
                if len(ls) == 0:
                    return False
                if char == ')':
                    new_char = ls.pop()
                    if new_char != '(':
                        return False

                if char == '}':
                    new_char = ls.pop()
                    if new_char != '{':
                        return False
                if char == ']':
                    new_char = ls.pop()
                    if new_char != '[':
                        return False
        if len(ls) > 0:
            return False
        return True
