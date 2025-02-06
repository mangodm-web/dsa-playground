combination = []
VOWELS = {"a", "e", "i", "o", "u"}

def is_valid(s):
	vowel_count = 0

	for char in s:
		if char in VOWELS:
			vowel_count += 1	

	consonant_count = len(s) - vowel_count

	return vowel_count >= 1 and consonant_count >= 2

def print_combinations(index, level):
	global L, C, arr, combination

	if level == L:
		combination_str = "".join(combination)

		if is_valid(combination_str):
			print(combination_str)	
		return

	for i in range(index, C):
		combination.append(arr[i])
		print_combinations(i + 1, level + 1)
		combination.pop()

while True:
	try:
		L, C = map(int, input().split(" "))
		arr = sorted(input().split(" "))
		print_combinations(0, 0)
	except:
		break
