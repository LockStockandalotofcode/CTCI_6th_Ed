import random, bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # generate a random integer between 1 and total sum (both inclusive)       
        target = random.randint(1, self.total_sum)

        # Binary search to find first value >= target
        # bisect_left returns the leftmost point of insertion
        return bisect.bisect_left(self.prefix_sums, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()