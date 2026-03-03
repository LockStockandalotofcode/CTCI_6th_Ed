class TimeMap:

    def __init__(self):
        # dictionary that stores list of pairs of the form [timestamp, value]
        # keeping timestamp at index [0] in the pair ensures list remains sorted by timestamp value
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = "" # stores required result value

        # get list of values associated with given key
        values = self.store.get(key, [])

        # Binary search for the largest timestamp <= target timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # if timestamp at mid index is less than target timestamp move towards the right-half portion, else left half portion
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)