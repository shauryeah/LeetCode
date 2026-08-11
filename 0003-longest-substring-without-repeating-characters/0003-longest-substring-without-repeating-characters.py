class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited=set()
        left=0
        maxx=0
        cnt=0
        for right in range(len(s)):
            while(s[right] in visited):
                maxx=max(cnt,maxx)
                if(s[left] in visited):
                    visited.remove(s[left])
                left+=1
                cnt-=1
            cnt+=1
            visited.add(s[right])

        maxx=max(maxx,cnt)
        return maxx



        