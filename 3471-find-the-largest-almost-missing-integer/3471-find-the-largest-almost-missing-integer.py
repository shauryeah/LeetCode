class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nmap={}
        for i in range(len(nums)-k+1):
            subarr=nums[i:i+k]
            for x in set(subarr):
                nmap[x]=nmap.get(x,0)+1
        ans=-1
        for x in nmap:
            if nmap[x]==1:
                ans=max(ans,x)
        return ans
