# 1부터 n까지 번호가 적힌 구슬이 있다.
# 이중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력한다.


def permutate(n: int, m: int) -> None:
    selected = [0] * m
    checked = [0] * (n + 1)

    def dfs(level: int) -> None:
        if level == m:
            for num in selected:
                print(num, end=" ")
            print()
        else:
            for num in range(1, n + 1):
                if num not in checked:
                    checked[num] = 1
                    selected[level] = num
                    dfs(level + 1)
                    checked[num] = 0

    dfs(0)


if __name__ == "__main__":
    n, m = 3, 2

    permutate(n, m)
