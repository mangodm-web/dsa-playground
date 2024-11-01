from typing import List


def find_min_coins_for_change(candidates: List[int], target: int) -> int:
    min_coins = float("inf")

    def dfs(count: int, current_amount: int) -> None:
        nonlocal min_coins

        if count > min_coins or current_amount > target:
            return
        if current_amount == target:
            min_coins = min(min_coins, count)
        else:
            for coin in candidates:
                dfs(count + 1, current_amount + coin)

    dfs(0, 0)

    return min_coins


if __name__ == "__main__":
    candidates = [1, 2, 5]
    target = 25

    candidates.sort(reverse=True)
    answer = find_min_coins_for_change(candidates, target)
    assert answer == 5
