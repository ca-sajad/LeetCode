'''
Given two integer arrays arr1 and arr2, and the integer d,
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i]
such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
'''


def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    counter = 0
    for i in range(len(arr1)):
        flag = True
        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) <= d:
                flag = False
                break
        if flag:
            counter += 1
    return counter


def findTheDistanceValue2(A, B, d):
        return sum(all(abs(a - b) > d for b in B) for a in A)


import bisect
def findTheDistanceValue3(arr1: list[int], arr2: list[int], d: int) -> int:
    arr2.sort()
    if arr2 and arr1:
        counter = len(arr1)
        for a in arr1:
            ind = bisect.bisect_left(arr2, a)
            if ind < len(arr2):
                if arr2[ind] and (abs(arr2[ind] - a) <= d) or \
                    arr2[ind - 1] and (abs(arr2[ind - 1] - a) <= d):
                    counter -= 1
            else:
                if arr2[ind - 1] and (abs(arr2[ind - 1] - a) <= d):
                    counter -= 1
    else:
        counter = 0
    return counter



arr1 = [-3,10,2,8,0,10]
arr2 = [-9,-1,-4,-9,-8]
d = 9
import time
t1 = time.time()
for _ in range(10**4):
    findTheDistanceValue(arr1, arr2, d)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
for _ in range(10**4):
    findTheDistanceValue2(arr1, arr2, d)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
for _ in range(10**4):
    findTheDistanceValue3(arr1, arr2, d)
t2 = time.time()
print(t2 - t1)

print(findTheDistanceValue(arr1, arr2, d))
print(findTheDistanceValue2(arr1, arr2, d))
print(findTheDistanceValue3(arr1, arr2, d))