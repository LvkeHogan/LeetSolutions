class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_index = 0
        substr = set()
        maxlen = 0
        
        for r_index in range(len(s)):
            #condition to handle when a dupe exists
            while s[r_index] in substr:
                substr.remove(s[l_index])
                l_index += 1
            substr.add(s[r_index])
            if maxlen < len(substr):
                maxlen = len(substr)
        return maxlen