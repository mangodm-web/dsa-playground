from collections import deque
import math


def solution(progresses, speeds):
    result = []
    days_remaining = deque(math.ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    
    while days_remaining:
        current_day = days_remaining.popleft()
        features_deployed = 1
        
        while days_remaining and days_remaining[0] <= current_day:
            days_remaining.popleft()
            features_deployed += 1
            
        result.append(features_deployed)

    return result
