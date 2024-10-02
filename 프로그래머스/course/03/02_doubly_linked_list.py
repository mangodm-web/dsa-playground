from typing import List, Optional


class Node:
    def __init__(self, item: int) -> None:
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """양방향 연결 리스트"""

    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self) -> List[int]:
        """
        양방향 연결 리스트의 앞에서부터 맨 뒤까지 순회하여 각 노드의 데이터를 리스트에 담아 반환한다.

        Returns:
            List[int]: 노드의 데이터가 담긴 리스트
        """
        nodes = []

        current = self.head

        for _ in range(self.node_count):
            current = current.next
            nodes.append(current.data)

        return nodes

    def get_at(self, pos: int) -> Optional[Node]:
        if pos < 1 or pos > self.node_count:
            return None

        i = 0
        mid_pos = self.node_count // 2

        if pos > mid_pos:
            current = self.tail

            while i < self.node_count - pos + 1:
                current = current.prev
                i += 1
        else:
            current = self.head

            while i < pos:
                current = current.next
                i += 1

        return current

    def reverse(self) -> List[int]:
        """
        양방향 연결 리스트의 끝에서부터 맨 앞까지 순회하여 각 노드의 데이터를 리스트에 담아 반환한다.

        Returns:
            List[int]: 노드의 데이터가 담긴 리스트
        """
        nodes = []

        current = self.tail

        for _ in range(self.node_count):
            current = current.prev
            nodes.append(current.data)

        return nodes

    def insert_before(self, next: Node, new_node: Node) -> bool:
        """
        주어진 노드의 이전 위치에 새로운 노드 추가

        Args:
            next (Node): 새로운 노드 다음에 위치한 노드
            new_node (Node): 추가할 노드
        """
        prev = next.prev

        prev.next = new_node
        new_node.prev = prev
        new_node.next = next
        next.prev = new_node

        self.node_count += 1
        return True
