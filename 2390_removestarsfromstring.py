class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        #use a set, because it already doesn't tolerate duplicates, and order + index don't necessarily matter
        set1 = set(nums1)
        set2 = set(nums2)
        nums1U = []
        nums2U = []
  
        for num in set1:
            if num not in set2:
                nums1U.append(num)
        for num in set2:
            if num not in set1:
                nums2U.append(num)
            

        return nums1U, nums2U