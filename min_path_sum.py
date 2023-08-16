class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def recur(i:int,j:int)->int:
            if i < 0 or j < 0:
                return maxsize
            elif i == j == 0:
                return grid[0][0]
            else:
                return grid[i][j] + min(recur(i-1,j),recur(i,j-1))
        return recur(len(grid) - 1, len(grid[0]) - 1)
