from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]< target:
                left = mid + 1
            else: right = mid - 1
        return -1
    def binary_search(self, nums: List[int], target: int, left, right) -> int:
        if left>right:
            return -1
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(self, nums,target, mid + 1, right)
        else: return self.binary_search(self, nums, target, left, mid-1)

    
nums = [-1,0,3,5,9,12]
target = 9
sol = Solution()
print(sol.search(nums, target))