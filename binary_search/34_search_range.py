'''
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''
import bisect


def searchRange(nums: list[int], target: int) -> list[int]:
    l, r = -1, -1
    if nums:
        size = len(nums)
        start = 0
        end = size - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid - 1] != target or mid == 0:
                    l = mid
                    r = bisect.bisect_right(nums, target) - 1
                    break
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

    return [l, r]


nums = [5,7,7,7,7,8,8,10,10,10]
target = 7
print(searchRange(nums, target))