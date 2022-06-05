class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target-nums[i]) != i:
                    li.append(i)
                    li.append(nums.index(target-nums[i]))
                    return li