# 1289. Minimum Falling Path Sum II
#
#
# Given an n x n integer matrix grid, return the minimum sum of a falling path
# with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from
# each row of grid such that no two elements chosen in adjacent rows are in the
# same column.
#
#
#
# Example 1:
#      1    2    3
#      4    5    6
#      7    8    9
#
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# Example 2:
#
# Input: grid = [[7]]
# Output: 7
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:

        # t = O(n^3) s = O(n^2)
        # N = len(grid)
        # cache = {} # type: ignore
        #
        # def helper(r,c):
        #     if r == N -1:
        #         return grid[r][c]
        #
        #     if (r,c) in cache:
        #         return cache[(r,c)]
        #
        #     res = float("inf")
        #     for next_col in range(N):
        #
        #         if c != next_col:
        #             res = min(
        #                 res,
        #                 grid[r][c] + helper(r+1,next_col)
        #             )
        #     cache[(r,c)] = res
        #
        #     return res
        #
        # res = float("inf")
        #
        # for c in range(N):
        #     res = min(res,helper(0,c))
        #
        # return res

        # Dp
        # time = O(n^3)  s --> O(2n)

        # N = len(grid)
        #
        # dp = grid[0]
        #
        # for r in range(1, N):
        #
        #     next_dp = [float("inf")] * N
        #
        #     for curr_c in range(N):
        #         for prev_c in range(N):
        #             if prev_c != curr_c:
        #                 next_dp[curr_c] = min(
        #                     next_dp[curr_c], grid[r][curr_c] + dp[prev_c]
        #                 )
        #     dp = next_dp
        #
        # return min(dp)
        #

        def get_min_two(row):
            two_smallest = [] # (val,index)
            
            for val , idx in row:
                if len(two_smallest) < 2:
                    two_smallest.append((val,idx))
                elif two_smallest[1][0] > val:
                    two_smallest.pop()
                    two_smallest.append((val,idx))
                two_smallest.sort()

            return two_smallest
        
        N = len(grid)
        first_row = [(val,idx) for idx,val in enumerate(grid[0])]
        dp = get_min_two(first_row):
    
        for r in range(1,N):
            next_dp = [] # (val,idx)
            for curr_c in range(N):
                curr_val = grid[r][curr_c]
                min_val = float("inf")
                for prev_val,prev_c in dp:
                    if curr_c != prev_c:
                        min_val = min(min_val,curr_val+prev_val)
                next_dp.append((min_val,curr_c))
                next_dp = get_min_two(next_dp)
            dp = next_dp

        return min([val for val, idx in dp])

            
