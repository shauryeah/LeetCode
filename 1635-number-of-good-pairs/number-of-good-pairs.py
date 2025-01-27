class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        count=0
        for i in range(0,length):
            for j in range(i+1,length):
                if nums[i]==nums[j]:
                    count+=1
        return count    