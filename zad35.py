class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target<nums[0]:
            return 0
        for i in range(1, len(nums)):
            if target<nums[i]:
                return i
        return len(nums)