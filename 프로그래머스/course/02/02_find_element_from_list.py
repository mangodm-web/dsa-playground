# 02. 리스트에서 원소 찾아내기
import pytest
from typing import List


def solution(L: List[int], x: int) -> List[int]:
    """
    리스트 L과 정수 x가 인자로 주어질 때, 정수 x가 발견되는 모든 인덱스를 구하여 이를 리스트에 담아 반환한다.

    Args:
        L (List[int]): 정수 리스트
        x (int): 찾을 정수

    Returns:
        List[int]: 정수 x의 위치가 담긴 리스트, 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1]를 반환
    """
    idx = -1
    answer = []

    while True:
        try:
            idx = L.index(x, idx + 1)
            answer.append(idx)
        except ValueError:
            break

    return answer if answer else [-1]


@pytest.mark.parametrize(
    "L, x, expected",
    [
        ([64, 72, 83, 72, 54], 83, [2]),
        ([64, 72, 83, 72, 54], 72, [1, 3]),
        ([64, 72, 83, 72, 54], 49, [-1]),
    ],
)
def test_solution(L, x, expected):
    assert solution(L, x) == expected
