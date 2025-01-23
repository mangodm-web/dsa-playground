def solution(n, times):
    min_time, max_time = 0, max(times) * n

    while min_time < max_time:
        mid_time = (min_time + max_time) // 2
        people_processed = 0
        
        for time in times:
            people_processed += (mid_time // time)

        if people_processed < n:
            min_time = mid_time + 1
        else:
            max_time = mid_time

    return min_time

