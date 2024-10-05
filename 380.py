import random 

class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.numsList = []

    def insert(self, val: int) -> bool:
        inserted = val not in self.numsMap
        if inserted:
            self.numsMap[val] = len(self.numsList)
            self.numsList.insert(len(self.numsList), val)
        return inserted

    def remove(self, val: int) -> bool:
        exists = val in self.numsMap
        if exists:
            idx = self.numsMap[val]
            lastValue = self.numsList[-1]
            self.numsList[idx] = lastValue            
            self.numsMap[lastValue] = idx
            del self.numsMap[val]
            self.numsList.pop()
        return exists

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:

obj = RandomizedSet()

obj.insert(3)
obj.remove(3)

# param_2 = obj.remove(val)
# param_3 = obj.getRandom()