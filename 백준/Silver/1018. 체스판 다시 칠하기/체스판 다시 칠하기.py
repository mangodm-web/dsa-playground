def create_boards():
    board1 = [["W" if (i + j) % 2 == 0 else "B" for j in range(8)] for i in range(8)]
    board2 = [["B" if (i + j) % 2 == 0 else "W" for j in range(8)] for i in range(8)]
    return board1, board2

def find_min_repaints(y: int, x: int) -> int:
    diff_with_white_start = sum(target[y + i][x + j] != board1[i][j] for i in range(8) for j in range(8))
    diff_with_black_start = sum(target[y + i][x + j] != board2[i][j] for i in range(8) for j in range(8))
    return min(diff_with_white_start, diff_with_black_start)

board1, board2 = create_boards()

N, M = map(int, input().split())
target = [input().strip() for _ in range(N)]

min_repaints = float("inf")

for y in range(N - 7):
    for x in range(M - 7):
        min_repaints = min(min_repaints, find_min_repaints(y, x))

print(min_repaints)
