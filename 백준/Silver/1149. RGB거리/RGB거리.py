# RGB거리

from typing import List


def solution(N: int, arr: List[List[int]]) -> int:
	dp = [[0 for _ in range(3)] for _ in range(N)]

	for i in range(N):
		for j in range(3):
			dp[i][j] = arr[i][j]
			dp[i][j] += min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

	return min(dp[-1])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, arr))
