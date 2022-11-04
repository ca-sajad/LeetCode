'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''
import bisect


def twoSum(numbers: list[int], target: int) -> list[int]:
    mid = bisect.bisect_left(numbers, target // 2)
    if (index1 := mid - 1) >= 0:
        while index1 >= 0:
            if (index2 := find_index2(index1, numbers, target)) != -1:
                return [index1 + 1, index2 + 1]
            index1 -= 1

        index1 = mid
        if (index2 := find_index2(index1, numbers, target)) != -1:
            return [index1 + 1, index2 + 1]

    if (index1 := mid) == 0:
        if (index2 := find_index2(index1, numbers, target)) != -1:
            return [index1 + 1, index2 + 1]


def find_index2(index1, numbers, target):
    new_target = target - numbers[index1]
    index = bisect.bisect_right(numbers, new_target)
    if numbers[index1] + numbers[index - 1] == target:
        return index - 1
    return -1

numbers = [-3,3,11,15]
target = 0
print(twoSum(numbers, target))


'''
other people's solutions
'''
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1

# dictionary
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i









