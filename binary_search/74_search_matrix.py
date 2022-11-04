'''
Write an efficient algorithm that searches for a value target
in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''
import bisect


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if row[-1] >= target:
            index = bisect.bisect_left(row, target)
            if row[index] == target:
                return True
            break
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))


# other's solution
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    first, last = 0, rows * cols - 1

    while first <= last:
        mid = (first + last) // 2
        if matrix[mid // cols][mid % cols] == target:
            return True
        if matrix[mid // cols][mid % cols] > target:
            last = mid - 1
        if matrix[mid // cols][mid % cols] < target:
            first = mid + 1

    return False






