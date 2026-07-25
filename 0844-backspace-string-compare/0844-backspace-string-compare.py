class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for i in s:
            if stack1 and i=='#':
                stack1.pop()
            else:
                if i!='#':
                    stack1.append(i)
        for j in t:
            if stack2 and j=='#':
                stack2.pop()
            else:
                if j!='#':
                    stack2.append(j)
        return stack1==stack2