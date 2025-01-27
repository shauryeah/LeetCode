class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L=[]
        for i in s:
            if i.isalnum()==True:
                L.append(i.lower())
        if L==L[::-1]:
            return True
        else:
            return False