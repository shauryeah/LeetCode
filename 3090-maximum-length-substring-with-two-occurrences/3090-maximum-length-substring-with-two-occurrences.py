class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited={}
        for i in s:
            if i not in visited:
                visited[i]=0
        maxx=0
        left=0
        maxxcount=0
        for right in range(len(s)):
            visited[s[right]]+=1
            maxxcount=max(maxxcount,visited[s[right]])
            while(maxxcount>2):
                visited[s[left]]-=1
                if(s[left]==s[right]):
                    maxxcount=visited[s[left]]
                left+=1
            maxx=max(maxx,right-left+1)
        return maxx