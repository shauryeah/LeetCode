class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        if(nums[left]<=nums[right]):
                return nums[left]
        while(left<right):
            mid=(left+right)//2
            if(nums[mid+1]<nums[mid]):
                return nums[mid+1]
            elif(nums[left]<=nums[mid]):
                left=mid+1
            else:
                right=mid
        