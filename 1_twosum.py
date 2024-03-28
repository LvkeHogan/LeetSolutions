class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberhashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numberhashmap:
                return [numberhashmap[diff],i]
            else:
                numberhashmap[nums[i]] = i
