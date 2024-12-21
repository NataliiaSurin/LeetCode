def removeDuplicates(nums: list[int]) -> int:
    myset = set((nums))
    nums = list((myset))
    print(nums)
    return len(nums)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))