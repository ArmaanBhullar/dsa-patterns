"""
https://leetcode.com/problems/my-calendar-i/description/
"""
class MyCalendar:

    def __init__(self):
        # maintain sorted list of events, sorted by start times
        self.starts = []  # empty calendar to start with
        self.ends = []

    def add(self, pos, start, end) -> None:
        self.starts.insert(pos, start)
        self.ends.insert(pos, end)

    def book(self, start: int, end: int) -> bool:
        # find index of this start event
        if len(self.starts) == 0:
            self.add(0, start, end)
            return True

        idx = bisect.bisect(self.starts, start)

        if idx == len(self.starts):
            if self.ends[-1] <= start:
                self.add(idx, start, end)
                return True
            return False
        if idx == 0:
            # at the end
            if self.starts[0] >= end:
                self.add(idx, start, end)
                return True
            return False
        else:  # middle somewhere
            # at the end
            if self.starts[idx] >= end and self.ends[idx - 1] <= start:
                self.add(idx, start, end)
                return True
            else:
                return False
