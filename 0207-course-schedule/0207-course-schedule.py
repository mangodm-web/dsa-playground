class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = set()
        def DFS(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True

            visited.add(course)
            for prerequisite in graph[course]:
                if not DFS(prerequisite):
                    return False
            
            visited.remove(course)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not DFS(course):
                return False
        
        return True
