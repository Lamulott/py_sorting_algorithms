import random


def quicksort2(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    left = []
    right = []
    equal = []
    for i in nums:
        if i < pivot:
            left.append(i)
        if i > pivot:
            right.append(i)
        if i == pivot:
            equal.append(i)
    return quicksort2(left) + equal + quicksort2(right)


print(quicksort2([3, 6, 5, 9, -24, 0]))
print(quicksort2([]))
print(quicksort2([0]))
