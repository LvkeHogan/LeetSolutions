class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1
        
        while ptr2 > ptr1:
            result = numbers[ptr1] + numbers[ptr2]
            if result > target:
                ptr2 -= 1
            elif result < target:
                ptr1 += 1
            else:
                return [ptr1 + 1,ptr2 + 1]
