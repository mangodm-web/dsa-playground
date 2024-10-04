from typing import List


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    """
    각 작업의 진도와 작업 속도를 바탕으로 매 배포마다 완료된 기능의 개수를 계산하여 반환한다.

    Args:
        progresses (List[int]): 각 작업의 현재 진행 상태를 나타내는 리스트 (100 미만 자연수)
        speeds (List[int]): 각 작업의 속도를 나타내는 리스트 (100 이하의 자연수)

    Returns:
        List[int]: 각 배포마다 몇 개의 기능이 배포되는지가 담긴 리스트

    Notes:
        idea:
            1. 각 작업의 진도와 작업 속도를 하나의 작업 단위로 묶어 큐에 저장한다.
            2. 매일 모든 작업의 진행 상태를 업데이트하고, 첫번째 작업이 완료되었을 때 큐에서 제거한다.
            - 이때, 그 뒤의 작업들도 같이 배포할 수 있는지 확인한다.
            - 완료된 작업들은 큐에서 제거하며, 해당 배포에 반영할 수 있는 기능의 개수를 세어서 결과 리스트에 저장한다.
            3. 큐 안의 모든 작업이 처리될 때까지 이 과정을 반복한다.
        time complexity: O(n^2), n은 전체 작업의 수(progressses, speeds 배열의 길이).
            매일 모든 작업의 진행 상태를 업데이트하고, 작업이 완료될 때마다 큐에서 제거하는 과정에서
            이중 루프가 발생할 수 있다.
        space complexity: O(n), n은 전체 작업의 수
            큐와 결과 리스트에 최대 n개의 값이 저장될 수 있다.
    """
    result = []
    q = [
        {"progress": progress, "speed": speed}
        for progress, speed in zip(progresses, speeds)
    ]

    while q:
        q = [
            {"progress": elem["progress"] + elem["speed"], "speed": elem["speed"]}
            for elem in q
        ]

        if q[0]["progress"] >= 100:
            feature_count = 0

            while q and q[0]["progress"] >= 100:
                q.pop(0)
                feature_count += 1

            result.append(feature_count)

    return result
