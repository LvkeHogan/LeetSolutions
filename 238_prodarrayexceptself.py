class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        #range(beginning, end, increment)
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result


        '''
        #my second solution, still slow what the heck
        #calculate prefix products in nums, going left to right in nums
        result = []
        for i in range(len(nums)):
            result.append(result[i - 1] * nums[i - 1])
        
        #calculate suffix prods into result array
        prod = 1
        for i in range(len(nums) - 2,-1,-1):
            prod *= nums[i - 1]
            result[i] *= prod
        return result
        
        #my first solution
        result = []
        #suffix will be built in reverse.
        prefixProd = []
        suffixProd = []
        for i in range(len(nums)):
            if i == 0:
                prefixProd.append(1)
                suffixProd.append(1)
            else:
            #compute prefix prod at element
                prefixProd.append(prefixProd[i - 1] * nums[i - 1])
            #cvompute suffix prod at element
                suffixProd.append(suffixProd[i - 1] * nums[len(nums) - i])
        print(prefixProd,suffixProd)
        for i in range(len(nums)):
            result.append(prefixProd[i] * suffixProd[len(nums) - 1 - i])
        return result

        '''