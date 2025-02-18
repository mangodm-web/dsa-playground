# 보물

from typing import List


def solution(N: int, A: List[int], B: List[int]) -> int:
	answer = 0

	A_sorted = sorted(A)
	B_sorted = sorted(B, key=lambda x:-x)

	for x, y in zip(A_sorted, B_sorted):
		answer += (x * y)

	return answer

N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

print(solution(N, A, B))
