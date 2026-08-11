class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        maxx=0
        cnt=0
        for right in range(len(s)):
            if s[right].lower() in 'aeiou':
                cnt+=1
            while(right-left+1==k):
                maxx=max(maxx,cnt)
                if s[left].lower() in 'aeiou':
                    cnt-=1
                left+=1
        return maxx
            
