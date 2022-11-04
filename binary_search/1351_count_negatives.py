'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
'''


def countNegatives(grid: list[list[int]]) -> int:
    col_size = len(grid[0])
    total = 0
    index = 0
    for row in reversed(grid):
        for i in range(index, col_size):
            if row[i] < 0:
                total += 1
            else:
                index = i + 1

    return total


grid = [[-11]]
print(countNegatives(grid))
