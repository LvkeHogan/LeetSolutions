class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 < pointer2:
            s[pointer1],s[pointer2] =  s[pointer2],s[pointer1]

            pointer1 += 1
            pointer2 -= 1
