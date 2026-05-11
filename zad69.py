class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 0
        right = x
        while left<=right:
            mid = (left+right)/2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return int(mid)
            elif mid*mid < x:
                left = mid +1
            else: right = mid - 1
        return 0


sol = Solution()
print(sol.mySqrt(8))