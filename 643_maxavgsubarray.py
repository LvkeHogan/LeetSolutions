class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ptr1 = 0
        ptr2 = k - 1
        maxsum = sum(nums[ptr1:ptr2 + 1])
        #initialize csum
        csum = maxsum

        while ptr2 <= len(nums) - 2:
            csum -= nums[ptr1]
            ptr1 += 1
            ptr2 += 1
            csum += nums[ptr2]
            if csum > maxsum:
                maxsum = csum
        return maxsum / k
            
        