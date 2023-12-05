def intersection_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp
    return nums


numbers = [3, 6, 5, 9, -24, 0]
print(intersection_sort(numbers))