"""
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
---
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        self.r = len(grid)
        self.c = len(grid[0])
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count +=1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=self.r or j>=self.c or grid[i][j]!="1":
            return
        grid[i][j] = '#'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))