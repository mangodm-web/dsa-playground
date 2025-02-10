N, S = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

from itertools import combinations

answer = 0

for i in range(1, N + 1):
	comb = list(combinations(arr, i))

	for combination in comb:
		if sum(combination) == S:
			answer += 1

print(answer)
