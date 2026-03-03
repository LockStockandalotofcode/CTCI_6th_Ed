class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build adjacency list and in-degree array 
        adj = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # 2. make queue of 0- prerequisite courses
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        finish_counter = 0 

        # 3. process the queue
        while queue:
            curr = queue.popleft()
            finish_counter += 1

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. If we finished all courses, then no cycle exists
        return finish_counter == numCourses