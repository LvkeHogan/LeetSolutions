class Solution:
    def reverseWords(self, s: str) -> str:

        #Quick dirty Pythonic way
        wordList = s.split()
        wordList.reverse()
        return " ".join(wordList)
        