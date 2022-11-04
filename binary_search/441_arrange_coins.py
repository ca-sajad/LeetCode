'''
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins.
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
'''

def arrangeCoins(n: int) -> int:
    start = 0
    end = n

    while True:
        mid = (start + end) // 2
        if f(mid) <= n < f(mid + 1):
            return mid
        elif f(mid) < n:
            start = mid + 1
        else:
            end = mid - 1


def f(n):
    return n * (n + 1) / 2


print(arrangeCoins(7))