class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for number in nums:
            if number not in hashset:
                hashset.add(number)
            else:
                return True
        return False