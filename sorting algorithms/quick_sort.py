def quicksort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    N = len(nums)
    pivot = nums[N // 2]
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
    return quicksort(left) + equal + quicksort(right)


print(quicksort([3, 6, 5, 9, -24, 0]))
print(quicksort([]))
print(quicksort([0]))
