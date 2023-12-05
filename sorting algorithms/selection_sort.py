def selection_sort(nums: list[int]) -> list[int]:
    c = len(nums)
    for i in range(c):
        current_min = nums[i]
        min_index = i
        for j in range(i, c):
            if nums[j] < current_min:
                current_min = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


numbers = [3, 6, 5, 9, -24, 0]
print(selection_sort(numbers))
