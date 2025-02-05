def solution(n):
    if n == 0:
        print("-", end="")
        return
    
    solution(n - 1)
    print(" " * (3 ** (n - 1)), end="")
    solution(n - 1)

while True:
    try:
        N = int(input())
        solution(N)
        print()
    except:
        break
