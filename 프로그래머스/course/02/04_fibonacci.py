# 04. 피보나치 수열
import pytest


def solution(x: int) -> int:
    """
    피보나치 수열의 x번째 값을 구하여 반환한다.
    피보나치 수열은 첫번째 값이 0, 두번째 값이 1이고,
    이후의 값은 이전 두 값의 합으로 이루어진다.

    Args:
        x: 0 또는 양의 정수

    Returns:
        int: 피보나치 수열의 해당 값
    """
    if x <= 1:
        return x

    return solution(x - 2) + solution(x - 1)


@pytest.mark.parametrize(
    "x, expected",
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)],
)
def test_solution(x, expected):
    assert solution(x) == expected
