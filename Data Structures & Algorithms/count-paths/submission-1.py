class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vis = {}
        def dfs(r, c):
            if r == m - 1 or c == n - 1:
                return 1 # only one path for bottom row or last col
            
            if (r, c) in vis:
                return vis[(r, c)] # return valid paths from this point
            vis[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return vis[(r, c)]

        
        return dfs(0, 0)