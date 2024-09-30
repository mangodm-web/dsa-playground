# 03. 이진탐색
import pytest
from typing import List


def solution(L: List[int], x: int) -> int:
    """
    리스트 L과 그 안에서 찾으려 하는 원소 x가 인자로 주어질 때, x와 같은 값을 가지는 원소의 인덱스를 리턴한다.

    Args:
        L (List[int]): 정렬된 정수 리스트 (중복된 원소는 없다.)
        x (int): 찾을 정수

    Returns:
        int: x의 인덱스를 반환, x가 리스트 L 안에 없으면 -1을 반환
    """
    left, right = 0, len(L) - 1

    while left <= right:
        mid = (left + right) // 2

        if L[mid] == x:
            return mid
        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


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
    assert solution(L, x) == expected
