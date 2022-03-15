class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return nums.index(nums[i])
        return -1