from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        max_frequency = 0

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1

            if frequencies[num] > max_frequency:
                max_frequency = frequencies[num]

        buckets = [[] for _ in range(max_frequency + 1)]
        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        result = []
        for frequency in range(max_frequency, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))
