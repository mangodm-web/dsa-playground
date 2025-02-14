def dfs(numbers, target, depth=0, cum_sum=0):
    if depth == len(numbers):
        return int(cum_sum == target)

    return (
        dfs(numbers, target, depth + 1, cum_sum + numbers[depth])
        + dfs(numbers, target, depth + 1, cum_sum - numbers[depth])
    )


def solution(numbers, target):
    return dfs(numbers, target)
