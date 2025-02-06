choose = []

def combination(arr, c, index=0, level=0):
	if level == c:
		print(" ".join(map(str, choose)))
		return

	for i in range(index, len(arr)):
		choose.append(arr[i])
		combination(arr, c, i + 1, level + 1)
		choose.pop()

while True:
	try:
		arr = list(map(int, input().split(" ")))
		
		if arr == [0]:
			break

		k, S = arr[0], arr[1:]
		combination(S, 6)
		print()

	except:
		break
