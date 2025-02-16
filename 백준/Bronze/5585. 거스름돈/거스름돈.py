# 거스름돈
def calculate_min_coins(payment: int) -> int:
	COINS = [500, 100, 50, 10, 5, 1]
	answer = 0
	change = 1000 - payment

	for coin in COINS:
		answer += (change // coin)
		change %= coin

	return answer

amount = int(input())
print(calculate_min_coins(amount))
