from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i = len(nums) - 1
    while i > 0:
        if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
        i -= 1
    return len(nums)
