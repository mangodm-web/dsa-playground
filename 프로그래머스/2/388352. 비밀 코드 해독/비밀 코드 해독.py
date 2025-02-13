from itertools import combinations
from typing import List


def count_matches(a: List[int], b: List[int]) -> int:
    intersection = set(a) & set(b)
    
    return len(intersection)

def solution(n: int, q: List[List[int]], ans: List[int]) -> int:
    answer = 0
    pools = list(combinations(range(1, n + 1), 5))
    
    for pool in pools:
        is_passed = all(count_matches(pool, candidate) == expected for candidate, expected in zip(q, ans))
        
        if is_passed:
            answer += 1

    return answer
