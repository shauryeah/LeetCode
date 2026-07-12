class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new=''
        for i in s:
            if i.isalnum():
                new+=i
        left=0
        right=len(new)-1
        while(left<right):
            if new[left].lower()!=new[right].lower():
                return False
            left+=1
            right-=1
        return True
