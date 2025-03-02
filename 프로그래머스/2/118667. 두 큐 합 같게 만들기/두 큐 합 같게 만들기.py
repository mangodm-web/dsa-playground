from collections import deque
from typing import List


def solution(queue1: List[int], queue2: List[int]) -> int:
    sum_1, sum_2 = sum(queue1), sum(queue2)
    total = sum_1 + sum_2
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    queue1, queue2 = deque(queue1), deque(queue2)
    num_operations = 0
    LIMIT = (len(queue1) + len(queue2)) * 2
    
    while num_operations <= LIMIT:
        if sum_1 == target:
            return num_operations 
        
        if sum_1 > sum_2:
            num = queue1.popleft()
            sum_1 -= num
            queue2.append(num)
            sum_2 += num
        else:
            num = queue2.popleft()
            sum_2 -= num
            queue1.append(num)
            sum_1 += num
        
        num_operations += 1
        
    return -1
