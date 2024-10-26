class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = { i: [] for i in range(n) }

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()

        def DFS(v: int) -> None:
            visited.add(v)

            for adj in graph[v]:
                if adj not in visited:
                    DFS(adj)

        DFS(0)

        return len(visited) == n
