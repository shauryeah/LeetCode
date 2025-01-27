class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        cont=0
        for i in words:
            if i[::-1]==i:
                return i
                cont+=1
            else:
                continue
        if cont==0:
            return ""