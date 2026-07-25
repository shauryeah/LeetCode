class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        a=''
        for i in s:
            if stack:
                if stack[-1]==i:
                    stack.pop()
                    
                else:
                    stack.append(i)
            else:
                stack.append(i)
        for i in stack:
            a+=i
        return a