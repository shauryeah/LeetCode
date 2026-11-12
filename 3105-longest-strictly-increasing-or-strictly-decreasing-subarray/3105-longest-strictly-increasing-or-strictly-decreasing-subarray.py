class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc=1
        dec=1
        longest=1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                inc+=1
                dec=1
            elif(nums[i]<nums[i-1]):
                inc=1
                dec+=1
            else:
                inc=1
                dec=1
            longest=max(longest,inc,dec)
        return longest