class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # goal = len(nums) - 1

        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return True if goal == 0 else False
        maxjump = 0
        for i,num in enumerate(nums):
            if num != 0:
                jump = num + i
            else:
                jump = 0

            if i > maxjump:
                return False

            if jump > maxjump:
                maxjump = jump

            print(maxjump)
        return True


        

        