class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def back(s,openn,closee):
            if(len(s)==2*n):
                ans.append(s)
                return
            if openn<n:
                back(s+'(',openn+1,closee)
            if closee<openn:
                back(s+')',openn,closee+1)
        back('',0,0)
        return ans
