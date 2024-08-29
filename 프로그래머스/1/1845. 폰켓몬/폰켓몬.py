def solution(nums):
    n_to_choose = len(nums) // 2
    n_unique = len(set(nums))
    
    return min(n_to_choose, n_unique)
