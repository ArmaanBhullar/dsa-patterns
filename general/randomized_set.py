"""
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""
class RandomizedSet:
    import random
    def __init__(self):
        self.dict = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = 1
            self.vals.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        # print(val, self.dict)
        if val not in self.dict:
            return False
        else:
            del self.dict[val]
            return True

    def getRandom(self) -> int:
        random_number = int(random.random() * len(self.vals))
        while (self.vals[random_number] not in self.dict):
            random_number = int(random.random() * len(self.vals))
        return self.vals[random_number]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
