import pytest
from typing import List


def solution(L: List[int], x: int, l: int, u: int) -> int:
    """
    리스트 L과 그 안에서 찾으려 하는 원소 x, 탐색 구간의 lower bound, upper bound가 주어질 때,
    x와 같은 값을 가지는 원소의 인덱스를 리턴한다.

    Args:
        L (List[int]): 정렬된 정수 리스트 (중복된 원소는 없다.)
        x (int): 찾을 정수
        l (int): 탐색의 lower bound
        u (int): 탐색의 upper bound

    Returns:
        int: x의 인덱스를 반환, x가 리스트 L 안에 없으면 -1을 반환
    """
    if l > u:
        return -1
    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    if x < L[mid]:
        return solution(L, x, l, mid - 1)
    return solution(L, x, mid + 1, u)


@pytest.mark.parametrize(
    "L, x, expected",
    [
        ([2, 3, 5, 6, 9, 11, 15], 6, 3),
        ([2, 5, 7, 9, 11], 4, -1),
        ([], 4, -1),
        ([2, 5, 7, 9, 11], 2, 0),
        ([2, 5, 7, 9, 11], 11, 4),
        ([11], 11, 0),
    ],
)
def test_solution(L, x, expected):
    assert solution(L, x, 0, len(L) - 1) == expected
