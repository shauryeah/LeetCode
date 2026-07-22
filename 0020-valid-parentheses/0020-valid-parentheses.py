class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in['(','{','[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                m=stack.pop()
                if i==')':
                    if m!='(':
                        return False
                elif(i=="}"):
                    if m!='{':
                        return False
                else:
                    if m!='[':
                        return False
        return len(stack)==0
                    
        