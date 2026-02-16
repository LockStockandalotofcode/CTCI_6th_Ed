class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        # form adjacency list and indegrees a list holding no. of indegrees for course number defined by index
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegrees[course] += 1

        # deque for traversal 
        # result gets stored in list - order by the end
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for dependent in adj[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    queue.append(dependent)
                
        return [] if len(order) < numCourses else order