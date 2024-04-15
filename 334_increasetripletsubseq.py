class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = inf
        num2 = inf

        for num in nums:
            if num > num2:
                return True
            if num > num1:
                num2 = min(num2, num)
            num1 = min(num1, num)
        return False

            
            
                

        