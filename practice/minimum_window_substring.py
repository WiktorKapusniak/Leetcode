class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        required = len(need)
        formed = 0

        minimum = float("inf")
        min_left = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < minimum:
                    minimum = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        if minimum == float("inf"):
            return ""
        return s[min_left:min_left + minimum]


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))