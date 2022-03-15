# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        min = 1
        max = n
        
        while min<=max:
            mid = (min+max)//2
            
            if isBadVersion(mid):
                max = mid - 1
            else:
                min = mid + 1
        return min
        
        