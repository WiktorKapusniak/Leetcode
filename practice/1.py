nums = [2,3,11,7]
target = 9
# wynik: [0,1]

from typing import List


def twoSum(nums, target) -> List[int]: 
    seen = {}

    for i, num in enumerate(nums):
        rest = target - num
        if rest in seen:
            return [seen[rest], i]
        
        seen[num] = i
    
    return []

print(twoSum(nums, target))
print(enumerate(nums))