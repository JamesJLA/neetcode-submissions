class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        output = []
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prereq in courses[course]:
                if not dfs(prereq):
                    return False

            visited.add(course)
            visiting.remove(course)
            output.append(course)
            return True

        for course in courses:
            if not dfs(course):
                return []

        return output
