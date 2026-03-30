class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        for i in range(len(candidates)):
            if candidates[i] > target:
                candidates.pop(i)
        result = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            else:
                for j in self.combinationSum(candidates[i:], target-candidates[i]):
                    result.append([candidates[i]]+j)
        return result   
    