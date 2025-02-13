from typing import List


def convert_to_mins(time: int) -> int:
    hours, mins = divmod(time, 100)
    
    return (hours * 60) + mins

def solution(schedules: List[int], timelogs: List[int], startday: int) -> int:
    result = 0

    for schedule, timelog in zip(schedules, timelogs):
        is_passed = True

        for j, time in enumerate(timelog):
            day = (startday + j) % 7

            if day in {0, 6}:
                continue

            if convert_to_mins(time) - convert_to_mins(schedule) > 10:
                is_passed = False
                break

        if is_passed:
            result += 1

    return result
