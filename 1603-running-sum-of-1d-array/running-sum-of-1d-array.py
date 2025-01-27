class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[nums[0]]
        sum=0
        for i in range(1,len(nums)):
            for j in range(i+1):
                sum=sum+nums[j]
            a.append(sum)
            sum=0
        return a

        