from typing import List


def solution(d: List[int], budget: int) -> int:
    """
    부서별로 물품 구매에 필요한 금액과 예산이 주어질 때,
    예산 안에서 최대 몇 개의 부서에 물품을 지원할 수 있는지 세어서 반환한다.

    Args:
        d (List[int]): 각 부서가 신청한 금액이 담긴 리스트
        budget (int): 전체 예산

    Returns:
        int: 예산 내에서 지원 가능한 부서의 최대 개수

    Notes:
        idea: 각 부서의 신청 금액을 오름차순으로 정렬 후,
        작은 금액부터 예산에 맞춰 최대한 많은 부서를 지원한다.
        time complexity: O(nlogn), n개의 요소를 가진 리스트 d를
        정렬하는 데 소요되는 시간
        space complexity: O(1), in-place sort이므로 추가적인 메모리 사용 없이,
        상수 공간만 사용
    """
    d.sort()
    count = 0

    for cost in d:
        if budget < cost:
            break

        budget -= cost
        count += 1

    return count
