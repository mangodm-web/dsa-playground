from typing import List, Optional


class Node:
    def __init__(self, item: int) -> None:
        self.data = item
        self.next = None


class LinkedList:
    """
    연결 리스트(Linked List)
    """

    def __init__(self) -> None:
        self.node_count = 0
        self.head = None
        self.tail = None

    def get_at(self, pos: int) -> Optional[Node]:
        """
        주어진 pos에 위치한 노드를 반환한다.

        Args:
            pos (int): 연결 리스트의 n번째 정보 (1부터 인덱스 시작)

        Returns:
            Optional[Node]: n번째에 위치한 노드를 반환한다.
        """
        if pos < 1 or pos > self.node_count:
            return None

        current = self.head
        for _ in range(1, pos):
            current = current.next

        return current

    def traverse(self) -> List[int]:
        """
        연결리스트의 요소를 배열에 담아 반환한다.

        Returns:
            List[int]: 연결리스트의 요소가 담긴 배열
        """
        result = []

        for i in range(1, self.node_count + 1):
            node = self.get_at(i)
            result.append(node.data)

        return result

    def insert_at(self, pos: int, new_node: Node) -> bool:
        """
        연결리스트의 특정 위치에 주어진 노드를 추가한다.

        Args:
            pos (int): 노드를 추가할 위치 (1부터 인덱스 시작)
            new_node (Node): 추가할 노드

        Returns:
            bool: 노드를 추가했는지 여부
        """
        if pos < 1 or pos > self.node_count + 1:
            return False

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            if pos == self.node_count + 1:
                prev = self.tail
            else:
                prev = self.get_at(pos - 1)
            new_node.next = prev.next
            prev.next = new_node

        if pos == self.node_count + 1:
            self.tail = new_node

        self.node_count += 1
        return True

    def pop_at(self, pos: int) -> int:
        """
        주어진 위치에 있는 노드를 제거하고, 제거된 노드의 데이터를 반환한다.

        Args:
            pos (int): 제거할 노드의 위치 (1부터 인덱스 시작)

        Raises:
            IndexError: 주어진 위치가 1보다 작거나 노드 전체 수보다 클 경우

        Returns:
            int: 제거된 노드의 데이터
        """
        if pos < 1 or pos > self.node_count:
            raise IndexError

        if pos == 1:
            current = self.head
            self.head = self.head.next
            current.next = None
        else:
            prev = self.get_at(pos - 1)
            current = prev.next

            if pos == self.node_count:
                self.tail = prev
                self.tail.next = None
            else:
                prev.next = current.next
                current.next = None

        self.node_count -= 1

        if self.node_count == 0:
            self.head, self.tail = None, None

        return current.data
