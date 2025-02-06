N = int(input())
check = [False] * (N + 1)
permutation = []

def print_permutations(level):
	global N, check, permutation

	if level == N:
		for number in permutation:
			print(number, end=" ")
		print()
		return

	for i in range(1, N + 1):
		if check[i]:
			continue

		permutation.append(i)
		check[i] = True

		print_permutations(level + 1)

		check[i] = False
		permutation.pop()

print_permutations(0)
