# 463. Island Perimeter
#
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
#
#
#
# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
# Input: grid = [[1,0]]
# Output: 4
#
#
# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        positions_visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in positions_visited:
                return 0

            positions_visited.add((i, j))

            perimeter = dfs(i, j)
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i - 1, j)

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
