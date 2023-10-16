"""
https://leetcode.com/problems/text-justification/description/
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_count_processed = 0
        not_done = True

        def justify(ls: List[str], width: int, is_end: bool) -> str:
            if len(ls) == 1:
                return f"{ls[0]}" + " " * (width - len(ls[0]))
            if is_end:
                first = " ".join(ls)
                return f"{first}" + " " * (width - len(first))
            else:
                fill_counter = sum([len(word) for word in ls])
                extra_space = width - fill_counter
                start_space = extra_space // (len(ls) - 1)
                num_spaces = [start_space for i in range(len(ls) - 1)]
                remaining = extra_space % (len(ls) - 1)
                for i in range(remaining):
                    num_spaces[i] += 1
                str_builder = ""
                for i in range(len(ls)):
                    str_builder += ls[i]
                    if i != len(ls) - 1:
                        str_builder += " " * num_spaces[i]
                return str_builder

            return " ".join(ls)

        ls_answer = []
        while not_done:
            start = word_count_processed
            end = start
            run_length = len(words[start]) + 1
            while (end + 1 < len(words)) and (run_length + len(words[end + 1]) <= maxWidth):
                # if adding new word is possible
                end += 1
                run_length += len(words[end]) + 1
            if end + 1 == len(words):
                ls_answer.append(justify(words[start: end + 1], maxWidth, is_end=True))
            else:
                ls_answer.append(justify(words[start: end + 1], maxWidth, is_end=False))
            if end + 1 == len(words):
                not_done = False
            word_count_processed = end + 1

        return ls_answer