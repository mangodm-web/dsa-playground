n = int(input())

scores = [tuple(map(int, input().split(" "))) for _ in range(n)]
scores.sort(key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for score in scores[:3]:
	print(score[0], end=" ")
