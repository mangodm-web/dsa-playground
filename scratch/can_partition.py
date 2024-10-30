# n개의 원소로 구성된 자연수 집합이 주어졌을 때,
# 이 집합을 두 개의 부분집합으로 나누었을 때,
# 합이 같은 경우가 존재하면 "YES", 그렇지 않으면 "NO"를 출력하는 프로그램

import sys
from typing import List


class Solution:
    def can_partition(arr: List[int]) -> None:
        n = len(arr)
        total = sum(arr)

        def DFS(L: int, cum_sum: int) -> None:
            if cum_sum > total // 2:
                return
            if L == n:
                if cum_sum * 2 == total:
                    print("YES")
                    sys.exit(0)
            else:
                DFS(L + 1, cum_sum + arr[L])
                DFS(L + 1, cum_sum)

        DFS(0, 0)
        print("NO")


if __name__ == "__main__":
    arr_str = input("자연수 집합을 입력해주세요. (예: 1 2 3 4 5)")
    arr = list(map(int, arr_str.split(" ")))
    Solution.can_partition(arr)
