class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        def bfs(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            islands = 0
            q = deque([(r, c)])
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr, nc))
                            q.append((nr, nc))
                islands += 1

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    bfs(i, j)
                    islands += 1
        
        return islands

        