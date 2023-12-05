def merge_sort(left: list[int], right: list[int]) -> list[int]:
    N, M = len(left), len(right)
    if N == 0 and M == 0:
        return []
    if N == 1 and M == 1:
        res = [*min(left, right), *max(left, right)]
        return res
    i = j = 0
    merge = []
    while i < N and j < M:
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    merge += left[i:] + right[j:]
    return merge


def split_and_merge(nums: list[int]) -> list[int]:
    pivot = len(nums) // 2
    left, right = nums[:pivot], nums[pivot:]

    if len(left) > 1:
        left = split_and_merge(left)
    if len(right) > 1:
        right = split_and_merge(right)

    return merge_sort(left, right)


print(split_and_merge([3, 6, 5, 9, -24, 0]))
print(split_and_merge([]))
print(split_and_merge([0]))