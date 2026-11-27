class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = { i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            courses[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        processed = 0

        while queue:
            course = queue.popleft()

            for prereq in courses[course]:
                indegree[prereq] -= 1

                if indegree[prereq] == 0:
                    queue.append(prereq)
            processed += 1

        return processed == numCourses