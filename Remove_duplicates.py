class RemoveDuplicates:
    def removeDuplicates(self, nums):
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i]);

        return len(nums);


nums = [0,0,0,1,1,2,2,2,3,4];
obj = RemoveDuplicates();
obj.removeDuplicates(nums);