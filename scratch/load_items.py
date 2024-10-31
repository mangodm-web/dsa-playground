# 주어진 물건의 무게 목록(weights)에서 바구니의 무게 제한(limit)을 넘지 않으면서,
# 최대한 많은 물건을 담을 수 있는 프로그램을 작성해보자.

from typing import List


def load_items(weights: List[int], limit: int) -> int:
    result = -1

    def dfs(index: int, current_sum: int, total_sum: int) -> None:
        nonlocal result

        if current_sum + (sum(weights) - total_sum) < result:
            return

        if current_sum > limit:
            return

        if index == len(weights):
            result = max(result, current_sum)
            return

        dfs(index + 1, current_sum + weights[index], total_sum + weights[index])
        dfs(index + 1, current_sum, total_sum + weights[index])

    dfs(0, 0, 0)

    return result


if __name__ == "__main__":
    weights = [81, 58, 42, 33, 61]
    limit = 259

    result = load_items(weights, limit)

    assert result == 242
