class Solution:
    def groupAnagrams(self, strs):
        output = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in output:
                output[''.join(sorted(i))].append(i)
            else: output[''.join(sorted(i))] = [i]
        return list(output.values())


strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))