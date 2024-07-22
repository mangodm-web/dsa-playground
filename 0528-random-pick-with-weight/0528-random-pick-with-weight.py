import random

class Solution:
    def __init__(self, w: List[int]):
        self.interval = []
        cum_sum = 0

        for weight in w:
            prev_sum = cum_sum
            cum_sum += weight
            self.interval.append([prev_sum, cum_sum])
        self.total_sum = cum_sum

    def pickIndex(self) -> int:
        random_ind = random.randint(0, self.total_sum - 1)
        for i in range(len(self.interval)):
            p, c = self.interval[i]
            if p <= random_ind < c:
                return i
