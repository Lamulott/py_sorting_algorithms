def bubble_sort(nums: list[int]) -> list[int]:
    i = 1
    while i < len(nums):
        for j in range(len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        i += 1
    return nums


numbers = [3, 6, 5, 9, -24, 0]
print(bubble_sort(numbers))