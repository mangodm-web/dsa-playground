from itertools import permutations
from typing import List


def solution(k: int, dungeons: List[List[int]]) -> int:
    max_trials = 0
    
    for case in permutations(dungeons):
        temp_k = k
        trials = 0
        
        for min_k, damage in case:
            if temp_k < min_k:
                break
            temp_k -= damage
            trials += 1
            
        max_trials = max(max_trials, trials)
    
    return max_trials
