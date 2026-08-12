class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zerocount=0
        onecount=0
        left=0
        maxx=0
        for right in range(len(nums)):
            if(nums[right]==0):
                zerocount+=1
            elif(nums[right]==1):
                onecount+=1
            while(zerocount>k):
                maxx=max(maxx,onecount+k)
                if(nums[left]==1):
                    onecount-=1
                    left+=1
                else:
                    zerocount-=1
                    left+=1
            maxx=max(maxx,onecount+zerocount)
        return maxx

