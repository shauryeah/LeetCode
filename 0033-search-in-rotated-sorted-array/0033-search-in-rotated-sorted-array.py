class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
            elif(nums[left]<=nums[mid]):
                if(nums[left]<=target and target<=nums[mid]):
                    right=mid-1
                else:
                    left=mid+1
            
            elif(nums[left]>nums[mid]):
                if(nums[right]>=target and nums[mid]<=target):
                    left=mid+1
                else:
                    right=mid-1
            
        return -1

