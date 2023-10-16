"""
https://leetcode.com/problems/logger-rate-limiter/description/
"""
class Logger:

    def __init__(self):
        self.msg_dict = {}
        self.msg_queue = deque([])  # stores (timestamp, msg)

    def clean_queue(self, time: int):
        # print(f"Cleaning queue, time = {time}, queue = {self.msg_queue}")
        if self.msg_queue:
            while time - self.msg_queue[0][0] > 10:  # while timestamp
                # these messages are old, clean these up
                _, msg = self.msg_queue.popleft()
                # print(f"Deleting msg={msg}, time={_}")
                if self.msg_dict[msg] == _:
                    del self.msg_dict[msg]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # print(timestamp, message, self.msg_dict)
        if timestamp - self.msg_dict.get(message, float('-inf')) >= 10:
            self.msg_dict[message] = timestamp
            self.msg_queue.append((timestamp, message))
            ans = True
        else:
            ans = False
        self.clean_queue(timestamp)
        return ans

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)