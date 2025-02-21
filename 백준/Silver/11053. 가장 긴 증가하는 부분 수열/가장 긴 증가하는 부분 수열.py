# 가장 긴 증가하는 부분 수열

from typing import List


def solution(N: int, arr: List[List[int]]) -> int:
	dp = [-1 for _ in range(N + 1)]
	dp[1] = 1

	for current_index in range(2, N + 1):
		longest = 0

		for previous_index in range(1, current_index):
			if arr[current_index] > arr[previous_index]:
				longest = max(longest, dp[previous_index])

		dp[current_index] = longest + 1

	return max(dp[1:])

N = int(input())
arr = [0] + list(map(int, input().split()))

print(solution(N, arr))
