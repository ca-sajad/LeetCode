'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
'''


def isPerfectSquare(num: int) -> bool:
    start = 1
    end = num

    while start <= end:
        mid = (start + end) // 2
        square = mid * mid
        if square == num:
            return True
        elif square > num:
            end = mid - 1
        else:
            start = mid + 1
    return False


# Newton's method
def squareRoot(n, l):
    # Assuming the sqrt of n as n only
    x = n
    while True:
        # Calculate more closed x
        root = 0.5 * (x + (n / x))
        # Check for closeness
        if (abs(root - x) < l):
            break
        # Update root
        x = root
    return root


print(isPerfectSquare(3600))
print(squareRoot(16, 0.01))











