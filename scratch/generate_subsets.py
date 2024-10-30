# 자연수 n이 주어지면 1부터 n까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램


class Solution:
    def generate_subsets(n: int) -> None:
        checked = [0] * (n + 1)

        def DFS(L: int) -> None:
            if L == n + 1:
                for i in range(1, n + 1):
                    if checked[i] == 1:
                        print(i, end=" ")
                print()
            else:
                checked[L] = 1
                DFS(L + 1)
                checked[L] = 0
                DFS(L + 1)

        DFS(1)


if __name__ == "__main__":
    n = int(input("자연수 n을 입력해주세요. (예: 3)"))
    Solution.generate_subsets(n)
