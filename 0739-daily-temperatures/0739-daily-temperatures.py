class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i]>temperatures[stack[-1]]:
                    k=stack.pop()
                    ans[k]=i-k
                stack.append(i)
        return ans









































































































        