'''
ou are given an array of characters letters that is sorted in non-decreasing
order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than
target. If such a character does not exist, return the first character in letters.


Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
'''


def nextGreatestLetter(letters: list[str], target: str) -> str:
    if target >= letters[-1]:
        return letters[0]

    start = 0
    end = len(letters)
    while True:
        mid = (end + start) // 2
        if mid == 0 and letters[mid] > target:
            return letters[mid]
        elif letters[mid - 1] <= target < letters[mid]:
            return letters[mid]
        elif target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1


letters = ["c","f","j"]
target = "k"
print(nextGreatestLetter(letters, target))
