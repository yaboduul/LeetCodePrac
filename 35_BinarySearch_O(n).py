class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            ans = (start+end)//2
            if nums[ans] == target:
                return ans
            elif nums[ans] > target:
                end = ans - 1
            elif nums[ans] < target:
                start = ans +1
        return start