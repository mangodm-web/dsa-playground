import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        self.cum_sums = []
        cum_sum = 0

        for weight in w:
            cum_sum += weight
            self.cum_sums.append(cum_sum)
        self.total_sum = cum_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        index = bisect.bisect_left(self.cum_sums, target)
        
        return index
