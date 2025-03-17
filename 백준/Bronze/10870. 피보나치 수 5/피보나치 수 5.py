from typing import List


def fib(n: int) -> int:
	if n <= 1:
		return n

	a, b = 0, 1
	
	for i in range(2, n + 1):
		a, b = b, a + b

	return b

def solution():
	n = int(input())
	
	answer = fib(n)
	
	print(answer)

solution()
