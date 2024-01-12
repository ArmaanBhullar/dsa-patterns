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
        start_idx_start = bisect.bisect_left(self.starts, start)
        start_idx_end = bisect.bisect_right(self.ends, start)
        end_idx_start = bisect.bisect_left(self.starts, end)
        end_idx_end = bisect.bisect_right(self.ends, end)
        can_be_inserted = (start_idx_start == start_idx_end == end_idx_end == end_idx_start)
        # print(start_idx_start, start_idx_end, end_idx_start, end_idx_end)
        # print(can_be_inserted, start, end, self.starts, self.ends)
        if can_be_inserted:
            self.add(start_idx_start, start, end)
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
