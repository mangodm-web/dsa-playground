# 01. 정렬된 리스트에 원소 삽입
import pytest
from typing import List


def solution(L: List[int], x: int) -> List[int]:
    """
    리스트 L과 정수 x가 인자로 주어질 때, 리스트 L은 오름차순으로 정렬된 상태이다.
    이 함수는 리스트 내의 올바른 위치에 x를 추가하여 정렬된 상태의 결과 리스트를 반환한다.

    Args:
        L (List[int]): 정렬된 정수 리스트
        x (int): 추가할 정수

    Returns:
        List[int]: 정렬된 리스트에 x가 추가된 새로운 리스트
    """
    for i in range(len(L)):
        if x <= L[i]:
            L.insert(i, x)
            return L

    L.append(x)
    return L


@pytest.mark.parametrize(
    "L, x, expected",
    [
        ([20, 37, 58, 72, 91], 65, [20, 37, 58, 65, 72, 91]),
        ([20, 37, 58, 72, 91], 20, [20, 20, 37, 58, 72, 91]),
        ([20, 37, 58, 72, 91], 10, [10, 20, 37, 58, 72, 91]),
        ([20, 37, 58, 72, 91], 100, [20, 37, 58, 72, 91, 100]),
    ],
)
def test_solution(L, x, expected):
    assert solution(L, x) == expected
