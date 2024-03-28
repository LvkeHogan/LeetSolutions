class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        #we need to go with minimum length
        minlength = min(lengths)
        common = ""
        flag = True
        for i in range(minlength):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    flag = False
            if flag == True:
                common = common + char
        return common


