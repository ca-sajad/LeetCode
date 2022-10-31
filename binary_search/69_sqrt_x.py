'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''


# binary search
def mySqrt(n: int) -> int:
    start = 0
    end = n

    while True:
        mid = (end + start) // 2
        if (mid) ** 2 <= n < (mid + 1) ** 2:
            return mid
        elif mid ** 2 > n:
            end = mid - 1
        else:
            start = mid + 1


print(mySqrt(0))


# Newton's method
def mySqrt2(n: int) -> int:
    # Assuming the sqrt of n as n only
    if n == 0:
        return n
    x = n
    l = 0.1
    while True:
        # Calculate more closed x
        root = 0.5 * (x + (n / x))
        # Check for closeness
        if (abs(root - x) < l):
            break
        # Update root
        x = root
    return int(root)


