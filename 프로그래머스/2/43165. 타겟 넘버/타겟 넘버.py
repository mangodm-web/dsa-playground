from typing import List

def dfs(numbers: List[int], target: int, depth: int = 0, cum_sum: int = 0) -> int:
    if depth == len(numbers):
        if cum_sum == target:
            return 1
        else:
            return 0
    
    add_path = dfs(numbers, target, depth + 1, cum_sum + numbers[depth])
    subtract_path = dfs(numbers, target, depth + 1, cum_sum - numbers[depth])
    
    return add_path + subtract_path

def solution(numbers: List[int], target: int) -> int:
    return dfs(numbers, target)
