from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            water_amount = min(height[left],height[right]) * (right - left)
            if water_amount>max:
                max = water_amount
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max