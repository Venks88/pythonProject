class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        return [i, j]


nums = [3, 2, 4]
target = 6
obj = Solution()
obj.twoSum(nums, target)
