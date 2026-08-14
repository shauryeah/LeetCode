class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                ans[i]=0
                stack.append(i)
            while(stack and temperatures[i]>=temperatures[stack[-1]]):
                stack.pop()
            if(stack):
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans












































































































        