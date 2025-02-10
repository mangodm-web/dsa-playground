N = int(input())

pools = [num for num in range(100, 1000) if str(num)[0] != str(num)[1] and str(num)[0] != str(num)[2] and str(num)[1] != str(num)[2] and str(num)[1] != "0" and str(num)[2] != "0"]
guesses = []
answer = []

def count_ball(guess, assumed):
	guess_str, assumed_str = str(guess), str(assumed)
	strike, ball = 0, 0

	for i in range(len(guess_str)):
		for j in range(len(guess_str)):
				if i == j and guess_str[i] == assumed_str[i]:
					strike += 1
				if i != j and guess_str[i] == assumed_str[j]:
					ball += 1

	return strike, ball

for i in range(N):
	guess, strike, ball = list(map(int, input().split(" ")))
	guesses.append([guess, strike, ball])

for pool in pools:
	is_ok = True

	for guess in guesses:
		guess, strike, ball = guess
		s, b = count_ball(guess, pool)
		if s != strike or b != ball:
			is_ok = False

	if is_ok:
		answer.append(pool)

print(len(answer))
