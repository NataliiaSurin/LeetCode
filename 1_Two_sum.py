def two_sum(nums: list[int], target: int) -> list[int]:
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x] + nums[y] == target and x != y:
                indices = [x, y]
                return indices


print(two_sum([3, 3], 6))