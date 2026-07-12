class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        k=0
        j=-1
        for i in range(len(s)//2):
            s[k],s[j]=s[j],s[k]
            k+=1
            j-=1
