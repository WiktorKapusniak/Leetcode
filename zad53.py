from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
        return max_global
    
sol = Solution()
print(sol.maxSubArray([5,4,-1,7,8]))