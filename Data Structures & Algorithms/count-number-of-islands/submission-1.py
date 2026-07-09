class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #rows=m & cols=n
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            else:
                #mark visited node as 0 to avoid revisit
                grid[r][c] = "0"
                dfs(r, c+1) #right
                dfs(r+1, c) #down
                dfs(r, c-1) #left
                dfs(r-1, c) #up

        num_islands = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r,c)
        return num_islands

#time and space: O(rows * cols)