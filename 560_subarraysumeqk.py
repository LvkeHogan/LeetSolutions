class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        #Garbage solution
        count = 0
        for i in range(len(nums)):
            j = i
            while j < len(nums):
                if sum(nums[i:j + 1]) == k:
                    count += 1
                j += 1
        return count
        '''
        
        '''
        #attempt at an OK solution
        count = 0
        l = 0
        r = 0
        while r < len(nums) and l < len(nums):
            if sum(nums[l:r+1]) < k:
                r += 1
            elif sum (nums[l:r+1]) > k:
                l += 1
            else:
                count += 1
                l += 1
        return count

        #Surprise, doesn't work.
        '''

        #solution using prefix sums
        prefixsums = {0:1}
        count = 0
        arraysum = 0
        for n in nums:
            arraysum += n
            diff = arraysum - k
            count += prefixsums.get(diff,0)
            prefixsums[arraysum] = 1 + prefixsums.get(arraysum,0)
        return count 
            
            
                